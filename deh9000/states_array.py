"""This module implements an extension to StructArray for state_ts.

This is really only defined in its own module to avoid a circular
import dependency.
"""
import c
import states_parser
from states import state_t, S_NULL

class StatesArray(c.StructArray):
	"""Wrapper around StructArray that adds some extra methods."""

	def __init__(self, states):
		super(StatesArray, self).__init__(state_t, states)

	def walk(self, index):
		"""Iterate over states in sequence starting from given index.

		Each state in the states array has a "nextstate" field that
		indicates a state that follows it. This function returns a
		generator that yields the index of each state in the sequence,
		ending when the NULL state (0) is reached, a state is reached
		that never ends (tics < 0), or when a state is reached that
		has already been reached.
		"""
		previous_states = set()
		while index != S_NULL:
			yield index
			previous_states.add(index)
			if self[index].tics < 0:
				return
			index = self[index].nextstate
			if index in previous_states:
				return

	def parse(self, alloc_states, defstr):
		"""Parse list of states in DECORATE format, copying into array.

		In order to copy the states into the array, a collection of
		states to allocate must be provided (indexes into the array).
		States which are used will be removed from alloc_states.
		DehackedFile.free_states and DehackedFile.reclaim_states are
		useful functions to generate a list of states to use.

		Returned is a dictionary mapping from label name to index of
		state representing that label.
		"""
		states, labels = states_parser.parse(defstr)
		old_to_new = states_parser.remap_states(states, self,
		                                        alloc_states)
		return {label: old_to_new[state_id]
		        for label, state_id in labels.items()}


class CodePointers(object):
	"""Class that generates the Code Pointers blocks.

	Dehacked allows modification of the states table's 'action' field
	but it uses a weird mechanism to do so that uses separate blocks
	to the "Frame" blocks used for the rest of the fields.

	Every state which has an action pointer set (ie. in the original
	table) has a "pointer number" assigned to it, and only these states
	can be modified in dehacked patches.
	"""
	def __init__(self, states):
		self.lax_mode = False
		self.states = states
		self._state_to_pointer = {}
		self._action_to_state = {}
		for state_id, state in enumerate(states.original()):
			if state.action is not None:
				ptr_id = len(self._state_to_pointer)
				self._state_to_pointer[state_id] = ptr_id
				self._action_to_state[state.action] = state_id
			elif None not in self._action_to_state:
				# We want _action_to_state to contain at least
				# one entry for 'None', so we can null out
				# action pointers if desired.
				self._action_to_state[None] = state_id

	def match_key(self):
		return (CodePointers,)

	def _format_diff(self, ptr_id, state_id):
		state = self.states[state_id]
		return "Pointer %d (Frame %d)\nCodep Frame = %d" % (
			ptr_id, state_id,
			self._action_to_state[state.action])

	def _sanity_check_pointers(self):
		if self.lax_mode:
			return
		for state_id, state in enumerate(self.states):
			assert (state.action is None
			     or state_id in self._state_to_pointer), (
				"State %d has an action pointer, but it isn't "
				"valid to set a pointer on this state in a "
				"Vanilla Dehacked patch. Either use a "
				"different state, or turn on lax mode with "
				"strings.lax_mode = True" % (
					state_id,
				)
			)

	def dehacked_diffs(self, other=None):
		self._sanity_check_pointers()
		result = []
		for state_id, state in enumerate(self.states):
			if other is not None:
				other_state = other[state_id]
			else:
				other_state = state.original()
			# We need to look up the pointer ID for this state_id.
			# But Vanilla Dehacked (and certain source ports) only
			# allows action pointers to be changed in states that
			# originally had an action pointer. In this case
			# we just generate a fake pointer ID.
			if state.action != other_state.action:
				ptr_id = self._state_to_pointer.get(
					state_id, 100000 + state_id)
				result.append(
					self._format_diff(ptr_id, state_id))
		return result

