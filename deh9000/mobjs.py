"""Constants and types representing Doom's mobjinfo array.

The mobjinfo array lists the types of thing which exist in Doom (monsters,
decorations, powerups, etc.). In the Doom source code the equivalent
definitions are found in info.h.
"""

import c

class mobjinfo_t(c.Struct):
	DEHACKED_NAME = "Thing"

	doomednum    = c.StructField("ID #")
	spawnstate   = c.StructField("Initial frame")
	spawnhealth  = c.StructField("Hit points")
	seestate     = c.StructField("First moving frame")
	seesound     = c.StructField("Alert sound")
	reactiontime = c.StructField("Reaction time")
	attacksound  = c.StructField("Attack sound")
	painstate    = c.StructField("Injury frame")
	painchance   = c.StructField("Pain chance")
	painsound    = c.StructField("Pain sound")
	meleestate   = c.StructField("Close attack frame")
	missilestate = c.StructField("Far attack frame")
	deathstate   = c.StructField("Death frame")
	xdeathstate  = c.StructField("Exploding frame")
	deathsound   = c.StructField("Death sound")
	speed        = c.StructField("Speed")
	radius       = c.StructField("Width")
	height       = c.StructField("Height")
	mass         = c.StructField("Mass")
	damage       = c.StructField("Missile damage")
	activesound  = c.StructField("Action sound")
	flags        = c.StructField("Bits")
	raisestate   = c.StructField("Respawn frame")

	# Which fields are references to entries in the states table?
	state_fields = ("spawnstate", "seestate", "painstate", "meleestate",
	                "missilestate", "deathstate", "xdeathstate",
	                "raisestate")

	# Which fields are references to entries in the S_sfx table?
	sound_fields = ("seesound", "attacksound", "painsound", "deathsound",
	                "activesound")

	# Because dehacked things are indexed from 1:
	def dehacked_header(self, array_index):
		return "Thing %d" % (array_index + 1)


class MobjArray(c.StructArray):
	def __init__(self, states):
		super(MobjArray, self).__init__(mobjinfo_t, states)

	def __copy__(self):
		result = MobjArray(states=self)
		result.original = self.original or self
		return result

	# We need to wrap parse_section() method to patch the array index:
	def parse_section(self, stream, index):
		index = int(index) - 1
		super(MobjArray, self).parse_section(
			stream, index="%d" % index)


FRACUNIT = 1 << 16

MF_SPECIAL = 1
MF_SOLID = 2
MF_SHOOTABLE = 4
MF_NOSECTOR = 8
MF_NOBLOCKMAP = 16
MF_AMBUSH = 32
MF_JUSTHIT = 64
MF_JUSTATTACKED = 128
MF_SPAWNCEILING = 256
MF_NOGRAVITY = 512
MF_DROPOFF = 0x400
MF_PICKUP = 0x800
MF_NOCLIP = 0x1000
MF_SLIDE = 0x2000
MF_FLOAT = 0x4000
MF_TELEPORT = 0x8000
MF_MISSILE = 0x10000
MF_DROPPED = 0x20000
MF_SHADOW = 0x40000
MF_NOBLOOD = 0x80000
MF_CORPSE = 0x100000
MF_INFLOAT = 0x200000
MF_COUNTKILL = 0x400000
MF_COUNTITEM = 0x800000
MF_SKULLFLY = 0x1000000
MF_NOTDMATCH = 0x2000000
MF_TRANSLATION = 0xc000000
MF_TRANSSHIFT = 26

mobjtype_t = c.Enum([
	"MT_PLAYER",
	"MT_POSSESSED",
	"MT_SHOTGUY",
	"MT_VILE",
	"MT_FIRE",
	"MT_UNDEAD",
	"MT_TRACER",
	"MT_SMOKE",
	"MT_FATSO",
	"MT_FATSHOT",
	"MT_CHAINGUY",
	"MT_TROOP",
	"MT_SERGEANT",
	"MT_SHADOWS",
	"MT_HEAD",
	"MT_BRUISER",
	"MT_BRUISERSHOT",
	"MT_KNIGHT",
	"MT_SKULL",
	"MT_SPIDER",
	"MT_BABY",
	"MT_CYBORG",
	"MT_PAIN",
	"MT_WOLFSS",
	"MT_KEEN",
	"MT_BOSSBRAIN",
	"MT_BOSSSPIT",
	"MT_BOSSTARGET",
	"MT_SPAWNSHOT",
	"MT_SPAWNFIRE",
	"MT_BARREL",
	"MT_TROOPSHOT",
	"MT_HEADSHOT",
	"MT_ROCKET",
	"MT_PLASMA",
	"MT_BFG",
	"MT_ARACHPLAZ",
	"MT_PUFF",
	"MT_BLOOD",
	"MT_TFOG",
	"MT_IFOG",
	"MT_TELEPORTMAN",
	"MT_EXTRABFG",
	"MT_MISC0",
	"MT_MISC1",
	"MT_MISC2",
	"MT_MISC3",
	"MT_MISC4",
	"MT_MISC5",
	"MT_MISC6",
	"MT_MISC7",
	"MT_MISC8",
	"MT_MISC9",
	"MT_MISC10",
	"MT_MISC11",
	"MT_MISC12",
	"MT_INV",
	"MT_MISC13",
	"MT_INS",
	"MT_MISC14",
	"MT_MISC15",
	"MT_MISC16",
	"MT_MEGA",
	"MT_CLIP",
	"MT_MISC17",
	"MT_MISC18",
	"MT_MISC19",
	"MT_MISC20",
	"MT_MISC21",
	"MT_MISC22",
	"MT_MISC23",
	"MT_MISC24",
	"MT_MISC25",
	"MT_CHAINGUN",
	"MT_MISC26",
	"MT_MISC27",
	"MT_MISC28",
	"MT_SHOTGUN",
	"MT_SUPERSHOTGUN",
	"MT_MISC29",
	"MT_MISC30",
	"MT_MISC31",
	"MT_MISC32",
	"MT_MISC33",
	"MT_MISC34",
	"MT_MISC35",
	"MT_MISC36",
	"MT_MISC37",
	"MT_MISC38",
	"MT_MISC39",
	"MT_MISC40",
	"MT_MISC41",
	"MT_MISC42",
	"MT_MISC43",
	"MT_MISC44",
	"MT_MISC45",
	"MT_MISC46",
	"MT_MISC47",
	"MT_MISC48",
	"MT_MISC49",
	"MT_MISC50",
	"MT_MISC51",
	"MT_MISC52",
	"MT_MISC53",
	"MT_MISC54",
	"MT_MISC55",
	"MT_MISC56",
	"MT_MISC57",
	"MT_MISC58",
	"MT_MISC59",
	"MT_MISC60",
	"MT_MISC61",
	"MT_MISC62",
	"MT_MISC63",
	"MT_MISC64",
	"MT_MISC65",
	"MT_MISC66",
	"MT_MISC67",
	"MT_MISC68",
	"MT_MISC69",
	"MT_MISC70",
	"MT_MISC71",
	"MT_MISC72",
	"MT_MISC73",
	"MT_MISC74",
	"MT_MISC75",
	"MT_MISC76",
	"MT_MISC77",
	"MT_MISC78",
	"MT_MISC79",
	"MT_MISC80",
	"MT_MISC81",
	"MT_MISC82",
	"MT_MISC83",
	"MT_MISC84",
	"MT_MISC85",
	"MT_MISC86",
])

mobjtype_t.create_globals(globals())

# To match the Doom source, but if you're really a Python programmer you
# probably shouldn't be using this.
NUMMOBJTYPES = len(mobjtype_t)

