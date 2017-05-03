
import copy
import collections

class Enum(list):
	def __init__(self, values):
		super(Enum, self).__init__(values)

	def create_globals(self, globals):
		for index, name in enumerate(self):
			globals[name] = index

class CStructBase(object):
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
		return list(cls._field_names)

	@classmethod
	def field_deh_name(cls, field):
		return cls._field_deh_map[field]

	def original(self):
		args, kwargs = self._original_values
		return type(self)(*args, **kwargs)

	def __str__(self):
		return "%s(%s)" % (
			self._type_name,
			", ".join("%s=%r" % (f, getattr(self, f))
				for f in self._field_names))

	def dehacked_output(self, fields):
		result = ""
		for field in fields:
			result += "%s = %s\n" % (
				self.field_deh_name(field),
				getattr(self, field))
		return result

	def dehacked_diff(self, other=None):
		return self.dehacked_output(self.diff(other))

	def diff(self, other=None):
		if other is None:
			other = self.original()
		return [
			f for f in self._field_names
			if getattr(self, f) != getattr(other, f)
		]

def CStruct(typename, fields):
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

