
import collections
from sounds import *
from states import *

Mobj = collections.namedtuple("Mobj", [
    "doomednum",
    "spawnstate",
    "spawnhealth",
    "seestate",
    "seesound",
    "reactiontime",
    "attacksound",
    "painstate",
    "painchance",
    "painsound",
    "meleestate",
    "missilestate",
    "deathstate",
    "xdeathstate",
    "deathsound",
    "speed",
    "radius",
    "height",
    "mass",
    "damage",
    "activesound",
    "flags",
    "raisestate",
])

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

MOBJ_NAMES = [
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
]

for index, name in enumerate(MOBJ_NAMES):
    globals()[name] = index


MOBJS = [
    Mobj(		# MT_PLAYER
	-1,		# doomednum
	S_PLAY,		# spawnstate
	100,		# spawnhealth
	S_PLAY_RUN1,		# seestate
	sfx_None,		# seesound
	0,		# reactiontime
	sfx_None,		# attacksound
	S_PLAY_PAIN,		# painstate
	255,		# painchance
	sfx_plpain,		# painsound
	S_NULL,		# meleestate
	S_PLAY_ATK1,		# missilestate
	S_PLAY_DIE1,		# deathstate
	S_PLAY_XDIE1,		# xdeathstate
	sfx_pldeth,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	56*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_DROPOFF|MF_PICKUP|MF_NOTDMATCH,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_POSSESSED
	3004,		# doomednum
	S_POSS_STND,		# spawnstate
	20,		# spawnhealth
	S_POSS_RUN1,		# seestate
	sfx_posit1,		# seesound
	8,		# reactiontime
	sfx_pistol,		# attacksound
	S_POSS_PAIN,		# painstate
	200,		# painchance
	sfx_popain,		# painsound
	0,		# meleestate
	S_POSS_ATK1,		# missilestate
	S_POSS_DIE1,		# deathstate
	S_POSS_XDIE1,		# xdeathstate
	sfx_podth1,		# deathsound
	8,		# speed
	20*FRACUNIT,		# radius
	56*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_posact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL,		# flags
	S_POSS_RAISE1		# raisestate
    ),

    Mobj(		# MT_SHOTGUY
	9,		# doomednum
	S_SPOS_STND,		# spawnstate
	30,		# spawnhealth
	S_SPOS_RUN1,		# seestate
	sfx_posit2,		# seesound
	8,		# reactiontime
	0,		# attacksound
	S_SPOS_PAIN,		# painstate
	170,		# painchance
	sfx_popain,		# painsound
	0,		# meleestate
	S_SPOS_ATK1,		# missilestate
	S_SPOS_DIE1,		# deathstate
	S_SPOS_XDIE1,		# xdeathstate
	sfx_podth2,		# deathsound
	8,		# speed
	20*FRACUNIT,		# radius
	56*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_posact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL,		# flags
	S_SPOS_RAISE1		# raisestate
    ),

    Mobj(		# MT_VILE
	64,		# doomednum
	S_VILE_STND,		# spawnstate
	700,		# spawnhealth
	S_VILE_RUN1,		# seestate
	sfx_vilsit,		# seesound
	8,		# reactiontime
	0,		# attacksound
	S_VILE_PAIN,		# painstate
	10,		# painchance
	sfx_vipain,		# painsound
	0,		# meleestate
	S_VILE_ATK1,		# missilestate
	S_VILE_DIE1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_vildth,		# deathsound
	15,		# speed
	20*FRACUNIT,		# radius
	56*FRACUNIT,		# height
	500,		# mass
	0,		# damage
	sfx_vilact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_FIRE
	-1,		# doomednum
	S_FIRE1,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_UNDEAD
	66,		# doomednum
	S_SKEL_STND,		# spawnstate
	300,		# spawnhealth
	S_SKEL_RUN1,		# seestate
	sfx_skesit,		# seesound
	8,		# reactiontime
	0,		# attacksound
	S_SKEL_PAIN,		# painstate
	100,		# painchance
	sfx_popain,		# painsound
	S_SKEL_FIST1,		# meleestate
	S_SKEL_MISS1,		# missilestate
	S_SKEL_DIE1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_skedth,		# deathsound
	10,		# speed
	20*FRACUNIT,		# radius
	56*FRACUNIT,		# height
	500,		# mass
	0,		# damage
	sfx_skeact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL,		# flags
	S_SKEL_RAISE1		# raisestate
    ),

    Mobj(		# MT_TRACER
	-1,		# doomednum
	S_TRACER,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_skeatk,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_TRACEEXP1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_barexp,		# deathsound
	10*FRACUNIT,		# speed
	11*FRACUNIT,		# radius
	8*FRACUNIT,		# height
	100,		# mass
	10,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_MISSILE|MF_DROPOFF|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_SMOKE
	-1,		# doomednum
	S_SMOKE1,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_FATSO
	67,		# doomednum
	S_FATT_STND,		# spawnstate
	600,		# spawnhealth
	S_FATT_RUN1,		# seestate
	sfx_mansit,		# seesound
	8,		# reactiontime
	0,		# attacksound
	S_FATT_PAIN,		# painstate
	80,		# painchance
	sfx_mnpain,		# painsound
	0,		# meleestate
	S_FATT_ATK1,		# missilestate
	S_FATT_DIE1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_mandth,		# deathsound
	8,		# speed
	48*FRACUNIT,		# radius
	64*FRACUNIT,		# height
	1000,		# mass
	0,		# damage
	sfx_posact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL,		# flags
	S_FATT_RAISE1		# raisestate
    ),

    Mobj(		# MT_FATSHOT
	-1,		# doomednum
	S_FATSHOT1,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_firsht,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_FATSHOTX1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_firxpl,		# deathsound
	20*FRACUNIT,		# speed
	6*FRACUNIT,		# radius
	8*FRACUNIT,		# height
	100,		# mass
	8,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_MISSILE|MF_DROPOFF|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_CHAINGUY
	65,		# doomednum
	S_CPOS_STND,		# spawnstate
	70,		# spawnhealth
	S_CPOS_RUN1,		# seestate
	sfx_posit2,		# seesound
	8,		# reactiontime
	0,		# attacksound
	S_CPOS_PAIN,		# painstate
	170,		# painchance
	sfx_popain,		# painsound
	0,		# meleestate
	S_CPOS_ATK1,		# missilestate
	S_CPOS_DIE1,		# deathstate
	S_CPOS_XDIE1,		# xdeathstate
	sfx_podth2,		# deathsound
	8,		# speed
	20*FRACUNIT,		# radius
	56*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_posact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL,		# flags
	S_CPOS_RAISE1		# raisestate
    ),

    Mobj(		# MT_TROOP
	3001,		# doomednum
	S_TROO_STND,		# spawnstate
	60,		# spawnhealth
	S_TROO_RUN1,		# seestate
	sfx_bgsit1,		# seesound
	8,		# reactiontime
	0,		# attacksound
	S_TROO_PAIN,		# painstate
	200,		# painchance
	sfx_popain,		# painsound
	S_TROO_ATK1,		# meleestate
	S_TROO_ATK1,		# missilestate
	S_TROO_DIE1,		# deathstate
	S_TROO_XDIE1,		# xdeathstate
	sfx_bgdth1,		# deathsound
	8,		# speed
	20*FRACUNIT,		# radius
	56*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_bgact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL,		# flags
	S_TROO_RAISE1		# raisestate
    ),

    Mobj(		# MT_SERGEANT
	3002,		# doomednum
	S_SARG_STND,		# spawnstate
	150,		# spawnhealth
	S_SARG_RUN1,		# seestate
	sfx_sgtsit,		# seesound
	8,		# reactiontime
	sfx_sgtatk,		# attacksound
	S_SARG_PAIN,		# painstate
	180,		# painchance
	sfx_dmpain,		# painsound
	S_SARG_ATK1,		# meleestate
	0,		# missilestate
	S_SARG_DIE1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_sgtdth,		# deathsound
	10,		# speed
	30*FRACUNIT,		# radius
	56*FRACUNIT,		# height
	400,		# mass
	0,		# damage
	sfx_dmact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL,		# flags
	S_SARG_RAISE1		# raisestate
    ),

    Mobj(		# MT_SHADOWS
	58,		# doomednum
	S_SARG_STND,		# spawnstate
	150,		# spawnhealth
	S_SARG_RUN1,		# seestate
	sfx_sgtsit,		# seesound
	8,		# reactiontime
	sfx_sgtatk,		# attacksound
	S_SARG_PAIN,		# painstate
	180,		# painchance
	sfx_dmpain,		# painsound
	S_SARG_ATK1,		# meleestate
	0,		# missilestate
	S_SARG_DIE1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_sgtdth,		# deathsound
	10,		# speed
	30*FRACUNIT,		# radius
	56*FRACUNIT,		# height
	400,		# mass
	0,		# damage
	sfx_dmact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_SHADOW|MF_COUNTKILL,		# flags
	S_SARG_RAISE1		# raisestate
    ),

    Mobj(		# MT_HEAD
	3005,		# doomednum
	S_HEAD_STND,		# spawnstate
	400,		# spawnhealth
	S_HEAD_RUN1,		# seestate
	sfx_cacsit,		# seesound
	8,		# reactiontime
	0,		# attacksound
	S_HEAD_PAIN,		# painstate
	128,		# painchance
	sfx_dmpain,		# painsound
	0,		# meleestate
	S_HEAD_ATK1,		# missilestate
	S_HEAD_DIE1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_cacdth,		# deathsound
	8,		# speed
	31*FRACUNIT,		# radius
	56*FRACUNIT,		# height
	400,		# mass
	0,		# damage
	sfx_dmact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_FLOAT|MF_NOGRAVITY|MF_COUNTKILL,		# flags
	S_HEAD_RAISE1		# raisestate
    ),

    Mobj(		# MT_BRUISER
	3003,		# doomednum
	S_BOSS_STND,		# spawnstate
	1000,		# spawnhealth
	S_BOSS_RUN1,		# seestate
	sfx_brssit,		# seesound
	8,		# reactiontime
	0,		# attacksound
	S_BOSS_PAIN,		# painstate
	50,		# painchance
	sfx_dmpain,		# painsound
	S_BOSS_ATK1,		# meleestate
	S_BOSS_ATK1,		# missilestate
	S_BOSS_DIE1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_brsdth,		# deathsound
	8,		# speed
	24*FRACUNIT,		# radius
	64*FRACUNIT,		# height
	1000,		# mass
	0,		# damage
	sfx_dmact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL,		# flags
	S_BOSS_RAISE1		# raisestate
    ),

    Mobj(		# MT_BRUISERSHOT
	-1,		# doomednum
	S_BRBALL1,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_firsht,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_BRBALLX1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_firxpl,		# deathsound
	15*FRACUNIT,		# speed
	6*FRACUNIT,		# radius
	8*FRACUNIT,		# height
	100,		# mass
	8,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_MISSILE|MF_DROPOFF|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_KNIGHT
	69,		# doomednum
	S_BOS2_STND,		# spawnstate
	500,		# spawnhealth
	S_BOS2_RUN1,		# seestate
	sfx_kntsit,		# seesound
	8,		# reactiontime
	0,		# attacksound
	S_BOS2_PAIN,		# painstate
	50,		# painchance
	sfx_dmpain,		# painsound
	S_BOS2_ATK1,		# meleestate
	S_BOS2_ATK1,		# missilestate
	S_BOS2_DIE1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_kntdth,		# deathsound
	8,		# speed
	24*FRACUNIT,		# radius
	64*FRACUNIT,		# height
	1000,		# mass
	0,		# damage
	sfx_dmact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL,		# flags
	S_BOS2_RAISE1		# raisestate
    ),

    Mobj(		# MT_SKULL
	3006,		# doomednum
	S_SKULL_STND,		# spawnstate
	100,		# spawnhealth
	S_SKULL_RUN1,		# seestate
	0,		# seesound
	8,		# reactiontime
	sfx_sklatk,		# attacksound
	S_SKULL_PAIN,		# painstate
	256,		# painchance
	sfx_dmpain,		# painsound
	0,		# meleestate
	S_SKULL_ATK1,		# missilestate
	S_SKULL_DIE1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_firxpl,		# deathsound
	8,		# speed
	16*FRACUNIT,		# radius
	56*FRACUNIT,		# height
	50,		# mass
	3,		# damage
	sfx_dmact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_FLOAT|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_SPIDER
	7,		# doomednum
	S_SPID_STND,		# spawnstate
	3000,		# spawnhealth
	S_SPID_RUN1,		# seestate
	sfx_spisit,		# seesound
	8,		# reactiontime
	sfx_shotgn,		# attacksound
	S_SPID_PAIN,		# painstate
	40,		# painchance
	sfx_dmpain,		# painsound
	0,		# meleestate
	S_SPID_ATK1,		# missilestate
	S_SPID_DIE1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_spidth,		# deathsound
	12,		# speed
	128*FRACUNIT,		# radius
	100*FRACUNIT,		# height
	1000,		# mass
	0,		# damage
	sfx_dmact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_BABY
	68,		# doomednum
	S_BSPI_STND,		# spawnstate
	500,		# spawnhealth
	S_BSPI_SIGHT,		# seestate
	sfx_bspsit,		# seesound
	8,		# reactiontime
	0,		# attacksound
	S_BSPI_PAIN,		# painstate
	128,		# painchance
	sfx_dmpain,		# painsound
	0,		# meleestate
	S_BSPI_ATK1,		# missilestate
	S_BSPI_DIE1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_bspdth,		# deathsound
	12,		# speed
	64*FRACUNIT,		# radius
	64*FRACUNIT,		# height
	600,		# mass
	0,		# damage
	sfx_bspact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL,		# flags
	S_BSPI_RAISE1		# raisestate
    ),

    Mobj(		# MT_CYBORG
	16,		# doomednum
	S_CYBER_STND,		# spawnstate
	4000,		# spawnhealth
	S_CYBER_RUN1,		# seestate
	sfx_cybsit,		# seesound
	8,		# reactiontime
	0,		# attacksound
	S_CYBER_PAIN,		# painstate
	20,		# painchance
	sfx_dmpain,		# painsound
	0,		# meleestate
	S_CYBER_ATK1,		# missilestate
	S_CYBER_DIE1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_cybdth,		# deathsound
	16,		# speed
	40*FRACUNIT,		# radius
	110*FRACUNIT,		# height
	1000,		# mass
	0,		# damage
	sfx_dmact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_PAIN
	71,		# doomednum
	S_PAIN_STND,		# spawnstate
	400,		# spawnhealth
	S_PAIN_RUN1,		# seestate
	sfx_pesit,		# seesound
	8,		# reactiontime
	0,		# attacksound
	S_PAIN_PAIN,		# painstate
	128,		# painchance
	sfx_pepain,		# painsound
	0,		# meleestate
	S_PAIN_ATK1,		# missilestate
	S_PAIN_DIE1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_pedth,		# deathsound
	8,		# speed
	31*FRACUNIT,		# radius
	56*FRACUNIT,		# height
	400,		# mass
	0,		# damage
	sfx_dmact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_FLOAT|MF_NOGRAVITY|MF_COUNTKILL,		# flags
	S_PAIN_RAISE1		# raisestate
    ),

    Mobj(		# MT_WOLFSS
	84,		# doomednum
	S_SSWV_STND,		# spawnstate
	50,		# spawnhealth
	S_SSWV_RUN1,		# seestate
	sfx_sssit,		# seesound
	8,		# reactiontime
	0,		# attacksound
	S_SSWV_PAIN,		# painstate
	170,		# painchance
	sfx_popain,		# painsound
	0,		# meleestate
	S_SSWV_ATK1,		# missilestate
	S_SSWV_DIE1,		# deathstate
	S_SSWV_XDIE1,		# xdeathstate
	sfx_ssdth,		# deathsound
	8,		# speed
	20*FRACUNIT,		# radius
	56*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_posact,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_COUNTKILL,		# flags
	S_SSWV_RAISE1		# raisestate
    ),

    Mobj(		# MT_KEEN
	72,		# doomednum
	S_KEENSTND,		# spawnstate
	100,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_KEENPAIN,		# painstate
	256,		# painchance
	sfx_keenpn,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_COMMKEEN,		# deathstate
	S_NULL,		# xdeathstate
	sfx_keendt,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	72*FRACUNIT,		# height
	10000000,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID|MF_SPAWNCEILING|MF_NOGRAVITY|MF_SHOOTABLE|MF_COUNTKILL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_BOSSBRAIN
	88,		# doomednum
	S_BRAIN,		# spawnstate
	250,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_BRAIN_PAIN,		# painstate
	255,		# painchance
	sfx_bospn,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_BRAIN_DIE1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_bosdth,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	10000000,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID|MF_SHOOTABLE,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_BOSSSPIT
	89,		# doomednum
	S_BRAINEYE,		# spawnstate
	1000,		# spawnhealth
	S_BRAINEYESEE,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	32*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_NOSECTOR,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_BOSSTARGET
	87,		# doomednum
	S_NULL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	32*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_NOSECTOR,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_SPAWNSHOT
	-1,		# doomednum
	S_SPAWN1,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_bospit,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_firxpl,		# deathsound
	10*FRACUNIT,		# speed
	6*FRACUNIT,		# radius
	32*FRACUNIT,		# height
	100,		# mass
	3,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_MISSILE|MF_DROPOFF|MF_NOGRAVITY|MF_NOCLIP,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_SPAWNFIRE
	-1,		# doomednum
	S_SPAWNFIRE1,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_BARREL
	2035,		# doomednum
	S_BAR1,		# spawnstate
	20,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_BEXP,		# deathstate
	S_NULL,		# xdeathstate
	sfx_barexp,		# deathsound
	0,		# speed
	10*FRACUNIT,		# radius
	42*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID|MF_SHOOTABLE|MF_NOBLOOD,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_TROOPSHOT
	-1,		# doomednum
	S_TBALL1,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_firsht,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_TBALLX1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_firxpl,		# deathsound
	10*FRACUNIT,		# speed
	6*FRACUNIT,		# radius
	8*FRACUNIT,		# height
	100,		# mass
	3,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_MISSILE|MF_DROPOFF|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_HEADSHOT
	-1,		# doomednum
	S_RBALL1,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_firsht,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_RBALLX1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_firxpl,		# deathsound
	10*FRACUNIT,		# speed
	6*FRACUNIT,		# radius
	8*FRACUNIT,		# height
	100,		# mass
	5,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_MISSILE|MF_DROPOFF|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_ROCKET
	-1,		# doomednum
	S_ROCKET,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_rlaunc,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_EXPLODE1,		# deathstate
	S_NULL,		# xdeathstate
	sfx_barexp,		# deathsound
	20*FRACUNIT,		# speed
	11*FRACUNIT,		# radius
	8*FRACUNIT,		# height
	100,		# mass
	20,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_MISSILE|MF_DROPOFF|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_PLASMA
	-1,		# doomednum
	S_PLASBALL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_plasma,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_PLASEXP,		# deathstate
	S_NULL,		# xdeathstate
	sfx_firxpl,		# deathsound
	25*FRACUNIT,		# speed
	13*FRACUNIT,		# radius
	8*FRACUNIT,		# height
	100,		# mass
	5,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_MISSILE|MF_DROPOFF|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_BFG
	-1,		# doomednum
	S_BFGSHOT,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	0,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_BFGLAND,		# deathstate
	S_NULL,		# xdeathstate
	sfx_rxplod,		# deathsound
	25*FRACUNIT,		# speed
	13*FRACUNIT,		# radius
	8*FRACUNIT,		# height
	100,		# mass
	100,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_MISSILE|MF_DROPOFF|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_ARACHPLAZ
	-1,		# doomednum
	S_ARACH_PLAZ,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_plasma,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_ARACH_PLEX,		# deathstate
	S_NULL,		# xdeathstate
	sfx_firxpl,		# deathsound
	25*FRACUNIT,		# speed
	13*FRACUNIT,		# radius
	8*FRACUNIT,		# height
	100,		# mass
	5,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_MISSILE|MF_DROPOFF|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_PUFF
	-1,		# doomednum
	S_PUFF1,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_BLOOD
	-1,		# doomednum
	S_BLOOD1,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_TFOG
	-1,		# doomednum
	S_TFOG,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_IFOG
	-1,		# doomednum
	S_IFOG,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_TELEPORTMAN
	14,		# doomednum
	S_NULL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_NOSECTOR,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_EXTRABFG
	-1,		# doomednum
	S_BFGEXP,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC0
	2018,		# doomednum
	S_ARM1,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC1
	2019,		# doomednum
	S_ARM2,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC2
	2014,		# doomednum
	S_BON1,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL|MF_COUNTITEM,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC3
	2015,		# doomednum
	S_BON2,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL|MF_COUNTITEM,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC4
	5,		# doomednum
	S_BKEY,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL|MF_NOTDMATCH,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC5
	13,		# doomednum
	S_RKEY,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL|MF_NOTDMATCH,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC6
	6,		# doomednum
	S_YKEY,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL|MF_NOTDMATCH,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC7
	39,		# doomednum
	S_YSKULL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL|MF_NOTDMATCH,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC8
	38,		# doomednum
	S_RSKULL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL|MF_NOTDMATCH,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC9
	40,		# doomednum
	S_BSKULL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL|MF_NOTDMATCH,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC10
	2011,		# doomednum
	S_STIM,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC11
	2012,		# doomednum
	S_MEDI,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC12
	2013,		# doomednum
	S_SOUL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL|MF_COUNTITEM,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_INV
	2022,		# doomednum
	S_PINV,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL|MF_COUNTITEM,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC13
	2023,		# doomednum
	S_PSTR,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL|MF_COUNTITEM,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_INS
	2024,		# doomednum
	S_PINS,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL|MF_COUNTITEM,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC14
	2025,		# doomednum
	S_SUIT,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC15
	2026,		# doomednum
	S_PMAP,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL|MF_COUNTITEM,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC16
	2045,		# doomednum
	S_PVIS,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL|MF_COUNTITEM,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MEGA
	83,		# doomednum
	S_MEGA,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL|MF_COUNTITEM,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_CLIP
	2007,		# doomednum
	S_CLIP,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC17
	2048,		# doomednum
	S_AMMO,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC18
	2010,		# doomednum
	S_ROCK,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC19
	2046,		# doomednum
	S_BROK,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC20
	2047,		# doomednum
	S_CELL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC21
	17,		# doomednum
	S_CELP,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC22
	2008,		# doomednum
	S_SHEL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC23
	2049,		# doomednum
	S_SBOX,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC24
	8,		# doomednum
	S_BPAK,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC25
	2006,		# doomednum
	S_BFUG,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_CHAINGUN
	2002,		# doomednum
	S_MGUN,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC26
	2005,		# doomednum
	S_CSAW,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC27
	2003,		# doomednum
	S_LAUN,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC28
	2004,		# doomednum
	S_PLAS,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_SHOTGUN
	2001,		# doomednum
	S_SHOT,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_SUPERSHOTGUN
	82,		# doomednum
	S_SHOT2,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPECIAL,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC29
	85,		# doomednum
	S_TECHLAMP,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC30
	86,		# doomednum
	S_TECH2LAMP,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC31
	2028,		# doomednum
	S_COLU,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC32
	30,		# doomednum
	S_TALLGRNCOL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC33
	31,		# doomednum
	S_SHRTGRNCOL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC34
	32,		# doomednum
	S_TALLREDCOL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC35
	33,		# doomednum
	S_SHRTREDCOL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC36
	37,		# doomednum
	S_SKULLCOL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC37
	36,		# doomednum
	S_HEARTCOL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC38
	41,		# doomednum
	S_EVILEYE,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC39
	42,		# doomednum
	S_FLOATSKULL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC40
	43,		# doomednum
	S_TORCHTREE,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC41
	44,		# doomednum
	S_BLUETORCH,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC42
	45,		# doomednum
	S_GREENTORCH,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC43
	46,		# doomednum
	S_REDTORCH,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC44
	55,		# doomednum
	S_BTORCHSHRT,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC45
	56,		# doomednum
	S_GTORCHSHRT,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC46
	57,		# doomednum
	S_RTORCHSHRT,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC47
	47,		# doomednum
	S_STALAGTITE,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC48
	48,		# doomednum
	S_TECHPILLAR,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC49
	34,		# doomednum
	S_CANDLESTIK,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	0,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC50
	35,		# doomednum
	S_CANDELABRA,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC51
	49,		# doomednum
	S_BLOODYTWITCH,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	68*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID|MF_SPAWNCEILING|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC52
	50,		# doomednum
	S_MEAT2,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	84*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID|MF_SPAWNCEILING|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC53
	51,		# doomednum
	S_MEAT3,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	84*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID|MF_SPAWNCEILING|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC54
	52,		# doomednum
	S_MEAT4,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	68*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID|MF_SPAWNCEILING|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC55
	53,		# doomednum
	S_MEAT5,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	52*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID|MF_SPAWNCEILING|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC56
	59,		# doomednum
	S_MEAT2,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	84*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPAWNCEILING|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC57
	60,		# doomednum
	S_MEAT4,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	68*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPAWNCEILING|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC58
	61,		# doomednum
	S_MEAT3,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	52*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPAWNCEILING|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC59
	62,		# doomednum
	S_MEAT5,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	52*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPAWNCEILING|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC60
	63,		# doomednum
	S_BLOODYTWITCH,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	68*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SPAWNCEILING|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC61
	22,		# doomednum
	S_HEAD_DIE6,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	0,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC62
	15,		# doomednum
	S_PLAY_DIE7,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	0,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC63
	18,		# doomednum
	S_POSS_DIE5,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	0,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC64
	21,		# doomednum
	S_SARG_DIE6,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	0,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC65
	23,		# doomednum
	S_SKULL_DIE6,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	0,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC66
	20,		# doomednum
	S_TROO_DIE5,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	0,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC67
	19,		# doomednum
	S_SPOS_DIE5,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	0,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC68
	10,		# doomednum
	S_PLAY_XDIE9,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	0,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC69
	12,		# doomednum
	S_PLAY_XDIE9,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	0,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC70
	28,		# doomednum
	S_HEADSONSTICK,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC71
	24,		# doomednum
	S_GIBS,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	0,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC72
	27,		# doomednum
	S_HEADONASTICK,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC73
	29,		# doomednum
	S_HEADCANDLES,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC74
	25,		# doomednum
	S_DEADSTICK,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC75
	26,		# doomednum
	S_LIVESTICK,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC76
	54,		# doomednum
	S_BIGTREE,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	32*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC77
	70,		# doomednum
	S_BBAR1,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC78
	73,		# doomednum
	S_HANGNOGUTS,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	88*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID|MF_SPAWNCEILING|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC79
	74,		# doomednum
	S_HANGBNOBRAIN,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	88*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID|MF_SPAWNCEILING|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC80
	75,		# doomednum
	S_HANGTLOOKDN,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	64*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID|MF_SPAWNCEILING|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC81
	76,		# doomednum
	S_HANGTSKULL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	64*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID|MF_SPAWNCEILING|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC82
	77,		# doomednum
	S_HANGTLOOKUP,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	64*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID|MF_SPAWNCEILING|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC83
	78,		# doomednum
	S_HANGTNOBRAIN,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	16*FRACUNIT,		# radius
	64*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_SOLID|MF_SPAWNCEILING|MF_NOGRAVITY,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC84
	79,		# doomednum
	S_COLONGIBS,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC85
	80,		# doomednum
	S_SMALLPOOL,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP,		# flags
	S_NULL		# raisestate
    ),

    Mobj(		# MT_MISC86
	81,		# doomednum
	S_BRAINSTEM,		# spawnstate
	1000,		# spawnhealth
	S_NULL,		# seestate
	sfx_None,		# seesound
	8,		# reactiontime
	sfx_None,		# attacksound
	S_NULL,		# painstate
	0,		# painchance
	sfx_None,		# painsound
	S_NULL,		# meleestate
	S_NULL,		# missilestate
	S_NULL,		# deathstate
	S_NULL,		# xdeathstate
	sfx_None,		# deathsound
	0,		# speed
	20*FRACUNIT,		# radius
	16*FRACUNIT,		# height
	100,		# mass
	0,		# damage
	sfx_None,		# activesound
	MF_NOBLOCKMAP,		# flags
	S_NULL		# raisestate
    )
]

