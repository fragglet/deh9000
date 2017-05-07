"""Example program that replicates some of the DMARMY dehacked patch.

This classic patch included with Dehacked changes the Doom monsters to use
player marine sprites. The original is hand-crafted (I think) and changes all
of the monsters; this is a more limited version that just changes the former
humans, but does so in a programmatic way as a demo of DEH9000.
"""

from tables import *

humanoids = (MT_POSSESSED, MT_SHOTGUY, MT_CHAINGUY, MT_TROOP)
frame_fields = ("spawnstate", "seestate", "painstate", "meleestate",
                "missilestate", "deathstate", "xdeathstate", "raisestate")

def replace_sprites(startstate, newsprite):
	"""Update states in the given chain to change the sprite field.

	Starting from the given state index, this walks along the "nextstate"
	field setting the sprite to 'newsprite' for each in turn, until S_NULL
	is reached, or a state loop is detected.
	"""
	previous_states = {startstate}
	state = startstate
	while state != S_NULL:
		states[state].sprite = newsprite
		previous_states.add(state)
		state = states[state].nextstate
		if state in previous_states:
			return

def update_monster(mobjtype, color=0):
	"""Update the given mobjtype to look like a player."""
	mobj = mobjinfo[mobjtype]

	# Apply color.
	mobj.flags = (mobj.flags & ~MF_TRANSLATION) | (color << MF_TRANSSHIFT)

	# Sound like a player.
	mobj.seesound = sfx_None
	mobj.painsound = sfx_plpain
	mobj.deathsound = sfx_pldeth
	mobj.activesound = sfx_None

	for field_name in frame_fields:
		replace_sprites(getattr(mobj, field_name), SPR_PLAY)

# Update all humanoid monsters, and give them differing colors:
for i, mobjtype in enumerate(humanoids):
	color = i & 3
	update_monster(mobjtype, color)

# Change the imp to shoot a plasma ball instead of a fireball (or at least,
# we make the imp fireball look like a plasma ball).
mobjinfo[MT_TROOPSHOT].copy_from(mobjinfo[MT_PLASMA])

file.write("dmarmy.deh")

