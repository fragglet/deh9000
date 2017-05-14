"""This module includes functions for reclaiming state table entries.

Often implementing new behaviors requires additional states. While there are a
few unused states in Doom's states tables, there are not many. The functions
in this file are designed to change Doom's states table - usually in subtle
and hard to notice ways - so that states are freed up for other purposes.
"""

from mobjs import *
from states import *

def changed(struct):
	"""Returns true if the given struct has changed."""
	return len(struct.dehacked_diffs()) > 0

def clear_pain_elemental_resurrections(file):
	"""Clears the resurrect sequences for the Pain Elemental.

	The Pain Elemental has an animation sequence for the Archvile to
	resurrect it, but it disappears when it dies so this can never
	happen.
	"""
	mobjinfo = file.array_for_type(mobjinfo_t)
	mobjinfo[MT_PAIN].raisestate = S_NULL

def simpler_boss_brain_death(file):
	"""Removes two frames from the boss brain death animation."""
	states = file.array_for_type(state_t)
	state = states[S_BRAIN_DIE1]
	if not changed(state):
		state.tics += (
			states[S_BRAIN_DIE2].tics + states[S_BRAIN_DIE3].tics)
		state.nextstate = S_BRAIN_DIE4

def static_tech_lamps(file, state_id):
	"""Makes tech lamps static instead of animated."""
	states = file.array_for_type(state_t)
	states[state_id].tics = -1

def simpler_bfg_hit(file):
	"""Removes the last two frames of the BFG ball hit animation."""
	states = file.array_for_type(state_t)
	states[S_BFGLAND5].nextstate = S_NULL

def teleport_fog_item_respawn(file):
	"""Replaces the item respawn fog with teleport fog."""
	mobjinfo = file.array_for_type(mobjinfo_t)
	mobjinfo[MT_IFOG].spawnstate = S_TFOG

def simpler_teleport_fog(file):
	"""Simplifies the teleport fog animation by removing 5 frames."""
	states = file.array_for_type(state_t)
	states[S_TFOG2].nextstate = S_TFOG4  # Skip TFOGC
	states[S_TFOG6].nextstate = S_NULL   # Short ending

def all_red_torches(file, mobjtype):
	"""Makes all torches into red torches (no green/red)."""
	new_sprite = {
		MT_MISC41: S_REDTORCH,
		MT_MISC42: S_REDTORCH,
		MT_MISC44: S_RTORCHSHRT,
		MT_MISC45: S_RTORCHSHRT,
	}
	mobjinfo = file.array_for_type(mobjinfo_t)
	if mobjtype in new_sprite:
		mobjinfo[mobjtype].spawnstate = new_sprite[mobjtype]

def all_green_pillars(file, mobjtype):
	"""Makes red marble pillars into green pillars."""
	new_sprite = {
		MT_MISC34: S_TALLGRNCOL,
		MT_MISC35: S_SHRTGRNCOL,
	}
	mobjinfo = file.array_for_type(mobjinfo_t)
	if mobjtype in new_sprite:
		mobjinfo[mobjtype].spawnstate = new_sprite[mobjtype]

def static_gore_decorations(file, mobjtype):
	"""Makes gore/corpse decorations static instead of animated."""
	mobjinfo = file.array_for_type(mobjinfo_t)
	states = file.array_for_type(state_t)

	# Twitching impaled body uses non-twitching frame (2 frames):
	if mobjtype == MT_MISC75:
		mobjinfo[MT_MISC75].spawnstate = S_DEADSTICK
	else:
		state_id = mobjinfo[mobjtype].spawnstate
		# S_HEADCANDLES: Skull pile doesn't flicker (1 frame)
		# S_HEARTCOL: Beating heart column doesn't beat: 1 frame
		# S_BLOODYTWITCH: Hanging dude becomes static (3 frames):
		states[state_id].tics = -1

def static_evil_eye(file):
	"""Makes the floating "evil" eye static instead of animated."""
	states = file.array_for_type(state_t)
	# Saves 3 frames:
	states[S_EVILEYE].tics = -1

def simpler_bonus(file, state_id):
	"""Removes the animation on health bottles/armor helmets."""
	states = file.array_for_type(state_t)
	# Health bottle / armor helmet are static (5 frames each). But
	# we show frame #3 as this looks good when static.
	states[state_id].tics = -1
	states[state_id].frame = 3

def simpler_powerups(file, state_id):
	"""Simplifies the animation of powerups."""
	states = file.array_for_type(state_t)

	new_nextstate = {
		S_PMAP: S_PMAP,     # 5 frames from automap
		S_SOUL3: S_SOUL6,   # 2 frames from soulsphere
		S_MEGA2: S_MEGA,    # 2 frames from megasphere
		S_PINV3: S_PINV,    # 1 frame from invuln
		S_PINS3: S_PINS,    # 1 frame from invis
		S_PVIS: S_PVIS,     # 1 frame from lite-amp
	}
	states[state_id].nextstate = new_nextstate[state_id]

def no_blinking(file, state_id):
	"""Makes keys and armor vests static and stop blinking."""
	states = file.array_for_type(state_t)
	states[state_id].frame = 32769
	states[state_id].tics = -1

def squash_resurrect_animations(file, mobjtype):
	"""Reduces the number of frames in monster resurrection animations."""
	mobjinfo = file.array_for_type(mobjinfo_t)
	states = file.array_for_type(state_t)
	monsters = {
		MT_POSSESSED: 8,  # POSSI0
		MT_SHOTGUY: 8,    # SPOSI0
		MT_UNDEAD: 13,    # SKELN0
		MT_FATSO: 14,     # FATTO0
		MT_CHAINGUY: 7,   # CPOSH0
		MT_TROOP: 9,      # TROOJ0
		MT_SERGEANT: 10,  # SARGK0
		MT_SHADOWS: 10,   # SARGK0
		MT_HEAD: 8,       # HEADI0
		MT_BRUISER: 9,    # BOSSJ0
		MT_KNIGHT: 9,     # BOS2J0
		MT_BABY: 9,       # BSPIJ0
		MT_WOLFSS: 9,     # SSWVJ0
	}
	frame = monsters[mobjtype]
	mobj = mobjinfo[mobjtype]
	# Have we squashed this sequence already?
	if changed(states[mobj.raisestate]):
		return
	# Count total tics for the resurrection animation:
	total_tics = 0
	terminal = set(states.walk(mobj.seestate))
	for state_id in states.walk(mobj.raisestate):
		state = states[state_id]
		total_tics += state.tics
		# Only walk until we reach a normal state.
		if state.nextstate in terminal:
			final_state_id = state.nextstate
	else:
		raise ValueError("monster %s didn't reach seestate" % (
			mobjtype_t[mobjtype]))

	# Replace the whole animation with a single frame:
	states[mobj.raisestate].frame = frame
	states[mobj.raisestate].tics = total_tics
	states[mobj.raisestate].nextstate = final_state_id

def no_ss_nazi_resurrection(file):
	"""Makes the SS Nazi impossible for an Archvile to resurrect."""
	mobjinfo = file.array_for_type(mobjinfo_t)
	mobjinfo[MT_WOLFSS].raisestate = S_NULL

def blue_arachnotron_plasma_balls(file):
	"""Makes Arachnotron plasma balls blue like the player's."""
	mobjinfo = file.array_for_type(mobjinfo_t)
	mobjinfo[MT_ARACHPLAZ].spawnstate = S_PLASBALL
	mobjinfo[MT_ARACHPLAZ].deathstate = S_PLASEXP

def no_ss_nazi(file):
	"""Replaces the SS Nazi with the Zombieman."""
	mobjinfo = file.array_for_type(mobjinfo_t)
	doomednum = mobjinfo[MT_WOLFSS].doomednum
	mobjinfo[MT_WOLFSS].copy_from(mobjinfo[MT_POSSESSED])
	mobjinfo[MT_WOLFSS].doomednum = doomednum

def hell_knight_identical_to_baron(file):
	"""Makes the Hell Knight look identical to the Baron."""
	mobjinfo = file.array_for_type(mobjinfo_t)
	knight = mobjinfo[MT_KNIGHT]
	baron = mobjinfo[MT_BRUISER]
	for field in mobjinfo_t.state_fields:
		setattr(knight, field, getattr(baron, field))

strategies = [
	clear_pain_elemental_resurrections,
	simpler_boss_brain_death,
	(static_tech_lamps,               S_TECHLAMP),
	(static_tech_lamps,               S_TECH2LAMP),
	simpler_bfg_hit,
	teleport_fog_item_respawn,
	simpler_teleport_fog,
	(all_red_torches,                 MT_MISC41),
	(all_red_torches,                 MT_MISC42),
	(all_red_torches,                 MT_MISC44),
	(all_red_torches,                 MT_MISC45),
	(all_green_pillars,               MT_MISC34),
	(all_green_pillars,               MT_MISC35),
	(static_gore_decorations,         MT_MISC75),
	(static_gore_decorations,         MT_MISC73),
	(static_gore_decorations,         MT_MISC37),
	(static_gore_decorations,         MT_MISC51),
	static_evil_eye,
	(simpler_bonus,                   S_BON1),
	(simpler_bonus,                   S_BON2),
	(simpler_powerups,                S_PMAP),
	(simpler_powerups,                S_SOUL3),
	(simpler_powerups,                S_MEGA2),
	(simpler_powerups,                S_PINV3),
	(simpler_powerups,                S_PINS3),
	(simpler_powerups,                S_PVIS),
	(no_blinking,                     S_RKEY),
	(no_blinking,                     S_BKEY),
	(no_blinking,                     S_YKEY),
	(no_blinking,                     S_RSKULL),
	(no_blinking,                     S_BSKULL),
	(no_blinking,                     S_YSKULL),
	(no_blinking,                     S_ARM1),
	(no_blinking,                     S_ARM2),
	(squash_resurrect_animations,     MT_WOLFSS),
	(squash_resurrect_animations,     MT_BABY),
	(squash_resurrect_animations,     MT_KNIGHT),
	(squash_resurrect_animations,     MT_BRUISER),
	(squash_resurrect_animations,     MT_HEAD),
	(squash_resurrect_animations,     MT_SHADOWS),
	(squash_resurrect_animations,     MT_SERGEANT),
	(squash_resurrect_animations,     MT_TROOP),
	(squash_resurrect_animations,     MT_CHAINGUY),
	(squash_resurrect_animations,     MT_FATSO),
	(squash_resurrect_animations,     MT_UNDEAD),
	(squash_resurrect_animations,     MT_SHOTGUY),
	(squash_resurrect_animations,     MT_POSSESSED),
	no_ss_nazi_resurrection,
	blue_arachnotron_plasma_balls,
	no_ss_nazi,
	hell_knight_identical_to_baron,
]

if __name__ == "__main__":
	import tables
	try:
		tables.file.reclaim_states(999, debug=True)
	except Exception as e:
		print e
	freed = tables.file.free_states()
	print "Reclaim strategies get a maximum of %d states:" % len(freed)
	w = 0
	for state_id in sorted(freed):
		s = statenum_t[state_id]
		if w + len(s) + 2 >= 76:
			print
			w = 0
		if w == 0:
			print "    ",
		print "%s," % s,
		w += len(s) + 2
	tables.file.write("simple.deh")

	with open("simple.deh", "a") as f:
		f.write("\n\n\n# Free frames:\n")
		for i, state_id in enumerate(sorted(freed)):
			if (i % 10) == 0:
				f.write("# ")
			f.write("% 3d," % (state_id + 1))
			if (i % 10) == 9:
				f.write("\n")
		f.write("\n\n")


