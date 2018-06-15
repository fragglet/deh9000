"""MooD - a pacifist/tourist meta-mod for Doom

All monsters are pacifist and will not attack the player or each other.
The pistol has been replaced by the fist.
All weapon pickups have been replaced by the Health Potion.

For more information: https://jmtd.net/doom/mood/"""

from deh9000 import *

# pacifist monsters
for monster in mobjinfo:
	if not (monster.flags & MF_COUNTKILL) and monster != mobjinfo[MT_SKULL]:
		continue

	if monster.missilestate:
		states[monster.missilestate].tics = 1
		states[monster.missilestate].nextstate = monster.seestate

	# necessary if melee and missile use different frames (e.g. revenant)
	if monster.meleestate:
		states[monster.meleestate].tics = 1
		states[monster.meleestate].nextstate = monster.seestate

projectile_weapons = [
	MT_MISC25, # BFG 9000
	MT_MISC27, # Rocket Launcher
	MT_MISC28, # Plasma Gun
	MT_SHOTGUN,
	MT_SUPERSHOTGUN,
	MT_CHAINGUN
]

# make all weapons copies of +1 health potion (Except chainsaw)
for weapon in projectile_weapons:
	mobjinfo[weapon].spawnstate = mobjinfo[MT_MISC2].spawnstate

miscdata.initial_bullets = 0

# pistol becomes a fist
weaponinfo[wp_pistol].copy_from(weaponinfo[wp_fist])

dehfile.save("mood.deh")
