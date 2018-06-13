"""MooD - a pacifist/tourist meta-mod for Doom

All monsters are pacifist and will not attack the player or each other.
The pistol has been replaced by the fist.
All weapon pickups have been replaced by the Health Potion.

For more information: https://jmtd.net/doom/mood/"""

from deh9000 import *

# pacifist monsters
for name in [ MT_POSSESSED, MT_SHOTGUY, MT_TROOP, MT_CHAINGUY, MT_VILE,
              MT_FATSO, MT_SERGEANT, MT_BRUISER, MT_KNIGHT, MT_SKULL,
              MT_SPIDER, MT_BABY, MT_CYBORG, MT_KEEN, MT_WOLFSS, MT_PAIN,
              MT_HEAD, MT_UNDEAD ]:
    monster = mobjinfo[name]

    states[monster.missilestate].tics = 1
    states[monster.missilestate].nextstate = monster.seestate

    # necessary if melee and missile use different frames (e.g. revenant)
    if monster.meleestate != 0:
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

# make all weapons copies of +1 health bottle (Except chainsaw)
for weapon in projectile_weapons:
    mobjinfo[weapon].spawnstate = mobjinfo[MT_MISC2].spawnstate # health potion

miscdata.initial_bullets = 0

# pistol becomes a fist
weaponinfo[wp_pistol].ammo = weaponinfo[wp_fist].ammo
for state in weaponinfo_t.state_fields:
    setattr(weaponinfo[wp_pistol], state, getattr(weaponinfo[wp_fist], state))

dehfile.save("mood.deh")
