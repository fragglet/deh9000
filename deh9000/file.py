"""Class that represents an entire Dehacked file."""

import copy

import c
import interactive
import reclaim
import states_parser
import tables

from actions import A_FireCGun, A_FirePlasma
from ammo import am_noammo
from mobjs import mobjinfo_t
from states import state_t, S_PISTOL2, S_PISTOL4
from states_array import CodePointers, StatesArray
from string_repls import StringReplacements
from weapons import weaponinfo_t, wp_pistol
from weapons import wp_pistol


DEHACKED_HEADER_FORMAT = """
Patch File for DeHackEd v3.0

# Note: Use the pound sign ('#') to start comment lines.

Doom version = %(doom_version)s
Patch format = %(patch_format)s

"""


class DehackedFile(object):
	"""Class that represents an entire dehacked file.

	Each instance of a DehackedFile has a complete copy of all the tables
	that can be modified in a dehacked file. These are named to match the
	Doom source code where appropriate:

	  ammodata:   Ammo table              (Dehacked's "Ammo" section)
	  miscdata:   Miscellaneous variables (Dehacked's "Misc" section)
	  mobjinfo:   Map objects table       (Dehacked's "Thing" section)
	  states:     Animations frames       (Dehacked's "Frame" section)
	  strings:    String replacements     (Dehacked's "Text" section)
	  S_sfx:      Sound FX table          (Dehacked's "Sound" section)
	  weaponinfo: Weapons table           (Dehacked's "Weapon" section)

	These can be accessed via properties on DehackedFile and changed, for
	example:

	  file = deh9000.DehackedFile()
	  file.strings.HUSTR_1 = "Level 1"
	  file.mobjinfo[deh9000.MT_POSSESSED].spawnhealth *= 2

	If it is more convenient, it is possible to make a modified version of
	tables.py and load values from it, eg.

	  import modified_tables
	  file = deh9000.DehackedFile()
	  file.load_from_module(modified_tables)

	"""
	TABLE_MODULE_VARS = ("ammodata", "miscdata", "mobjinfo", "states",
	                    "S_sfx", "weaponinfo")

	def __init__(self, module=None, base_module=tables):
		# Build up a list of "parts", by copying the tables from
		# tables.py to use as a base. We make copies of the tables so
		# that each DehackedFile has its own independently mutable
		# version.
		self.parts = []
		for name in DehackedFile.TABLE_MODULE_VARS:
			obj = copy.copy(getattr(base_module, name))
			self.parts.append(obj)
			setattr(self, name, obj)

		self.strings = StringReplacements()

		if module is not None:
			self.load_from_module(module)

		self.parts.append(CodePointers(self.states))
		self.parts.append(self.strings)

		self.doom_version = 19
		self.patch_format = 6

	def load_from_module(self, module):
		"""Load tables from the given module.

		It is assumed that the given module is a modified version of
		the tables.py module.
		"""
		for name in DehackedFile.TABLE_MODULE_VARS:
			part = getattr(self, name)
			table = getattr(module, name)
			part.copy_from(table)

	def dehacked_header(self):
		return DEHACKED_HEADER_FORMAT.strip() % {
			'doom_version': self.doom_version,
			'patch_format': self.patch_format,
		}

	def mobj_states(self, mobj_id):
		"""Returns a set of all states used by the given mobj."""
		states = self.states
		mobjinfo = self.mobjinfo
		mobj = mobjinfo[mobj_id]
		result = set()
		for field in mobjinfo_t.state_fields:
			state_id = getattr(mobj, field)
			result |= set(states.walk(state_id))
		return result

	def weapon_states(self, weapon_id):
		"""Returns a set of all states used by the given weapon."""
		states = self.states
		weaponinfo = self.weaponinfo
		weapon = weaponinfo[weapon_id]
		result = set()
		for field in weaponinfo_t.state_fields:
			state_id = getattr(weapon, field)
			result |= set(states.walk(state_id))
		return result

	def reclaim_states(self, count, strategies=reclaim.strategies,
	                   avoid_strategies=(), debug=False):
		"""Tries to reclaim the given number of states.

		This is achieved using reclaim strategies found in reclaim.py
		to modify the mobjinfo and state tables in subtle ways. The
		more states requested, the more invasive the changes become.
		"""
		for strategy in strategies:
			free_states = self.free_states()
			if len(free_states) >= count:
				return free_states
			# User can list strategies to avoid:
			if strategy in avoid_strategies:
				continue
			# Strategies in the list can be bare functions to
			# call, or a tuple of function and arguments.
			if isinstance(strategy, tuple):
				func, args = strategy[0], strategy[1:]
			else:
				func, args = strategy, []
			# Allow strategy to avoid specified as function:
			if func in avoid_strategies:
				continue
			func(self, *args)
			if debug:
				print "After %s(%s), %d states free" % (
					func, args, len(self.free_states()))
		else:
			raise OverflowError(
				"Couldn't reclaim %d states." % count)

	def free_states(self):
		"""Returns a set of the indexes of all unreferenced states."""
		marked = {0}
		states = self.states
		# Mark all chains beginning from the hard-coded states. These
		# are states which are referenced directly in the source code.
		for state_id in set(StatesArray.HARDCODED_STATES):
			marked |= set(states.walk(state_id))
		# Add all states used by mobjs (referenced from mobjinfo).
		for mobj_id in range(len(self.mobjinfo)):
			marked |= self.mobj_states(mobj_id)
		# Add all weapon states (referenced from weaponinfo).
		weaponinfo = self.weaponinfo
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

	def save(self, filename):
		result_text = "\n\n".join(self.dehacked_diffs())
		with open(filename, "w") as f:
			f.write(result_text)

	def _parse_line(self, headers, stream, line):
		for regex, part in headers:
			m = regex.match(line)
			if m:
				params = m.groupdict()
				part.parse_section(stream, **params)
				break
		else:
			# TODO: Handle these unknown lines properly
			print "Unknown line: %s" % line

	def load(self, filename):
		headers = [(p.header_regexp(), p) for p in self.parts]
		with open(filename, "r") as f:
			while True:
				line = f.readline()
				if line == "":
					break
				self._parse_line(headers, f, line)

	def interactive(self, level=None, args=()):
		interactive.start_interactive(self, level=level, args=args)


if __name__ == "__main__":
	f = DehackedFile()
	f.ammodata[0].maxammo *= 2
	f.miscdata.initial_health = 15
	f.mobjinfo[1].spawnhealth *= 10
	f.states[S_PISTOL2].tics = 0
	f.states[S_PISTOL2].nextstate = S_PISTOL4
	f.strings.HUSTR_E1M1 = "First level"
	f.S_sfx[1].priority = 32
	f.weaponinfo[wp_pistol].ammo = am_noammo
	f.save("test.deh")

