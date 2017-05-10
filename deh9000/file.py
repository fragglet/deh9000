
import c
import strings
from actions import A_FireCGun, A_FirePlasma
from mobjs import mobjinfo_t
from states import state_t
from weapons import weaponinfo_t

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
	def __init__(self, strings_module=None, base_strings_module=strings):
		self._extras = {}
		# Build a reverse mapping from original string back
		# to property name.
		self._properties = set()
		self._reverse_map = {}
		for propname in dir(base_strings_module):
			value = getattr(base_strings_module, propname)
			if isinstance(value, str):
				self._reverse_map[value] = propname
				self._properties.add(propname)
		# Load strings from base_strings_module (strings.py) and then
		# (optionally) overwrite with strings from a modified version
		# if one has been provided.
		self.load_from_module(base_strings_module)
		if strings_module is not None:
			self.load_from_module(strings_module)

	def load_from_module(self, strings_module):
		"""Load strings from the given module.

		It is assumed that the given module is a modified version of
		the strings.py module.
		"""
		# We only overwrite properties that were originally defined
		# in base_strings_module at instantiation time; others are
		# ignored.
		for propname in set(dir(strings_module)) & self._properties:
			value = getattr(strings_module, propname)
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

class DehackedFile(object):
	def __init__(self, *parts):
		self.parts = parts
		self.doom_version = 19
		self.patch_format = 6

	def dehacked_header(self):
		return DEHACKED_HEADER_FORMAT.strip() % {
			'doom_version': self.doom_version,
			'patch_format': self.patch_format,
		}

	def array_for_type(self, t):
		for part in self.parts:
			if (isinstance(part, c.StructArray)
			    and isinstance(part[0], t)):
				return part
		raise LookupError("StructArray with type %r not found" % (t,))

	def mobj_states(self, mobj_id):
		"""Returns a set of all states used by the given mobj."""
		states = self.array_for_type(state_t)
		mobjinfo = self.array_for_type(mobjinfo_t)
		mobj = mobjinfo[mobj_id]
		result = set()
		for field in mobjinfo_t.state_fields:
			state_id = getattr(mobj, field)
			result |= set(states.walk(state_id))
		return result

	def weapon_states(self, weapon_id):
		"""Returns a set of all states used by the given weapon."""
		states = self.array_for_type(state_t)
		weaponinfo = self.array_for_type(weaponinfo_t)
		weapon = weaponinfo[weapon_id]
		result = set()
		for field in weaponinfo_t.state_fields:
			state_id = getattr(weapon, field)
			result |= set(states.walk(state_id))
		return result

	def free_states(self):
		"""Returns a set of the indexes of all unreferenced states."""
		marked = {0}
		states = self.array_for_type(state_t)
		# Mark all chains beginning from the hard-coded states. These
		# are states which are referenced directly in the source code.
		for state_id in set(state_t.hardcoded_states):
			marked |= set(states.walk(state_id))
		# Add all states used by mobjs (referenced from mobjinfo).
		for mobj_id in range(len(self.array_for_type(mobjinfo_t))):
			marked |= self.mobj_states(mobj_id)
		# Add all weapon states (referenced from weaponinfo).
		weaponinfo = self.array_for_type(weaponinfo_t)
		for weapon_id, weapon in enumerate(weaponinfo):
			weaponstates = self.weapon_states(weapon_id)
			marked |= weaponstates
			# There is a special case - if any of the states used
			# by this weapon invoke A_FirePlasma or A_FireCGun,
			# they can jump to weapon.flashstate+1, so we must mark
			# this state any others that follow it.
			actions = {states[sid].action for sid in weaponstates}
			if A_FirePlasma in actions or A_FireCGun in actions:
				second_state_id = weapon.flashstate + 1
				marked |= set(states.walk(second_state_id))
		# Make a set with all state numbers. What's not marked?
		allstates = set(range(len(states)))
		return allstates.difference(marked)

	def dehacked_diffs(self, other=None):
		result = []
		# If there's no diff then we compare against original values,
		# but if we're comparing against another file then we need to
		# match up parts and compare them.
		if other is None:
			for s in self.parts:
				result.extend(s.dehacked_diffs())
		else:
			parts_keyed = {p.match_key(): p for p in self.parts}
			other_parts = {p.match_key(): p for p in self.parts}
			assert parts_keyed.keys() == other_parts.keys(), (
				"Parts for files should match: %r != %r" % (
					parts_keyed.keys(), other_parts.keys(),
				))
			for key, part in parts_keyed.items():
				other_part = other_parts[key]
				result.extend(part.dehacked_diffs(
					other=other_part))
		if not result:
			result.append("# No difference was found!")
		return [self.dehacked_header()] + result

	def write(self, filename):
		result_text = "\n\n".join(self.dehacked_diffs())
		with open(filename, "w") as f:
			f.write(result_text)

if __name__ == '__main__':
	s = StringReplacements()
	s["hello world"] = "goodbye world"
	s.HUSTR_E1M1 = "E1M1: Another boring level"
	print s[strings.HUSTR_E1M1]

	print s.dehacked_diffs()

