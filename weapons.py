"""Constants and types representing Doom's weaponinfo array.

The weaponinfo array controls the various weapons wielded by the player during
play. In the Doom source code the equivalent definitions are found in
d_items.h.
"""

import c

weapontype_t = c.Enum([
	"wp_fist",
	"wp_pistol",
	"wp_shotgun",
	"wp_chaingun",
	"wp_missile",
	"wp_plasma",
	"wp_bfg",
	"wp_chainsaw",
	"wp_supershotgun",
])

weapontype_t.create_globals(globals())

NUMWEAPONS = len(weapontype_t)

weaponinfo_t = c.Struct("weaponinfo_t", "Weapon", [
	("ammo",        "Ammo type"),
	("upstate",     "Deselect frame"),
	("downstate",   "Select frame"),
	("readystate",  "Bobbing frame"),
	("atkstate",    "Shooting frame"),
	("flashstate",  "Firing frame"),
])

