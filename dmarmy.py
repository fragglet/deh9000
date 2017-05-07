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

	# Check all state fields and walk animation sequences to change
	# them all to use the player sprite:
	for field_name in frame_fields:
		startstate = getattr(mobj, field_name)
		for index in states.walk(startstate):
			states[index].sprite = SPR_PLAY

# Update all humanoid monsters, and give them differing colors:
for i, mobjtype in enumerate(humanoids):
	color = i & 3
	update_monster(mobjtype, color)

# Change the imp to shoot a plasma ball instead of a fireball (or at least,
# we make the imp fireball look like a plasma ball).
mobjinfo[MT_TROOPSHOT].copy_from(mobjinfo[MT_PLASMA])

file.write("dmarmy.deh")

