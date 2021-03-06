"""Class that represents an entire Dehacked file."""

from __future__ import absolute_import
from __future__ import print_function

import copy
import os
import tempfile
import unittest

from deh9000 import c
from deh9000 import deh_parser
from deh9000 import interactive
from deh9000 import reclaim
from deh9000 import states_parser
from deh9000 import tables

from deh9000.actions import A_FireCGun, A_FirePlasma
from deh9000.ammo import am_noammo
from deh9000.mobjs import mobjinfo_t
from deh9000.sprites import spritenum_t
from deh9000.states import *
from deh9000.states_array import CodePointers, StatesArray
from deh9000.string_repls import StringReplacements
from deh9000.weapons import weaponinfo_t, wp_pistol


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
		self.sprnames = self.strings.sprnames

		# Set a couple of hooks in the states array which make the API
		# for DECORATE-format parsing a bit nicer.
		self.states.get_alloc_states = self.free_states
		self.states.assign_sprites = self.assign_sprites

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
		return c.EnumSet(statenum_t, result)

	def weapon_states(self, weapon_id):
		"""Returns a set of all states used by the given weapon."""
		states = self.states
		weaponinfo = self.weaponinfo
		weapon = weaponinfo[weapon_id]
		result = set()
		for field in weaponinfo_t.state_fields:
			state_id = getattr(weapon, field)
			result |= set(states.walk(state_id))
		return c.EnumSet(statenum_t, result)

	def _run_reclaim(self, callback, strategies, avoid_strategies):
		last_strategy = "(start)"
		for strategy in strategies:
			if callback(last_strategy):
				return True
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
			last_strategy = "%s(%s)" % (func, args)

		# Ran out of strategies; did we achieve the goal?
		return callback(last_strategy)

	def reclaim_states(self, count, strategies=reclaim.strategies,
	                   avoid_strategies=(), debug=False):
		"""Tries to reclaim the given number of states.

		This is achieved using reclaim strategies found in reclaim.py
		to modify the mobjinfo and state tables in subtle ways. The
		more states requested, the more invasive the changes become.
		"""
		def reclaim_callback(last_strategy):
			states = self.free_states()
			if debug:
				print("After %s, %d states free" % (
					last_strategy,
					len(states)))
			return len(states) >= count

		if not self._run_reclaim(reclaim_callback,
		                         strategies, avoid_strategies):
			raise OverflowError(
				"Couldn't reclaim %d states." % count)

		return self.free_states()

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
		for weapon_id, weapon in enumerate(self.weaponinfo):
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
		return c.EnumSet(statenum_t, allstates.difference(marked))

	def free_sprites(self):
		"""Returns a set of indexes of unused sprites."""
		# Iterate over all non-free states and mark sprite numbers.
		free_states = self.free_states()
		used_sprites = set()
		for state_id, state in enumerate(self.states):
			if state_id not in free_states:
				used_sprites.add(state.sprite)
		# Make a set of all sprite numbers. What's not marked?
		allsprites = set(range(len(spritenum_t)))
		return c.EnumSet(spritenum_t,
		                 allsprites.difference(used_sprites))

	def reclaim_sprites(self, count, strategies=reclaim.strategies,
	                    avoid_strategies=(), debug=False):
		"""Tries to reclaim sprite numbers.

		This function uses the same reclaim strategies used by the
		reclaim_states method, but attempts to acquire sprite numbers
		(indexes into sprnames[]) instead.
		"""
		# Generator function that runs over all the provided strategies
		# and yields only those strategies which produce an increase in
		# the number of sprites. This is achieved by operating on a
		# separate "clean" DehackedFile instance.
		def sprite_strategies():
			f = DehackedFile()
			free_sprites = f.free_sprites()
			for strategy in strategies:
				f._run_reclaim(lambda _: False, [strategy], [])
				new_free_sprites = f.free_sprites()
				if len(new_free_sprites) > len(free_sprites):
					yield strategy
				free_sprites = new_free_sprites

		def reclaim_callback(last_strategy):
			sprites = self.free_sprites()
			if debug:
				print("After %s, %d sprites free" % (
					last_strategy,
					len(sprites)))
			return len(sprites) >= count

		# Run reclaim. The generator object returned by the
		# sprite_strategies() function above produces the sequence of
		# strategies to try.
		if not self._run_reclaim(reclaim_callback, sprite_strategies(),
		                         avoid_strategies):
			raise OverflowError(
				"Couldn't reclaim %d sprites." % count)

		return self.free_sprites()

	def assign_sprites(self, spritenames):
		"""Ensure that the given sprite names are in sprnames.

		If the sprite names are not in sprnames, they are set there
		by calling reclaim_sprites() to find unused sprites.
		Returns a list of sprite indexes corresponding to the list of
		names requested.
		"""
		spritenames = [s.upper() for s in spritenames]
		free_sprite_ids = self.free_sprites()
		# There is a subset of free_sprite_ids we can use, because
		# there is a corner case where a sprite is free but also in
		# the spritenames list we're trying to assign.
		have_ids = {spr_id for spr_id in free_sprite_ids
		            if self.sprnames[spr_id] not in spritenames}
		need = {name for name in spritenames
		        if name not in self.sprnames}
		if len(need) > len(have_ids):
			raise OverflowError(
				"Can't assign %d more sprites: only "
				"%d sprites are available." % (
					len(need), len(have_ids)))
		# We have enough sprites to assign all those in 'need'. So
		# go through the list and do so.
		for name in need:
			spr_id = have_ids.pop()
			self.sprnames[spr_id] = name
		return [self.sprnames.index(name) for name in spritenames]

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
		"""Save the Dehacked file to the given filename."""
		result_text = "\n\n".join(self.dehacked_diffs())
		with open(filename, "w") as f:
			f.write(result_text)

	def load(self, filename, strict_mode=False):
		"""Load a Dehacked file from the given filename."""
		deh_parser.parse_dehacked_file(filename, self.parts + [
			deh_parser.TopLevelProperty(
				"Doom version", self, "doom_version", int,
			),
			deh_parser.TopLevelProperty(
				"Patch format", self, "patch_format", int,
			),
		], strict_mode=strict_mode)

	def interactive(self, args=None, level=None):
		"""Start a source port testing this dehacked file.

		If invoked multiple times, the previously launched process is
		killed. Arguments are also saved so that they only need to be
		specified once; calling dehfile.interactive() relaunches the
		game with an updated dehacked patch and using the same
		arguments as before.
		"""
		interactive.start_interactive(self, args=args, level=level)


TEST_DEHACKED_FILE="""
Patch File for DeHackEd v3.0

# Note: Use the pound sign ('#') to start comment lines.

Doom version = 19
Patch format = 5

Ammo 0 (Bullets)
Max ammo = 400

Misc 0
Initial Health = 15

Thing 2 (Trooper)
Hit points = 200

Frame 14
Duration = 0
Next frame = 16

Sound 1
Value = 32

Weapon 1 (Pistol)
Ammo type = 5

Text 12 11
E1M1: HangarFirst level

Text 19 12
E1M2: Nuclear PlantSecond level
"""

class TestDehackedFile(unittest.TestCase):
	def test_save(self):
		dehfile = DehackedFile()
		dehfile.patch_format = 5
		dehfile.ammodata[0].maxammo *= 2
		dehfile.miscdata.initial_health = 15
		dehfile.mobjinfo[1].spawnhealth *= 10
		dehfile.states[S_PISTOL2].tics = 0
		dehfile.states[S_PISTOL2].nextstate = S_PISTOL4
		dehfile.strings["E1M1: Hangar"] = "First level"
		dehfile.strings.HUSTR_E1M2 = "Second level"
		dehfile.S_sfx[1].priority = 32
		dehfile.weaponinfo[wp_pistol].ammo = am_noammo
		path = os.path.join(tempfile.mkdtemp(), "test.deh")
		dehfile.save(path)

		with open(path) as f:
			contents = f.read()
			self.assertEqual(contents.strip(),
			                 TEST_DEHACKED_FILE.strip())

	def test_load(self):
		f = tempfile.NamedTemporaryFile(suffix=".deh", delete=False)
		f.write(TEST_DEHACKED_FILE.strip().encode('utf8'))
		f.close()

		dehfile = DehackedFile()
		dehfile.load(f.name)

		self.assertEqual(dehfile.patch_format, 5)
		self.assertEqual(dehfile.ammodata[0].maxammo, 400)
		self.assertEqual(dehfile.miscdata.initial_health, 15)
		self.assertEqual(dehfile.mobjinfo[1].spawnhealth, 200)
		self.assertEqual(dehfile.states[S_PISTOL2].tics, 0)
		self.assertEqual(dehfile.states[S_PISTOL2].nextstate,
		                 S_PISTOL4)
		self.assertEqual(dehfile.strings.HUSTR_E1M1, "First level")
		self.assertEqual(dehfile.strings["E1M1: Hangar"],
		                 "First level")
		self.assertEqual(dehfile.strings.HUSTR_E1M2, "Second level")
		self.assertEqual(dehfile.S_sfx[1].priority, 32)
		self.assertEqual(dehfile.weaponinfo[wp_pistol].ammo, am_noammo)

		os.unlink(f.name)

	def test_free_states(self):
		dehfile = DehackedFile()

		# These states are unused in Doom's states table:
		expected = {45, 892, 893, 46, 887}
		states = dehfile.free_states()
		self.assertEqual(set(states), expected)

		# Modifying monster states frees up more states:
		dehfile.states[S_POSS_DIE3].nextstate = S_POSS_DIE5
		expected.add(S_POSS_DIE4)
		states = dehfile.free_states()
		self.assertEqual(set(states), expected)

		# We can also modify gun states:
		dehfile.states[S_SGUN4].nextstate = S_SGUN6
		expected.add(S_SGUN5)
		states = dehfile.free_states()
		self.assertEqual(set(states), expected)

	def test_reclaim_states(self):
		dehfile = DehackedFile()
		states = dehfile.free_states()
		self.assertLess(len(states), 50)

		# Reclaim some states to use automatically.
		states = dehfile.reclaim_states(50)
		self.assertGreaterEqual(len(states), 50)

		# reclaim_states() result is practically the same as the
		# free_states() result.
		self.assertEqual(set(states), set(dehfile.free_states()))

	def test_reclaim_sprites(self):
		dehfile = DehackedFile()
		sprites = dehfile.free_sprites()
		self.assertLess(len(sprites), 10)

		# Reclaim some sprite numbers to use automatically.
		sprites = dehfile.reclaim_sprites(10)
		self.assertGreaterEqual(len(sprites), 10)

		# reclaim_sprites() result is practically the same as the
		# free_sprites() result.
		self.assertEqual(set(sprites), set(dehfile.free_sprites()))


if __name__ == "__main__":
	unittest.main()

