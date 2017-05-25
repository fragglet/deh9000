"""Python types which emulate C types."""

from __future__ import print_function
import copy
import re
import unittest

# Regexp that matches field assignment lines in dehacked files.
FIELD_ASSIGNMENT_RE = re.compile(r"\s*(?P<deh_name>\w[\w \#\.\/]+[\w\#])*"
                                 r"\s*=\s*"
                                 r"\s*(?P<value>\-?\d+)"
                                 r"\s*$", re.I)

class Enum(list):
	"""Wrapper around list that represents a C enum type."""
	def __init__(self, values):
		super(Enum, self).__init__(values)

	def create_globals(self, globals):
		"""Create constants in the given global dict."""
		for index, name in enumerate(self):
			globals[name] = index

class EnumSet(set):
	"""Wrapper around set for representing a set of enum values.

	This is in practical terms identical to a set of integers, but those
	values are assumed to be indexes into an Enum and the __repr__ method
	will represent the values in their symbolic form.
	"""
	def __init__(self, enum_type, values):
		super(EnumSet, self).__init__(values)
		self.enum_type = enum_type

	def __repr__(self):
		return "{%s}" % (
			", ".join(self.enum_type[i] for i in self)
		)

class StructField(property):
	"""Helper wrapper around property() for declaring C struct fields.

	This is used with Struct() (see below). Fields are declared in the
	following way:

		class MyStruct(c.Struct):
			DEHACKED_NAME = "My Struct Type"
			field1 = c.StructField("First Field")
			action = c.StructField(None)

	The dehacked name for the field must be provided (which usually differs
	to the property name used in the Doom source). Providing a value of
	"None" indicates that although a value can be stored for that field,
	no output should be ever produced to represent it. This is commonly
	used when the field represents a pointer type.
	"""
	instance_order = 0
	def __init__(prop, deh_name):
		field_number = StructField.instance_order
		StructField.instance_order += 1
		prop.order = field_number
		prop.deh_name = deh_name

		def getter(self):
			return self._fields[field_number]
		def setter(self, value):
			self._fields[field_number] = value
		super(StructField, prop).__init__(getter, setter)

class Struct(object):
	"""Base class for a type that emulate a C struct.

	Fields are declared using the StructField type; the order in which
	they are declared is preserved when initialization is performed; this
	allows objects to be instantiated similar to C struct initializers.
	Original values used when instantiating an object of this class are
	also remembered, so that they can be diffed against later when
	changes are made.

	Example:
		class Coordinate(c.Struct):
			DEHACKED_NAME = "Co-ordinate"
			x = c.StructField("X Value")
			y = c.StructField("Y Value")

		xy = Coordinate(20, 30)
		xy.x = 3
		xy.y = 5
		print(xy.dehacked_diffs(array_index=99))

		xy2 = Coordinate(50, 5)
		print(xy2.dehacked_diffs(xy))
	"""

	def __init__(self, *args, **kwargs):
		# Start with all fields initialized to zero, then override.
		self._fields = {}
		for f in self.field_names():
			setattr(self, f, 0)
		self.set_values(*args, **kwargs)
		# The 'original' pointer points back to the original struct
		# that this instance was copy.copy()d from. By default, the
		# struct points to itself as the original.
		self.original = self

	@classmethod
	def header_regexp(cls):
		return re.compile(r"%s\s+(?P<index>\d+)(\s*\(.*\))?\s*$" % (
			cls.DEHACKED_NAME))

	@classmethod
	def field_names(cls):
		props = []
		for f in dir(cls):
			value = getattr(cls, f)
			if isinstance(value, StructField):
				props.append((f, value))
		props = sorted(props, key=lambda x: x[1].order)
		return [name for name, _ in props]

	def _apply_assignment(self, stream, deh_name, value):
		try:
			field = self.deh_field_name(deh_name)
			setattr(self, field, int(value))
		except KeyError:
			stream.exception("parse error: unknown field %r" % (
				deh_name))

	def parse_section(self, stream, index="0"):
		"""Parse a section, reading assignments from the given stream.

		It is assumed that each line will be an assignment that
		conforms to FIELD_ASSIGNMENT_RE. The function will return once
		an empty line is reached.
		"""
		while True:
			line = stream.readline()
			if line.strip() == "":
				break
			m = FIELD_ASSIGNMENT_RE.match(line)
			if not m:
				stream.exception("parse error: %r" % line)
			self._apply_assignment(stream, **m.groupdict())

	def copy_from(self, other):
		"""Copy all field values from another struct.

		Every field will be overwritten to be identical to the other
		struct, which must be of the same type.
		"""
		assert type(self) == type(other), (
			"Structs must be of the same type, %r != %r" % (
				type(self), type(other),
			))
		for field_name in self.field_names():
			value = getattr(other, field_name)
			setattr(self, field_name, value)

	def set_values(self, *args, **kwargs):
		"""Set the values of all fields in the struct.

		This is the same as what happens at instantiation time,
		but can be used to overwrite many fields all at once.
		For example:

		c = Coordinate(10, 50)
		c.set_values(5, y=99)
		"""
		# Assign from args list:
		field_names = self.field_names()
		if len(args) > len(field_names):
			raise ValueError("%r only has %d fields" % (
				type(self).__name__, len(field_names)))
		for i, value in enumerate(args):
			setattr(self, field_names[i], value)

		# Override with kwargs:
		for field, value in kwargs.items():
			if field not in field_names:
				raise ValueError("%r has no field %r" % (
					type(self).__name__, field))
			setattr(self, field, value)

	@classmethod
	def field_deh_name(cls, field):
		"""For the given C field name, get the dehacked name."""
		prop = getattr(cls, field)
		return prop.deh_name

	@classmethod
	def deh_field_name(cls, deh_name):
		"""For the given dehacked name, get the C field name."""
		for field in cls.field_names():
			if cls.field_deh_name(field) == deh_name:
				return field
		raise KeyError("%r has no field for name %r" % (
			type(self).__name__, deh_name))

	def __copy__(self):
		result = type(self)()
		result.copy_from(self)
		result.original = self.original
		return result

	def __repr__(self):
		return "%s(%s)" % (
			type(self).__name__,
			", ".join("%s=%r" % (f, getattr(self, f))
				for f in self.field_names()))

	def dehacked_header(self, array_index):
		return "%s %d" % (self.DEHACKED_NAME, array_index)

	def dehacked_output(self, fields=None, array_index=0):
		"""Get a description of this struct in dehacked form.

		If no field names are provided then all fields are
		included in the description.
		"""
		if fields is None:
			fields = self.field_names()
		results = []
		for field in fields:
			deh_name = self.field_deh_name(field)
			if deh_name:
				results.append("%s = %s" % (
					deh_name, getattr(self, field)))
		if not results:
			return ""

		return "\n".join([self.dehacked_header(array_index)] + results)

	def dehacked_diffs(self, other=None, array_index=0):
		"""Produce dehacked format diff against another struct.

		If no struct is provided then the original values used
		when instantiating this struct are used.

		Returned is a list containing either one string (dehacked-
		format list of changes) or no entries (no diff).
		"""
		diff = self.dehacked_output(fields=self.diff(other),
		                            array_index=array_index)
		if diff:
			return [diff]
		else:
			return []

	def diff(self, other=None):
		"""Compare this struct against another struct.

		If no other struct is provided the diff is performed
		against the original values from instantiation time. A
		list of differing field names is returned.
		"""
		other = other or self.original
		return [
			f for f in self.field_names()
			if getattr(self, f) != getattr(other, f)
		]

class StructArray(object):
	"""Class emulating a C fixed-length array.

	The elements in it must all be of type Struct and cannot
	be changed after instantiation time (although the structs within
	it can be changed).

	Arrays of this type must be provided a list of initializer elements
	on instantiation, and for convenience these can be of type list,
	tuple or dict to initialize structs, eg.

	  foo = c.StructArray(MyType, [
	      MyType(x=1, y=2),
	      (3, 4),
	      {'x': 5, 'y': 6},
	  ])
	"""

	def __init__(self, struct_type, elements, one_indexed=False):
		if not isinstance(struct_type(), Struct):
			raise ValueError("%r not a struct type" % (
				struct_type,))
		self._struct_type = struct_type
		self.one_indexed = one_indexed

		copied_elements = []
		for i, el in enumerate(elements):
			if isinstance(el, (list, tuple)):
				el = struct_type(*el)
			elif isinstance(el, dict):
				el = struct_type(**el)
			elif isinstance(el, struct_type):
				el = copy.copy(el)
			else:
				raise ValueError("%r not of type %r" % (
					el, struct_type))
			copied_elements.append(el)

		self._elements = tuple(copied_elements)

		# The 'original' pointer points back to the original array
		# that this instance was copy.copy()d from. By default, the
		# array points to itself as the original.
		self.original = self

	def __iter__(self):
		return iter(self._elements)
	def __len__(self):
		return len(self._elements)
	def __getitem__(self, i):
		return self._elements[i]
	def __getslice__(self, i, j):
		return self._elements[i:j]

	def copy_from(self, other):
		assert self._struct_type == other._struct_type, (
			"Arrays must be of the same type, %r != %r" % (
				self._struct_type, other._struct_type,
			))
		assert len(self) == len(other), (
			"Arrays must be equal length, %d != %d" % (
				len(self), len(other),
			))
		for i, obj in enumerate(self):
			obj.copy_from(other[i])

	def __copy__(self):
		result = type(self)(self._struct_type, self,
		                    one_indexed=self.one_indexed)
		result.original = self.original
		return result

	def __repr__(self):
		return "c.StructArray(%s, [\n%s\n])" % (
			self._struct_type.__name__,
			"\n".join("\t%r," % x for x in self),
		)

	def header_regexp(self):
		return self._struct_type().header_regexp()

	def parse_section(self, stream, index):
		index = int(index)
		if self.one_indexed:
			index -= 1
		if index < 0 or index >= len(self):
			stream.exception("assignment out of range: %d must be "
			                 "in range 0-%d" % (index, len(self)))
		self[index].parse_section(stream)

	def match_key(self):
		return (StructArray, self._struct_type)

	def dehacked_diffs(self, other=None):
		result = []
		for i, el in enumerate(self):
			if other is not None:
				other_el = other[i]
			else:
				other_el = None
			array_index = i
			if self.one_indexed:
				array_index += 1
			result.extend(el.dehacked_diffs(
				other_el, array_index=array_index))
		return result


class TestStruct(unittest.TestCase):
	class Coordinate(Struct):
		DEHACKED_NAME = "Co-ordinate"
		y = StructField("Y Value")
		x = StructField("X Value")

	def test_instantiate(self):
		# Different styles of instantiation:
		xy = TestStruct.Coordinate()
		self.assertEqual(xy.y, 0)
		self.assertEqual(xy.x, 0)

		xy = TestStruct.Coordinate(10)
		self.assertEqual(xy.y, 10)
		self.assertEqual(xy.x, 0)

		xy = TestStruct.Coordinate(10, 20)
		self.assertEqual(xy.y, 10)
		self.assertEqual(xy.x, 20)

		xy = TestStruct.Coordinate(x=123)
		self.assertEqual(xy.x, 123)
		self.assertEqual(xy.y, 0)

		xy = TestStruct.Coordinate(x=123, y=456)
		self.assertEqual(xy.x, 123)
		self.assertEqual(xy.y, 456)

		xy = TestStruct.Coordinate(123, x=456)
		self.assertEqual(xy.y, 123)
		self.assertEqual(xy.x, 456)

	def test_field_names(self):
		self.assertEqual(TestStruct.Coordinate.field_names(),
		                 ["y", "x"])
		xy = TestStruct.Coordinate()
		self.assertEqual(xy.field_names(), ["y", "x"])

	def test_copy_from(self):
		xy = TestStruct.Coordinate()
		self.assertEqual(xy.x, 0)
		self.assertEqual(xy.y, 0)

		xy2 = TestStruct.Coordinate(10, 20)
		xy.copy_from(xy2)
		self.assertEqual(xy.y, 10)
		self.assertEqual(xy.x, 20)

	def test_clone(self):
		xy = TestStruct.Coordinate(10, 20)
		xy2 = copy.copy(xy)
		# Ensure it really is a copy by trashing the original:
		xy.x = 99999
		xy.y = 123123
		self.assertEqual(xy2.y, 10)
		self.assertEqual(xy2.x, 20)
		self.assertEqual(xy2.original, xy)

	def test_dehacked_diffs(self):
		xy = TestStruct.Coordinate(10, 20)
		# After copying we compare against the original:
		xy2 = copy.copy(xy)
		xy2.x = 99
		xy2.y = 1000
		diffs = xy2.dehacked_diffs(array_index=123)
		self.assertEqual(diffs, ["Co-ordinate 123\n"
		                         "Y Value = 1000\n"
		                         "X Value = 99"])

		# Only print fields which have changed:
		xy2.y = 10
		diffs = xy2.dehacked_diffs(array_index=123)
		self.assertEqual(diffs, ["Co-ordinate 123\n"
		                         "X Value = 99"])

		# We can compare against a different base:
		xy3 = TestStruct.Coordinate(1000, 99)
		diffs = xy2.dehacked_diffs(other=xy3, array_index=123)
		self.assertEqual(diffs, ["Co-ordinate 123\n"
		                         "Y Value = 10"])

class TestStructArray(unittest.TestCase):
	def test_init(self):
		arr = StructArray(TestStruct.Coordinate, [
			(10,),
			(30,),
		])
		self.assertEqual(len(arr), 2)
		self.assertEqual(arr[0].y, 10)
		self.assertEqual(arr[0].x, 0)
		self.assertEqual(arr[1].y, 30)
		self.assertEqual(arr[1].x, 0)

		arr = StructArray(TestStruct.Coordinate, [
			{"y": 10},
			{"x": 40},
		])
		self.assertEqual(len(arr), 2)
		self.assertEqual(arr[0].y, 10)
		self.assertEqual(arr[0].x, 0)
		self.assertEqual(arr[1].y, 0)
		self.assertEqual(arr[1].x, 40)

		arr = StructArray(TestStruct.Coordinate, [
			TestStruct.Coordinate(x=20, y=10),
			TestStruct.Coordinate(x=40, y=30),
		])
		self.assertEqual(len(arr), 2)
		self.assertEqual(arr[0].y, 10)
		self.assertEqual(arr[0].x, 20)
		self.assertEqual(arr[1].y, 30)
		self.assertEqual(arr[1].x, 40)

	def test_copy_from(self):
		arr = StructArray(TestStruct.Coordinate, [
			(),
			(),
		])
		arr2 = StructArray(TestStruct.Coordinate, [
			(10, 20),
			(30, 40),
		])
		arr.copy_from(arr2)
		self.assertEqual(arr[0].y, 10)
		self.assertEqual(arr[0].x, 20)
		self.assertEqual(arr[1].y, 30)
		self.assertEqual(arr[1].x, 40)

	def test_clone(self):
		arr = StructArray(TestStruct.Coordinate, [
			(10, 20),
			(30, 40),
		])
		arr2 = copy.copy(arr)
		# Trash the original array to ensure it's really a copy:
		arr[0].x = 0; arr[0].y = 0
		arr[1].x = 0; arr[1].y = 0

		self.assertEqual(arr2[0].y, 10)
		self.assertEqual(arr2[0].x, 20)
		self.assertEqual(arr2[1].y, 30)
		self.assertEqual(arr2[1].x, 40)

	def test_dehacked_diffs(self):
		arr = StructArray(TestStruct.Coordinate, [
			(10, 20),
			(30, 40),
		])
		arr2 = copy.copy(arr)
		arr2[0].x = 999
		arr2[1].y = 1234
		self.assertEqual(arr2.dehacked_diffs(), [
			'Co-ordinate 0\nX Value = 999',
			'Co-ordinate 1\nY Value = 1234',
		])

		# We can diff against a different array than the original, if
		# requested.
		arr3 = StructArray(TestStruct.Coordinate, [
			(50, 999),
			(1234, 65),
		])
		self.assertEqual(arr2.dehacked_diffs(other=arr3), [
			'Co-ordinate 0\nY Value = 10',
			'Co-ordinate 1\nX Value = 40',
		])


if __name__ == '__main__':
	unittest.main()
