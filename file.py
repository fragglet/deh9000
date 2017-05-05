
import strings

DEHACKED_HEADER_FORMAT = """
Patch File for DeHackEd v3.0

# Note: Use the pound sign ('#') to start comment lines.

Doom version = %(doom_version)s
Patch format = %(patch_format)s

"""

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
	def __init__(self, strings_module=strings):
		self._extras = {}

		# Copy all string properties from the strings module to
		# be properties of this object. But we also store a
		# reverse mapping of string back to property name.
		self._reverse_map = {}
		for propname in dir(strings_module):
			value = getattr(strings_module, propname)
			if not isinstance(value, str):
				continue
			setattr(self, propname, value)
			self._reverse_map[value] = propname

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

	def dehacked_diff(self, other=None):
		other = other or {}
		result = []
		for old, new in self.iteritems():
			# Both have the exact same replacement? No need
			# to repeat it.
			if other.get(old, old) == new:
				continue
			header = "Text %d %d\n" % (len(old), len(new))
			result.append(header + old + new)

		return "\n\n".join(result)

class DehackedFile(object):
	def __init__(self, *parts):
		self.parts = parts
		self.doom_version = 19
		self.patch_format = 6

	def dehacked_header(self):
		return DEHACKED_HEADER_FORMAT % {
			'doom_version': self.doom_version,
			'patch_format': self.patch_format,
		}

	def dehacked_diff(self, other=None):
		result = []
		# If there's no diff then we compare against original values,
		# but if we're comparing against another file then we need to
		# match up parts and compare them.
		if other is None:
			for s in self.parts:
				diff = s.dehacked_diff()
				if diff:
					result.append(diff)
		else:
			parts_keyed = {p.match_key(): p for p in self.parts}
			other_parts = {p.match_key(): p for p in self.parts}
			assert parts_keyed.keys() == other_parts.keys(), (
				"Parts for files should match: %r != %r" % (
					parts_keyed.keys(), other_parts.keys(),
				))
			for key, part in parts_keyed.items():
				other_part = other_parts[key]
				diff = part.dehacked_diff(other=other_part)
				if diff:
					result.append(diff)
		if not result:
			result.append("# No difference was found!")
		return self.dehacked_header() + "\n\n".join(result)

	def write(self, filename):
		with open(filename, "w") as f:
			f.write(self.dehacked_diff())

if __name__ == '__main__':
	s = StringReplacements()
	s["hello world"] = "goodbye world"
	s.HUSTR_E1M1 = "E1M1: Another boring level"
	print s[strings.HUSTR_E1M1]

	print s.dehacked_diff()

