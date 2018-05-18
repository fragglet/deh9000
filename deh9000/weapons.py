"""Constants and types representing Doom's weaponinfo array.

The weaponinfo array controls the various weapons wielded by the player during
play. In the Doom source code the equivalent definitions are found in
d_items.h.
"""

from __future__ import absolute_import

from deh9000 import c

class weaponinfo_t(c.Struct):
	DEHACKED_NAME = "Weapon"

	ammo       = c.StructField("Ammo type")
	upstate    = c.StructField("Deselect frame")
	downstate  = c.StructField("Select frame")
	readystate = c.StructField("Bobbing frame")
	atkstate   = c.StructField("Shooting frame")
	flashstate = c.StructField("Firing frame")

	state_fields = ("upstate", "downstate", "readystate", "atkstate",
	                "flashstate")


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

