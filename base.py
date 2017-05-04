
import copy

class Enum(list):
	"""Wrapper around list that represents a C enum type."""
	def __init__(self, values):
		super(Enum, self).__init__(values)

	def create_globals(self, globals):
		"""Create constants in the given global dict."""
		for index, name in enumerate(self):
			globals[name] = index

class CStructBase(object):
	"""Base class for a type that emulate a C struct.

	This is similar to a collections.namedtuple except mutable and
	tailored specifically to the dehacked use case. The original
	values are saved so that they can be diffed against later if
	they are changed, and we support dual C / dehacked names for
	fields.

	Also unlike named tuples, objects of this type can be
	initialized automatically like how C structs can be - not all
	fields need to be provided. Unspecified fields default to zero.
	"""
	def __init__(self, *args, **kwargs):
		# Fill in unspecified fields with 0, as C does:
		for i in range(len(args), len(self._field_names)):
			field = self._field_names[i]
			setattr(self, field, 0)

		self.set_values(*args, **kwargs)

		# Save a copy of the original values so that we can diff
		# later, if we want to.
		self._original_values = copy.deepcopy((args, kwargs))

	def set_values(self, *args, **kwargs):
		"""Set the values of all fields in the struct.

		This is the same as what happens at instantiation time,
		but can be used to overwrite many fields all at once.
		For example:

		c = Coordinate(10, 50)
		c.set_values(5, y=99)
		"""
		# Assign from args list:
		if len(args) > len(self._field_names):
			raise ValueError("%r only has %d fields" % (
				self._type_name, len(self._field_names)))
		for i, value in enumerate(args):
			field = self._field_names[i]
			setattr(self, field, value)

		# Override with kwargs:
		for field, value in kwargs.items():
			if field not in self._field_names:
				raise ValueError("%r has no field %r" % (
					self._type_name, field))
			setattr(self, field, value)

	@classmethod
	def fields(cls):
		"""Get a list of the C field names for this class."""
		return list(cls._field_names)

	@classmethod
	def field_deh_name(cls, field):
		"""For the given C field name, get the dehacked name."""
		return cls._field_deh_map[field]

	def original(self):
		"""Returns an object of the same type with the original values.

		The values set at instantiation time are saved and can
		be recalled later via this method, which is useful for
		eg. diffing.
		"""
		args, kwargs = self._original_values
		return type(self)(*args, **kwargs)

	def __str__(self):
		return "%s(%s)" % (
			self._type_name,
			", ".join("%s=%r" % (f, getattr(self, f))
				for f in self._field_names))

	def dehacked_output(self, fields=None):
		"""Get a description of this struct in dehacked form.

		If no field names are provided then all fields are
		included in the description.
		"""
		if fields is None:
			fields = self._field_names
		result = ""
		for field in fields:
			result += "%s = %s\n" % (
				self.field_deh_name(field),
				getattr(self, field))
		return result

	def dehacked_diff(self, other=None):
		"""Produce dehacked format diff against another struct.

		If no struct is provided then the original values used
		when instantiating this struct are used.
		"""
		return self.dehacked_output(self.diff(other))

	def diff(self, other=None):
		"""Compare this struct against another struct.

		If no other struct is provided the diff is performed
		against the original values from instantiation time. A
		list of differing field names is returned.
		"""
		if other is None:
			other = self.original()
		return [
			f for f in self._field_names
			if getattr(self, f) != getattr(other, f)
		]

def CStruct(typename, fields):
	"""Create a C-style struct type for representing dehacked values.

	Args:
	  typename: Name of the struct type.
	  fields: List of tuples containing:
	    C (and Python) field name
	    Dehacked name for the field
	"""
	class Result(CStructBase):
		_type_name = typename
		_field_deh_map = dict(fields)
		_field_names = [x for x, _ in fields]

	return Result

if __name__ == '__main__':
	Coordinate = CStruct("Coordinate", [
		("x", "X Value"),
		("y", "Y Value"),
	])

	c = Coordinate(3, 4)
	c.y = 99
	print c
	print c.dehacked_diff()

