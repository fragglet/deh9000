
import strings

class StringReplacements(object):
	"""Class that wraps the functionality of dehacked string replacements.

	Objects of this class behave very similar in API to a dict (all the
	common methods are implemented), except two types of functionality
	are provided.

	Firstly it's possible to do a simple string replacement by setting the
	old and new string. For example:

	  s["Picked up a red skull key."] = "Picked up a pink skull key."

	This is equivalent to:

	  s[strings.GOTREDSKULL] = "Picked up a pink skull key."

	However, it's often tedious to have to specify the whole original
	string like this. So for convenience, it's also possible to do string
	replacements for "standard" strings (those found in strings.py /
	d_englsh.h in the Doom source) just by setting a property:

	  s.GOTREDSKULL = "Picked up a pink skull key."
	"""
	def __init__(self, module=None, base_module=strings):
		self._extras = {}
		# Build a reverse mapping from original string back
		# to property name.
		self._properties = set()
		self._reverse_map = {}
		for propname in dir(base_module):
			value = getattr(base_module, propname)
			if isinstance(value, str):
				self._reverse_map[value] = propname
				self._properties.add(propname)
		# Load strings from base_module (strings.py) and then
		# (optionally) overwrite with strings from a modified version
		# if one has been provided.
		self.load_from_module(base_module)
		if module is not None:
			self.load_from_module(module)

	def load_from_module(self, module):
		"""Load strings from the given module.

		It is assumed that the given module is a modified version of
		the strings.py module.
		"""
		# We only overwrite properties that were originally defined
		# in base_module at instantiation time; others are
		# ignored.
		for propname in set(dir(module)) & self._properties:
			value = getattr(module, propname)
			if isinstance(value, str):
				setattr(self, propname, value)

	def __contains__(self, s):
		return s in self._reverse_map or s in self._extras

	def __getitem__(self, s):
		# Options here are:
		# * The string may be a property (ie. standard string of
		#   the type in d_englsh.h). Use the reverse mapping to
		#   find if this is the case, and if so get its value.
		# * May be a non-standard string, like an error message,
		#   that the user set a replacement on. Look up in the
		#   extras map.
		# * If the string hasn't been replaced by the user at all,
		#   just return the same string.
		if s in self._reverse_map:
			propname = self._reverse_map[s]
			return getattr(self, propname)
		else:
			return self._extras.get(s, s)

	def get(self, s):
		return self[s]

	def __setitem__(self, s, replacement):
		# If this is a standard string stored as a property then
		# use the reverse map to look up the property name and
		# overwrite it. Otherwise store in extras map.
		if s in self._reverse_map:
			propname = self._reverse_map[s]
			setattr(self, propname, replacement)
		else:
			self._extras[s] = replacement

	def __len__(self):
		return len(self._reverse_map) + len(self._extras)

	def __iter__(self):
		for s in self._reverse_map:
			yield s
		for s in self._extras:
			yield s

	def iteritems(self):
		for key in self:
			yield key, self[key]
	def iterkeys(self):
		return iter(self)
	def itervalues(self):
		for key in self:
			yield self[key]

	def items(self):
		return list(self.iteritems())
	def keys(self):
		return list(self.iterkeys())
	def values(self):
		return list(self.itervalues())

	def match_key(self):
		return (StringReplacements,)

	def dehacked_diffs(self, other=None):
		other = other or {}
		result = []
		for old, new in self.iteritems():
			# Both have the exact same replacement? No need
			# to repeat it.
			if other.get(old, old) == new:
				continue
			header = "Text %d %d\n" % (len(old), len(new))
			result.append(header + old + new)

		return result


if __name__ == '__main__':
	s = StringReplacements()
	s["hello world"] = "goodbye world"
	s.HUSTR_E1M1 = "E1M1: Another boring level"
	print s[strings.HUSTR_E1M1]

	print s.dehacked_diffs()

