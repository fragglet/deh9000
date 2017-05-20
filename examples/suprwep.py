"""Example program that recreates some of SUPRWEP8.DEH.

This classic patch included with Dehacked upgrades the player's weapons to be
as powerful as they possibly can be.
"""

from deh9000 import *

ignore_actions = (A_BFGsound, A_GunFlash)

def upgrade_weapon(weapon):
	# The weapon fire animation sequence ends with a state that
	# has action pointer A_ReFire. Seek through the animation
	# sequence to find which frame this is.
	for index in states.walk(weapon.atkstate):
		if states[index].action == A_ReFire:
			refire_state = index
			break

	# Now walk through the animation sequence again and set the
	# delay between frames to zero so that it is as fast as
	# possible. We probably want to "freeze frame" on the frame
	# that is shown at the moment of firing - this is usually the
	# first frame with an action pointer (though we must ignore
	# a couple of action pointers). Once we reach this frame,
	# jump to the refire frame immediately afterwards.
	for index in states.walk(weapon.atkstate):
		states[index].tics = 0
		action = states[index].action
		if action and action not in ignore_actions:
			states[index].tics = 1
			states[index].nextstate = refire_state
			break

for w in range(NUMWEAPONS):
	upgrade_weapon(weaponinfo[w])

# Given how fast the weapons fire we want as much ammo as possible.
for a in range(NUMAMMO):
	ammodata[a].clipammo = 100000
	ammodata[a].maxammo = 100000

dehfile.write("suprwep.deh")

