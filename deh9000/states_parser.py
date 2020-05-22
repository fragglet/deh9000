"""Parser for DECORATE-style States {} definitions.

The DECORATE syntax for defining states makes for a very clean way of defining
actor states and animations. In particular it's probably convenient for
converting such animations from DECORATE format to Dehacked.

Basic syntax looks like:

  # This is a comment.
  BOSF A 3 BRIGHT A_SpawnSound

These are, in order:
 * Sprite name (must be one of the Vanilla Doom sprite names (unlike DECORATE,
   new sprite names are not possible). See sprites.py.
 * Frame number as alphabet character (A-Z); this matches the WAD lump names.
 * Number of tics for this frame of animation to be shown (-1 = forever)
 * [optional] "BRIGHT" to always show the sprite at full brightness.
 * [optional] Action pointer name; see actions.py.

Multiple frames can be specified at once, for example this:

  BOSF BCD 3 BRIGHT A_SpawnFly

is equivalent to this:

  BOSF B 3 BRIGHT A_SpawnFly  # This is tedious ...
  BOSF C 3 BRIGHT A_SpawnFly
  BOSF D 3 BRIGHT A_SpawnFly

It is possible to attach labels to frames and use "Goto" to jump to them; the
"+" syntax allows jumping ahead in a sequence. For example:

  Tweedledum:
    TROO M 4
    TROO O 5 A_XScream
    TROO P 5
    Goto Tweedledee
  See:
  Tweedledee:
    TROO N 5
    Goto Tweedledum+1  # Jump to the A_XScream state

Unlike in DECORATE it isn't possible to jump to a label in another monster's
sequence, outside of the string being parsed. But Goto statements can jump to
specific entries in the states[] table. For example:

    TROO P 5
    Goto 123
  Tweedledee:
    TROO N 5
    Goto S_CYBER_RUN3

The "Loop" statement jumps back to the last label that was defined, eg.

  See:
    TROO OP 5
    Loop       # Keep on showing these two frames.

While the "Stop" statement jumps to the null state (S_NULL). This causes the
object to be deleted in-game:

  See:
    TROO A 35
    Stop       # We just show one frame for a second and disappear.

All sequences must end in a Goto, Loop or Stop statement.

Finally, it is sometimes important when dehacking for Vanilla Doom to use a
specific state ID that is hard-coded into the Doom source code. This can be
achieved using Pin() labels, for example:

  Pin(S_BRAINEXPLODE1):  # A_BrainScream uses this state!
    TROO N 5
  Pin(456):
    TROO P 5

When remapping it is important that any pinned states are included in the
alloc_states collection provided, otherwise it is not possible to apply the
pins.
"""

from __future__ import absolute_import
from __future__ import print_function

import copy
import re
import unittest

from deh9000 import c
from deh9000 import actions
from deh9000 import strings
from deh9000.actions import *
from deh9000.sprites import *
from deh9000.states import state_t, statenum_t, S_BFGEXP

# eg. "Spawn:"
GOTO_LABEL_RE = re.compile(r"\s*(?P<label>\w+)\s*:\s*")

# eg. "Pin(123):"
PIN_STATE_RE = re.compile(r"\s*Pin\s*"
                          r"\(\s*(?P<statenum>\w+)\s*\)"
                          r"\s*:\s*", re.I)

# Examples:
# BSPI A 20
# BSPI A 3 A_BabyMetal
# BOSF A 3 BRIGHT A_SpawnSound
# APLS AB 5 BRIGHT
# BOSF BCD 3 BRIGHT A_SpawnFly

FRAME_DEF_RE = re.compile(r"\s*(?P<sprname>\w\w\w\w)"
                          r"\s+(?P<frame>[a-z\[\\\]]+)"
                          r"\s+(?P<tics>\-?\d+)"
                          r"\s*(?P<bright>bright)?"
                          r"\s*(?P<action>A_\w+)?"
                          r"\s*$", re.I)

# Examples:
# Goto See
# Goto Spawn+1
GOTO_STATEMENT_RE = re.compile(r"\s*Goto"
                               r"\s+(?P<label>\w+)"
                               r"\s*(\+\s*(?P<offset>\d+))?"
                               r"\s*$", re.I)

# Jump back to last labeled state:
LOOP_STATEMENT_RE = re.compile(r"\s*Loop\s*$", re.I)

# End of sequence
STOP_STATEMENT_RE = re.compile(r"\s*Stop\s*$", re.I)

# Comments:
COMMENT_RE = re.compile(r"#.*")

# What the *state fields are called in DECORATE:
DECORATE_NAMES = {
	# mobj_t fields:
	"see":     "seestate",
	"spawn":   "spawnstate",
	"pain":    "painstate",
	"melee":   "meleestate",
	"missile": "missilestate",
	"death":   "deathstate",
	"xdeath":  "xdeathstate",
	"raise":   "raisestate",

	# weaponinfo_t fields:
	"select":   "upstate",
	"deselect": "downstate",
	"ready":    "readystate",
	"fire":     "atkstate",
	"flash":    "flashstate",
}

class StatesParseException(Exception):
	pass

class StateRemapException(Exception):
	pass


def action_pointer_for_name(name):
	if not name:
		return None
	if (not hasattr(actions, name) or
	    not isinstance(getattr(actions, name), actions.Action)):
		raise StatesParseException("Unknown action pointer %r" % name)
	return getattr(actions, name)


class _Parser(object):
	def __init__(self):
		self.sprnames = []
		self.states = [state_t(action=None)]
		self.state_labels = {}
		self.previous_state_id = -1
		self.loop_start_id = -1
		self.saved_gotos = []

	def more_lines(self):
		while self.lines and self.lines[0].strip() == "":
			self.line_number += 1
			self.lines.pop(0)
		return len(self.lines) > 0

	def next_line(self):
		if not self.more_lines():
			return ""
		#print("next line: %r" % self.lines[0])
		return self.lines[0]

	def matches_regexp(self, regexp):
		line = self.next_line()
		m = regexp.match(line)
		if m:
			#print("%r matches %r" % (line, regexp))
			self.lines[0] = line[m.end():]
			return m

	def parse_labels(self):
		labels = set()
		while True:
			m = self.matches_regexp(GOTO_LABEL_RE)
			if not m:
				break
			labels.add(m.groupdict()["label"])
		return labels

	def parse_pin(self):
		m = self.matches_regexp(PIN_STATE_RE)
		if not m:
			return None
		statenum = m.groupdict()["statenum"]
		result = self.parse_state_number(statenum)
		if result is None:
			self.exception("State ID %r for pin() unknown." % (
				statenum))
		return result

	def exception(self, s, line_number=None):
		if line_number is None:
			line_number = self.line_number
		raise StatesParseException("line %d: %s" % (line_number, s))

	def set_label(self, name, state_id):
		if name in self.state_labels:
			self.exception("Label %r defined multiple times." % (
				name))
		self.state_labels[name] = state_id
		# We also set loop_start_id so we know which is the last
		# label defined before a loop statement.
		self.loop_start_id = state_id

		# Also see if there's a Doom equivalent name:
		doom_name = DECORATE_NAMES.get(name.lower())
		if doom_name and doom_name not in self.state_labels:
			self.state_labels[doom_name] = state_id

	def alloc_new_state(self):
		result = len(self.states)
		self.states.append(state_t())
		return result

	def sprite_for_name(self, name):
		name = name.upper()
		try:
			return self.sprnames.index(name)
		except ValueError:
			self.sprnames.append(name)
			return len(self.sprnames) - 1

	def construct_states(self, params):
		sprite_num = self.sprite_for_name(params["sprname"])
		tics = int(params["tics"])
		is_bright = params.get("bright") != None
		action = action_pointer_for_name(params.get("action"))

		for fr in params["frame"]:
			frame = ord(fr.upper()) - ord('A')
			if is_bright:
				frame |= 32768
			yield state_t(
				sprite=sprite_num,
				frame=frame,
				tics=tics,
				action=action,
			)

	def parse_frame_def(self):
		labels = self.parse_labels()
		pin_id = self.parse_pin()
		m = self.matches_regexp(FRAME_DEF_RE)
		if not m:
			return False
		for state in self.construct_states(m.groupdict()):
			state_id = self.alloc_new_state()
			self.states[state_id].copy_from(state)

			# Link in states in a chain:
			if self.previous_state_id != -1:
				previous_state = (
					self.states[self.previous_state_id])
				previous_state.nextstate = state_id
			self.previous_state_id = state_id

			# If there were labels for this sequence, they should
			# be stored and pointed to the first stated in seq:
			for label in labels:
				self.set_label(label, state_id)
			if pin_id is not None:
				self.states[state_id].pin_state_id = pin_id
			# Only the first in sequence:
			labels = set()
			pin_id = None
		return True

	def parse_loop(self):
		if not self.matches_regexp(LOOP_STATEMENT_RE):
			return False

		if self.previous_state_id == -1:
			self.exception("Loop without a preceding state")
		if self.loop_start_id == -1:
			self.exception("Loop without a preceding label")
		state = self.states[self.previous_state_id]
		state.nextstate = self.loop_start_id
		self.previous_state_id = -1
		self.loop_start_id = -1
		return True

	def parse_stop(self):
		if not self.matches_regexp(STOP_STATEMENT_RE):
			return False

		if self.previous_state_id == -1:
			self.exception("Stop without a preceding state")
		state = self.states[self.previous_state_id]
		state.tics = -1
		state.nextstate = 0
		self.previous_state_id = -1
		self.loop_start_id = -1
		return True

	def parse_state_number(self, s):
		"""Returns state number if 's' describes a specific state."""
		try:
			return statenum_t.index(s)
		except ValueError:
			pass
		try:
			state_id = int(s)
			if 0 <= state_id < len(statenum_t):
				return state_id
		except ValueError:
			pass
		return None

	def parse_goto(self):
		m = self.matches_regexp(GOTO_STATEMENT_RE)
		if not m:
			return False
		if self.previous_state_id == -1:
			self.exception("Goto without a previous state")
		params = m.groupdict()
		label = params["label"]

		# Try to parse as an absolute state ID, ie. S_* enum name or
		# just an absolute state number. If so we set the nextstate
		# field directly and flag it so that we don't remap it later.
		goto_id = self.parse_state_number(label)
		if goto_id is not None:
			state = self.states[self.previous_state_id]
			state.nextstate = goto_id
			state.no_remap_nextstate = True
		else:
			# We can't "apply" this goto statement yet since it
			# may refer to a label that we haven't parsed yet. So
			# we save it for later.
			self.saved_gotos.append((
				self.line_number,
				self.previous_state_id,
				label,
				int(params.get("offset") or "0"),
			))

		self.previous_state_id = -1
		self.loop_start_id = -1
		return True

	def resolve_goto(self, line_number, label, offset):
		if label not in self.state_labels:
			self.exception("Goto to unknown label %r" % (label),
			               line_number=line_number)

		state_id = self.state_labels[label]
		for _ in range(offset):
			next_state_id = self.states[state_id].nextstate
			if next_state_id == -1:
				self.exception(
					"Goto offset %r + %d is longer than "
					"animation sequence" % (
						label, offset),
					line_number=line_number)
			state_id = next_state_id
		return state_id

	def apply_gotos(self):
		for line_number, state_id, label, offset in self.saved_gotos:
			self.states[state_id].nextstate = (
				self.resolve_goto(line_number, label, offset))

	def parse(self, defstr):
		# Split string into lines and remove comments:
		self.lines = [COMMENT_RE.sub("", line)
		              for line in defstr.split("\n")]
		self.line_number = 1
		while self.more_lines():
			if (not self.parse_frame_def() and
			    not self.parse_loop() and
			    not self.parse_goto() and
			    not self.parse_stop()):
				self.exception("Parse error")
		if self.previous_state_id != -1:
			self.exception("sequence should end in stop, loop, "
			               "or goto")
		self.apply_gotos()

def parse(defstr):
	"""Parses a string in DECORATE-style States {} syntax.

	Returned is a tuple containing two values:
	 - A list of state_t instances corresponding to the states described in
	   the string. The references in 'nextstate' are indexed relative to
	   the list itself; these can be copied and remapped into another
	   states list using remap_states().
	 - A dictionary mapping from label names defined in the string to
	   indexes in the states list to the states they represent.
	 - List of sprite names in the parsed states. The sprite field for each
	   state_t is an index into this list.
	"""
	p = _Parser()
	p.parse(defstr)
	return p.states, p.state_labels, p.sprnames

def _generate_old_to_new(old, new, alloc_states):
	"""Generate old ID -> new ID mapping table.

	It's assumed that state 0 is always NULL.
	"""
	if len(old) - 1 > len(alloc_states):
		raise StateRemapException(
			"Can't remap %d states from old: only have %d free "
			"states to work with." % (
				len(old) - 1, len(alloc_states)))

	# When parsing above we can flag states to be "pinned" to particular
	# state IDs when we copy into the state table. So assign these first
	# before we do any other logic.
	old_to_new = [0] * len(old)
	for old_id in range(1, len(old)):
		pin_id = getattr(old[old_id], "pin_state_id", -1)
		if pin_id == -1:
			continue
		if pin_id not in alloc_states:
			raise StateRemapException(
				"Can't pin parsed state to state #%d (%s); it "
				"is not found in alloc_states collection." % (
					pin_id, statenum_t[pin_id]))
		alloc_states.remove(pin_id)
		old_to_new[old_id] = pin_id

	# Categorize states by whether they can have an action pointer:
	alloc_action = set()
	alloc_non_action = set()
	for state_id in alloc_states:
		if new[state_id].original.action is not None:
			alloc_action.add(state_id)
		else:
			alloc_non_action.add(state_id)

	# Build old->new map, allocating from alloc_action for states which
	# need an action, and from alloc_non_action for states which don't.
	for old_id in range(1, len(old)):
		if hasattr(old[old_id], "pin_state_id"):
			continue
		if old[old_id].action is not None:
			if len(alloc_action) > 0:
				new_id = alloc_action.pop()
			else:
				# Won't work, unless BEX codeptrs are used:
				new_id = alloc_non_action.pop()
		else:
			if len(alloc_non_action) > 0:
				new_id = alloc_non_action.pop()
			else:
				# This is "wasteful" but there are no others:
				new_id = alloc_action.pop()
		old_to_new[old_id] = new_id
		alloc_states.remove(new_id)

	return old_to_new

def remap_states(old, new, alloc_states):
	"""Copy all states from old into new, remapping state IDs.

	alloc_states is a collection (list or set) of indexes into "new" which
	can be used to store the states copied from "old". Values are removed
	from this collection (via .pop()) that are consumed remapping states.

	The first state (old[0]) is not copied; it's assumed that state ID 0
	is a special value meaning NULL (S_NULL).
	"""
	old_to_new = _generate_old_to_new(old, new, alloc_states)

	# Copy over all states.
	for old_id in range(1, len(old)):
		new_id = old_to_new[old_id]
		new[new_id].copy_from(old[old_id])
		nextstate = new[new_id].nextstate
		# Remap the nextstate reference for the new array, unless it's
		# the "none" value of -1, or this state has been flagged to
		# reference an absolute state number and shouldn't be remapped.
		if (nextstate != -1 and
		    not getattr(old[old_id], "no_remap_nextstate", False)):
			new[new_id].nextstate = old_to_new[nextstate]

	return old_to_new

def remap_sprites(states, sprite_ids):
	"""Modify the given states to set the sprite fields."""
	for state in states:
		state.sprite = sprite_ids[state.sprite]


class TestParser(unittest.TestCase):
	TEST_INPUT = """
		# This is the spawn state:
		Spawn:
			TROO AB 10 A_Look
			Loop
		See:
			TROO AABBCCDD 3 A_Chase
			loop
		Melee:
		Missile:
			TROO EF 8 A_FaceTarget
			TROO G 6 A_TroopAttack
			goto S_CYBER_RUN3
		# Ouch! That hurt!
		Pain:
			TROO H 2
			TROO H 2 A_Pain
			Goto 456
		Death:
			TROO I 8 Bright
			TROO J 8 Bright A_Scream
		Pin(S_BFGEXP):
			TROO K 6
		Pin(199):
			TROO L 6 A_Fall
			TROO M -1
			Stop
		XDeath:
			TROO N 5
			TROO O 5 A_XScream
			TROO P 5
			TROO Q 5 A_Fall
			TROO RST 5
			TROO [\] 5
			TROO U -1
			Stop
		Raise:
			ASDF MLKJI 8
			Goto See
	"""

	def test_parse(self):
		expected_sprnames = [
			"TROO", "ASDF",
		]
		expected = c.StructArray(state_t, [
		(0,  0,  0, None,            0),  #  0
		(0,  0, 10, A_Look,          2),  #  1 Spawn:
		(0,  1, 10, A_Look,          1),  #  2 Loop

		(0,  0,  3, A_Chase,         4),  #  3 See:
		(0,  0,  3, A_Chase,         5),  #  4
		(0,  1,  3, A_Chase,         6),  #  5
		(0,  1,  3, A_Chase,         7),  #  6
		(0,  2,  3, A_Chase,         8),  #  7
		(0,  2,  3, A_Chase,         9),  #  8
		(0,  3,  3, A_Chase,        10),  #  9
		(0,  3,  3, A_Chase,         3),  # 10 Loop

		(0,  4,  8, A_FaceTarget,   12),  # 11 Melee:
		(0,  5,  8, A_FaceTarget,   13),  # 12
		(0,  6,  6, A_TroopAttack, 678),  # 13 Goto S_CYBER_RUN3

		(0,  7,  2, None,           15),  # 14 Pain:
		(0,  7,  2, A_Pain,        456),  # 15 Goto 456

		(0, 8|32768,  8, None,      17),  # 16 Death:
		(0, 9|32768,  8, A_Scream,  18),  # 17
		(0,      10,  6, None,      19),  # 18
		(0,      11,  6, A_Fall,    20),  # 19
		(0,      12, -1, None,       0),  # 20 Stop

		(0, 13,  5, None,           22),  # 21 XDeath:
		(0, 14,  5, A_XScream,      23),  # 22
		(0, 15,  5, None,           24),  # 23
		(0, 16,  5, A_Fall,         25),  # 24
		(0, 17,  5, None,           26),  # 25
		(0, 18,  5, None,           27),  # 26
		(0, 19,  5, None,           28),  # 27
		(0, 26,  5, None,           29),  # 28
		(0, 27,  5, None,           30),  # 29
		(0, 28,  5, None,           31),  # 30
		(0, 20, -1, None,            0),  # 31 Stop

		# Sprite number here is different (ASDF)
		(1, 12,  8, None,           33),  # 32 Raise:
		(1, 11,  8, None,           34),  # 33
		(1, 10,  8, None,           35),  # 34
		(1,  9,  8, None,           36),  # 35
		(1,  8,  8, None,            3),  # 36 Goto See
		])

		states, _, sprnames = parse(TestParser.TEST_INPUT)
		self.assertEqual(len(states), len(expected))
		self.assertEqual(sprnames, expected_sprnames)

		for i, got in enumerate(states):
			want = expected[i]
			msg = "mismatch in states[%d]" % i
			self.assertEqual(want.sprite, got.sprite, msg=msg)
			self.assertEqual(want.frame, got.frame, msg=msg)
			self.assertEqual(want.tics, got.tics, msg=msg)
			self.assertEqual(want.action, got.action, msg=msg)
			self.assertEqual(want.nextstate, got.nextstate,
			                 msg=msg)

	def test_labels(self):
		expected = {
			"Spawn":    1,
			"See":      3,
			"Melee":   11,
			"Missile": 11,
			"Pain":    14,
			"Death":   16,
			"XDeath":  21,
			"Raise":   32,

			"spawnstate":    1,
			"seestate":      3,
			"meleestate":   11,
			"missilestate": 11,
			"painstate":    14,
			"deathstate":   16,
			"xdeathstate":  21,
			"raisestate":   32,
		}
		_, labels, _ = parse(TestParser.TEST_INPUT)
		self.assertEqual(labels, expected)

	def test_no_remap(self):
		no_remap_states = {13, 15}
		states, _, _ = parse(TestParser.TEST_INPUT)
		for state_id, state in enumerate(states):
			if state_id in no_remap_states:
				self.assertTrue(state.no_remap_nextstate)
			else:
				self.assertFalse(
					hasattr(state, "no_remap_nextstate"))

	def test_pins(self):
		pins = {
			18: S_BFGEXP,
			19: 199,
		}
		states, _, _ = parse(TestParser.TEST_INPUT)
		for state_id, state in enumerate(states):
			if state_id in pins:
				self.assertEqual(state.pin_state_id,
				                 pins[state_id])
			else:
				self.assertFalse(
					hasattr(state, "pin_state_id"))


if __name__ == "__main__":
	unittest.main()

