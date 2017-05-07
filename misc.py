"""Definitions for Dehacked Misc section

The Misc section is a random collection of code hacks to tweak various in-game
constants. These are scattered throughout the Doom source; filenames are
listed below.
"""


import c

# The Doom source doesn't really have a deh_misc_t type, but it's convenient
# to represent this like a C struct. The field names match the names found in
# Chocolate Doom.
deh_misc_t = c.Struct("deh_misc_t", "Misc", [

	# This is the initial health a player has when starting anew.
	# See G_PlayerReborn in g_game.c
	("initial_health",     "Initial Health"),

	# This is the number of bullets the player has when starting anew.
	# See G_PlayerReborn in g_game.c
	("initial_bullets",    "Initial Bullets"),

	# This is the maximum health that can be reached using medikits
	# alone.  See P_TouchSpecialThing in p_inter.c
	("max_health",         "Max Health"),

	# This is the maximum armor which can be reached by picking up
	# armor helmets. See P_TouchSpecialThing in p_inter.c
	("max_armor",          "Max Armor"),

	# This is the armor class that is given when picking up the green
	# armor or an armor helmet. See P_TouchSpecialThing in p_inter.c
	#
	# DOS dehacked only modifies the behavior of the green armor shirt,
	# the armor class set by armor helmets is not affected.
	("green_armor_class",  "Green Armor Class"),

	# This is the armor class that is given when picking up the blue
	# armor or a megasphere. See P_TouchSpecialThing in p_inter.c
	#
	# DOS dehacked only modifies the MegaArmor behavior and not
	# the MegaSphere, which always gives armor type 2.
	("blue_armor_class",   "Blue Armor Class"),

	# The maximum health which can be reached by picking up the
	# soulsphere.  See P_TouchSpecialThing in p_inter.c
	("max_soulsphere",     "Max Soulsphere"),

	# The amount of health bonus that picking up a soulsphere
	# gives.  See P_TouchSpecialThing in p_inter.c
	("soulsphere_health",  "Soulsphere Health"),

	# This is what the health is set to after picking up a
	# megasphere.  See P_TouchSpecialThing in p_inter.c
	("megasphere_health",  "Megasphere Health"),

	# This is what the health value is set to when cheating using
	# the IDDQD god mode cheat.  See ST_Responder in st_stuff.c
	("god_mode_health",    "God Mode Health"),

	# This is what the armor is set to when using the IDFA cheat.
	# See ST_Responder in st_stuff.c
	("idfa_armor",         "IDFA Armor"),

	# This is what the armor class is set to when using the IDFA cheat.
	# See ST_Responder in st_stuff.c
	("idfa_armor_class",   "IDFA Armor Class"),

	# This is what the armor is set to when using the IDKFA cheat.
	# See ST_Responder in st_stuff.c
	("idkfa_armor",        "IDKFA Armor"),

	# This is what the armor class is set to when using the IDKFA cheat.
	# See ST_Responder in st_stuff.c
	("idkfa_armor_class",  "IDKFA Armor Class"),

	# This is the number of CELLs firing the BFG uses up.
	# See P_CheckAmmo and A_FireBFG in p_pspr.c
	("bfg_cells_per_shot", "BFG Cells/Shot"),

	# This controls whether monsters can harm other monsters of the same
	# species.  For example, whether an imp fireball will damage other
	# imps.  The value of this in dehacked patches is weird - '202' means
	# off, while '221' means on.
	#
	# See PIT_CheckThing in p_map.c
	("species_infighting", "Monsters infight"),
])

