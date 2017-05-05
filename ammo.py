"""Constants and types representing Doom's ammo arrays.

These control constants about the different ammo types found in the
game. In the Doom source code the definitions from this file are found
in doomdef.h.
"""

import c

ammotype_t = c.Enum([
	"am_clip",    # Pistol / chaingun ammo.
	"am_shell",   # Shotgun / double barreled shotgun.
	"am_cell",    # Plasma rifle, BFG.
	"am_misl",    # Missile launcher.
	"NUMAMMO",
	"am_noammo",  # Unlimited for chainsaw / fist.
])

ammotype_t.create_globals(globals())

# No such type "ammodata_t" really exists in the Doom source; this is
# really just two separate arrays (clipammo and maxammo). But for
# Dehacked's purposes it's convenient to treat them as one, since it
# treats them as one thing.
ammodata_t = c.Struct("ammodata_t", "Ammo", [
	("clipammo", "Per ammo"),
	("maxammo",  "Max ammo"),
])

