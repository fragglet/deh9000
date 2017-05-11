"""This module includes functions for reclaiming state table entries.

Often implementing new behaviors requires additional states. While there are a
few unused states in Doom's states tables, there are not many. The functions
in this file are designed to change Doom's states table - usually in subtle
and hard to notice ways - so that states are freed up for other purposes.
"""

from mobjs import *
from states import *

def clear_unused_resurrections(file):
	"""Clears the resurrect sequences for the Lost Soul/Pain Elemental.

	These monsters have animation sequences for the Archvile to
	resurrect them, but they disappear when they die so this can never
	happen.
	"""
	mobjinfo = file.array_for_type(mobjinfo_t)
	mobjinfo[MT_SKULL].raisestate = S_NULL
	mobjinfo[MT_PAIN].raisestate = S_NULL

def simpler_boss_brain_death(file):
	"""Removes two frames from the boss brain death animation."""
	states = file.array_for_type(state_t)
	states[S_BRAIN_DIE1].tics += (
		states[S_BRAIN_DIE2].tics + states[S_BRAIN_DIE3].tics)
	states[S_BRAIN_DIE1].nextstate = S_BRAIN_DIE4

def static_tech_lamps(file):
	"""Makes tech lamps static instead of animated."""
	states = file.array_for_type(state_t)
	states[S_TECHLAMP].nextstate = S_TECHLAMP
	states[S_TECHLAMP2].nextstate = S_TECHLAMP2

def simpler_bfg_hit(file):
	"""Removes the last two frames of the BFG ball hit animation."""
	states = file.array_for_type(state_t)
	states[S_BFGLAND4].nextstate = S_NULL

def teleport_fog_item_respawn(file):
	"""Replaces the item respawn fog with teleport fog."""
	mobjinfo = file.array_for_type(mobjinfo_t)
	mobjinfo[MT_IFOG].spawnstate = S_TFOG

def simpler_teleport_fog(file):
	"""Simplifies the teleport fog animation by removing 5 frames."""
	states = file.array_for_type(state_t)
	states[S_TFOG2].nextstate = S_TFOG4  # Skip TFOGC
	states[S_TFOG6].nextstate = S_NULL   # Short ending

def all_red_torches(file):
	"""Makes all torches into red torches (no green/red)."""
	mobjinfo = file.array_for_type(mobjinfo_t)
	mobjinfo[MT_MISC41].spawnstate = S_REDTORCH
	mobjinfo[MT_MISC42].spawnstate = S_REDTORCH
	mobjinfo[MT_MISC44].spawnstate = S_RTORCHSHRT
	mobjinfo[MT_MISC45].spawnstate = S_RTORCHSHRT

def all_green_pillars(file):
	"""Makes red marble pillars into green pillars."""
	mobjinfo = file.array_for_type(mobjinfo_t)
	mobjinfo[MT_MISC34].spawnstate = S_TALLGRNCOL
	mobjinfo[MT_MISC35].spawnstate = S_SHRTGRNCOL

def static_gore_decorations(file):
	"""Makes gore/corpse decorations static instead of animated."""
	mobjinfo = file.array_for_type(mobjinfo_t)
	states = file.array_for_type(state_t)
	# Twitching impaled body uses non-twitching frame (2 frames):
	mobjinfo[MT_MISC75].spawnstate = S_DEADSTICK
	# Skull pile doesn't flicker (1 frame)
	states[S_HEADCANDLES].nextstate = S_HEADCANDLES
	# Beating heart column doesn't beat: 1 frame
	states[S_HEARTCOL].nextstate = S_HEARTCOL
	# Hanging dude becomes static (3 frames):
	states[S_BLOODYTWITCH].nextstate = S_BLOODYTWITCH

def static_evil_eye(file):
	"""Makes the floating "evil" eye static instead of animated."""
	states = file.array_for_type(state_t)
	# Saves 3 frames:
	states[S_EVILEYE].nextstate = S_EVILEYE

def simpler_powerups(file):
	"""Simplifies the animation of powerups."""
	states = file.array_for_type(state_t)

	# Health bottle / armor helmet are static (5 frames each)
	states[S_BON1].nextstate = S_BON1
	states[S_BON1].frame = 3
	states[S_BON2].nextstate = S_BON2
	states[S_BON2].frame = 3

	states[S_PMAP].nextstate = S_PMAP    # 5 frames from automap
	states[S_SOUL3].nextstate = S_SOUL6  # 2 frames from soulsphere
	states[S_MEGA2].nextstate = S_MEGA   # 2 frames from megasphere
	states[S_PINV3].nextstate = S_PINV   # 1 frame from invuln
	states[S_PINS3].nextstate = S_PINS   # 1 frame from invis
	states[S_PVIS].nextstate = S_PVIS    # 1 frame from lite-amp

def no_blinking(file):
	"""Makes keys and armor vests static and stop blinking."""
	states = file.array_for_type(state_t)
	blinkers = (
		S_RKEY, S_BKEY, S_YKEY, S_RSKULL, S_BSKULL, S_YSKULL,
		S_ARM1, S_ARM2,
	)
	for state in blinkers:
		states[state].frame = 32769
		states[state].nextstate = state

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
	clear_unused_resurrections,
	simpler_boss_brain_death,
	static_tech_lamps,
	simpler_bfg_hit,
	teleport_fog_item_respawn,
	simpler_teleport_fog,
	all_red_torches,
	all_green_pillars,
	static_gore_decorations,
	simpler_powerups,
	no_blinking,
	no_ss_nazi_resurrection,
	blue_arachnotron_plasma_balls,
	no_ss_nazi,
	hell_knight_identical_to_baron,
]
