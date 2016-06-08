
from actions import *
from sprites import *

class State(object):
    def __init__(self, sprite, frame, tics, action, nextstate):
        self.sprite = sprite
        self.frame = frame
        self.tics = tics
        self.action = action
        self.nextstate = nextstate
        self.misc1 = 0
        self.misc2 = 0


STATE_NAMES = [
    "S_NULL",
    "S_LIGHTDONE",
    "S_PUNCH",
    "S_PUNCHDOWN",
    "S_PUNCHUP",
    "S_PUNCH1",
    "S_PUNCH2",
    "S_PUNCH3",
    "S_PUNCH4",
    "S_PUNCH5",
    "S_PISTOL",
    "S_PISTOLDOWN",
    "S_PISTOLUP",
    "S_PISTOL1",
    "S_PISTOL2",
    "S_PISTOL3",
    "S_PISTOL4",
    "S_PISTOLFLASH",
    "S_SGUN",
    "S_SGUNDOWN",
    "S_SGUNUP",
    "S_SGUN1",
    "S_SGUN2",
    "S_SGUN3",
    "S_SGUN4",
    "S_SGUN5",
    "S_SGUN6",
    "S_SGUN7",
    "S_SGUN8",
    "S_SGUN9",
    "S_SGUNFLASH1",
    "S_SGUNFLASH2",
    "S_DSGUN",
    "S_DSGUNDOWN",
    "S_DSGUNUP",
    "S_DSGUN1",
    "S_DSGUN2",
    "S_DSGUN3",
    "S_DSGUN4",
    "S_DSGUN5",
    "S_DSGUN6",
    "S_DSGUN7",
    "S_DSGUN8",
    "S_DSGUN9",
    "S_DSGUN10",
    "S_DSNR1",
    "S_DSNR2",
    "S_DSGUNFLASH1",
    "S_DSGUNFLASH2",
    "S_CHAIN",
    "S_CHAINDOWN",
    "S_CHAINUP",
    "S_CHAIN1",
    "S_CHAIN2",
    "S_CHAIN3",
    "S_CHAINFLASH1",
    "S_CHAINFLASH2",
    "S_MISSILE",
    "S_MISSILEDOWN",
    "S_MISSILEUP",
    "S_MISSILE1",
    "S_MISSILE2",
    "S_MISSILE3",
    "S_MISSILEFLASH1",
    "S_MISSILEFLASH2",
    "S_MISSILEFLASH3",
    "S_MISSILEFLASH4",
    "S_SAW",
    "S_SAWB",
    "S_SAWDOWN",
    "S_SAWUP",
    "S_SAW1",
    "S_SAW2",
    "S_SAW3",
    "S_PLASMA",
    "S_PLASMADOWN",
    "S_PLASMAUP",
    "S_PLASMA1",
    "S_PLASMA2",
    "S_PLASMAFLASH1",
    "S_PLASMAFLASH2",
    "S_BFG",
    "S_BFGDOWN",
    "S_BFGUP",
    "S_BFG1",
    "S_BFG2",
    "S_BFG3",
    "S_BFG4",
    "S_BFGFLASH1",
    "S_BFGFLASH2",
    "S_BLOOD1",
    "S_BLOOD2",
    "S_BLOOD3",
    "S_PUFF1",
    "S_PUFF2",
    "S_PUFF3",
    "S_PUFF4",
    "S_TBALL1",
    "S_TBALL2",
    "S_TBALLX1",
    "S_TBALLX2",
    "S_TBALLX3",
    "S_RBALL1",
    "S_RBALL2",
    "S_RBALLX1",
    "S_RBALLX2",
    "S_RBALLX3",
    "S_PLASBALL",
    "S_PLASBALL2",
    "S_PLASEXP",
    "S_PLASEXP2",
    "S_PLASEXP3",
    "S_PLASEXP4",
    "S_PLASEXP5",
    "S_ROCKET",
    "S_BFGSHOT",
    "S_BFGSHOT2",
    "S_BFGLAND",
    "S_BFGLAND2",
    "S_BFGLAND3",
    "S_BFGLAND4",
    "S_BFGLAND5",
    "S_BFGLAND6",
    "S_BFGEXP",
    "S_BFGEXP2",
    "S_BFGEXP3",
    "S_BFGEXP4",
    "S_EXPLODE1",
    "S_EXPLODE2",
    "S_EXPLODE3",
    "S_TFOG",
    "S_TFOG01",
    "S_TFOG02",
    "S_TFOG2",
    "S_TFOG3",
    "S_TFOG4",
    "S_TFOG5",
    "S_TFOG6",
    "S_TFOG7",
    "S_TFOG8",
    "S_TFOG9",
    "S_TFOG10",
    "S_IFOG",
    "S_IFOG01",
    "S_IFOG02",
    "S_IFOG2",
    "S_IFOG3",
    "S_IFOG4",
    "S_IFOG5",
    "S_PLAY",
    "S_PLAY_RUN1",
    "S_PLAY_RUN2",
    "S_PLAY_RUN3",
    "S_PLAY_RUN4",
    "S_PLAY_ATK1",
    "S_PLAY_ATK2",
    "S_PLAY_PAIN",
    "S_PLAY_PAIN2",
    "S_PLAY_DIE1",
    "S_PLAY_DIE2",
    "S_PLAY_DIE3",
    "S_PLAY_DIE4",
    "S_PLAY_DIE5",
    "S_PLAY_DIE6",
    "S_PLAY_DIE7",
    "S_PLAY_XDIE1",
    "S_PLAY_XDIE2",
    "S_PLAY_XDIE3",
    "S_PLAY_XDIE4",
    "S_PLAY_XDIE5",
    "S_PLAY_XDIE6",
    "S_PLAY_XDIE7",
    "S_PLAY_XDIE8",
    "S_PLAY_XDIE9",
    "S_POSS_STND",
    "S_POSS_STND2",
    "S_POSS_RUN1",
    "S_POSS_RUN2",
    "S_POSS_RUN3",
    "S_POSS_RUN4",
    "S_POSS_RUN5",
    "S_POSS_RUN6",
    "S_POSS_RUN7",
    "S_POSS_RUN8",
    "S_POSS_ATK1",
    "S_POSS_ATK2",
    "S_POSS_ATK3",
    "S_POSS_PAIN",
    "S_POSS_PAIN2",
    "S_POSS_DIE1",
    "S_POSS_DIE2",
    "S_POSS_DIE3",
    "S_POSS_DIE4",
    "S_POSS_DIE5",
    "S_POSS_XDIE1",
    "S_POSS_XDIE2",
    "S_POSS_XDIE3",
    "S_POSS_XDIE4",
    "S_POSS_XDIE5",
    "S_POSS_XDIE6",
    "S_POSS_XDIE7",
    "S_POSS_XDIE8",
    "S_POSS_XDIE9",
    "S_POSS_RAISE1",
    "S_POSS_RAISE2",
    "S_POSS_RAISE3",
    "S_POSS_RAISE4",
    "S_SPOS_STND",
    "S_SPOS_STND2",
    "S_SPOS_RUN1",
    "S_SPOS_RUN2",
    "S_SPOS_RUN3",
    "S_SPOS_RUN4",
    "S_SPOS_RUN5",
    "S_SPOS_RUN6",
    "S_SPOS_RUN7",
    "S_SPOS_RUN8",
    "S_SPOS_ATK1",
    "S_SPOS_ATK2",
    "S_SPOS_ATK3",
    "S_SPOS_PAIN",
    "S_SPOS_PAIN2",
    "S_SPOS_DIE1",
    "S_SPOS_DIE2",
    "S_SPOS_DIE3",
    "S_SPOS_DIE4",
    "S_SPOS_DIE5",
    "S_SPOS_XDIE1",
    "S_SPOS_XDIE2",
    "S_SPOS_XDIE3",
    "S_SPOS_XDIE4",
    "S_SPOS_XDIE5",
    "S_SPOS_XDIE6",
    "S_SPOS_XDIE7",
    "S_SPOS_XDIE8",
    "S_SPOS_XDIE9",
    "S_SPOS_RAISE1",
    "S_SPOS_RAISE2",
    "S_SPOS_RAISE3",
    "S_SPOS_RAISE4",
    "S_SPOS_RAISE5",
    "S_VILE_STND",
    "S_VILE_STND2",
    "S_VILE_RUN1",
    "S_VILE_RUN2",
    "S_VILE_RUN3",
    "S_VILE_RUN4",
    "S_VILE_RUN5",
    "S_VILE_RUN6",
    "S_VILE_RUN7",
    "S_VILE_RUN8",
    "S_VILE_RUN9",
    "S_VILE_RUN10",
    "S_VILE_RUN11",
    "S_VILE_RUN12",
    "S_VILE_ATK1",
    "S_VILE_ATK2",
    "S_VILE_ATK3",
    "S_VILE_ATK4",
    "S_VILE_ATK5",
    "S_VILE_ATK6",
    "S_VILE_ATK7",
    "S_VILE_ATK8",
    "S_VILE_ATK9",
    "S_VILE_ATK10",
    "S_VILE_ATK11",
    "S_VILE_HEAL1",
    "S_VILE_HEAL2",
    "S_VILE_HEAL3",
    "S_VILE_PAIN",
    "S_VILE_PAIN2",
    "S_VILE_DIE1",
    "S_VILE_DIE2",
    "S_VILE_DIE3",
    "S_VILE_DIE4",
    "S_VILE_DIE5",
    "S_VILE_DIE6",
    "S_VILE_DIE7",
    "S_VILE_DIE8",
    "S_VILE_DIE9",
    "S_VILE_DIE10",
    "S_FIRE1",
    "S_FIRE2",
    "S_FIRE3",
    "S_FIRE4",
    "S_FIRE5",
    "S_FIRE6",
    "S_FIRE7",
    "S_FIRE8",
    "S_FIRE9",
    "S_FIRE10",
    "S_FIRE11",
    "S_FIRE12",
    "S_FIRE13",
    "S_FIRE14",
    "S_FIRE15",
    "S_FIRE16",
    "S_FIRE17",
    "S_FIRE18",
    "S_FIRE19",
    "S_FIRE20",
    "S_FIRE21",
    "S_FIRE22",
    "S_FIRE23",
    "S_FIRE24",
    "S_FIRE25",
    "S_FIRE26",
    "S_FIRE27",
    "S_FIRE28",
    "S_FIRE29",
    "S_FIRE30",
    "S_SMOKE1",
    "S_SMOKE2",
    "S_SMOKE3",
    "S_SMOKE4",
    "S_SMOKE5",
    "S_TRACER",
    "S_TRACER2",
    "S_TRACEEXP1",
    "S_TRACEEXP2",
    "S_TRACEEXP3",
    "S_SKEL_STND",
    "S_SKEL_STND2",
    "S_SKEL_RUN1",
    "S_SKEL_RUN2",
    "S_SKEL_RUN3",
    "S_SKEL_RUN4",
    "S_SKEL_RUN5",
    "S_SKEL_RUN6",
    "S_SKEL_RUN7",
    "S_SKEL_RUN8",
    "S_SKEL_RUN9",
    "S_SKEL_RUN10",
    "S_SKEL_RUN11",
    "S_SKEL_RUN12",
    "S_SKEL_FIST1",
    "S_SKEL_FIST2",
    "S_SKEL_FIST3",
    "S_SKEL_FIST4",
    "S_SKEL_MISS1",
    "S_SKEL_MISS2",
    "S_SKEL_MISS3",
    "S_SKEL_MISS4",
    "S_SKEL_PAIN",
    "S_SKEL_PAIN2",
    "S_SKEL_DIE1",
    "S_SKEL_DIE2",
    "S_SKEL_DIE3",
    "S_SKEL_DIE4",
    "S_SKEL_DIE5",
    "S_SKEL_DIE6",
    "S_SKEL_RAISE1",
    "S_SKEL_RAISE2",
    "S_SKEL_RAISE3",
    "S_SKEL_RAISE4",
    "S_SKEL_RAISE5",
    "S_SKEL_RAISE6",
    "S_FATSHOT1",
    "S_FATSHOT2",
    "S_FATSHOTX1",
    "S_FATSHOTX2",
    "S_FATSHOTX3",
    "S_FATT_STND",
    "S_FATT_STND2",
    "S_FATT_RUN1",
    "S_FATT_RUN2",
    "S_FATT_RUN3",
    "S_FATT_RUN4",
    "S_FATT_RUN5",
    "S_FATT_RUN6",
    "S_FATT_RUN7",
    "S_FATT_RUN8",
    "S_FATT_RUN9",
    "S_FATT_RUN10",
    "S_FATT_RUN11",
    "S_FATT_RUN12",
    "S_FATT_ATK1",
    "S_FATT_ATK2",
    "S_FATT_ATK3",
    "S_FATT_ATK4",
    "S_FATT_ATK5",
    "S_FATT_ATK6",
    "S_FATT_ATK7",
    "S_FATT_ATK8",
    "S_FATT_ATK9",
    "S_FATT_ATK10",
    "S_FATT_PAIN",
    "S_FATT_PAIN2",
    "S_FATT_DIE1",
    "S_FATT_DIE2",
    "S_FATT_DIE3",
    "S_FATT_DIE4",
    "S_FATT_DIE5",
    "S_FATT_DIE6",
    "S_FATT_DIE7",
    "S_FATT_DIE8",
    "S_FATT_DIE9",
    "S_FATT_DIE10",
    "S_FATT_RAISE1",
    "S_FATT_RAISE2",
    "S_FATT_RAISE3",
    "S_FATT_RAISE4",
    "S_FATT_RAISE5",
    "S_FATT_RAISE6",
    "S_FATT_RAISE7",
    "S_FATT_RAISE8",
    "S_CPOS_STND",
    "S_CPOS_STND2",
    "S_CPOS_RUN1",
    "S_CPOS_RUN2",
    "S_CPOS_RUN3",
    "S_CPOS_RUN4",
    "S_CPOS_RUN5",
    "S_CPOS_RUN6",
    "S_CPOS_RUN7",
    "S_CPOS_RUN8",
    "S_CPOS_ATK1",
    "S_CPOS_ATK2",
    "S_CPOS_ATK3",
    "S_CPOS_ATK4",
    "S_CPOS_PAIN",
    "S_CPOS_PAIN2",
    "S_CPOS_DIE1",
    "S_CPOS_DIE2",
    "S_CPOS_DIE3",
    "S_CPOS_DIE4",
    "S_CPOS_DIE5",
    "S_CPOS_DIE6",
    "S_CPOS_DIE7",
    "S_CPOS_XDIE1",
    "S_CPOS_XDIE2",
    "S_CPOS_XDIE3",
    "S_CPOS_XDIE4",
    "S_CPOS_XDIE5",
    "S_CPOS_XDIE6",
    "S_CPOS_RAISE1",
    "S_CPOS_RAISE2",
    "S_CPOS_RAISE3",
    "S_CPOS_RAISE4",
    "S_CPOS_RAISE5",
    "S_CPOS_RAISE6",
    "S_CPOS_RAISE7",
    "S_TROO_STND",
    "S_TROO_STND2",
    "S_TROO_RUN1",
    "S_TROO_RUN2",
    "S_TROO_RUN3",
    "S_TROO_RUN4",
    "S_TROO_RUN5",
    "S_TROO_RUN6",
    "S_TROO_RUN7",
    "S_TROO_RUN8",
    "S_TROO_ATK1",
    "S_TROO_ATK2",
    "S_TROO_ATK3",
    "S_TROO_PAIN",
    "S_TROO_PAIN2",
    "S_TROO_DIE1",
    "S_TROO_DIE2",
    "S_TROO_DIE3",
    "S_TROO_DIE4",
    "S_TROO_DIE5",
    "S_TROO_XDIE1",
    "S_TROO_XDIE2",
    "S_TROO_XDIE3",
    "S_TROO_XDIE4",
    "S_TROO_XDIE5",
    "S_TROO_XDIE6",
    "S_TROO_XDIE7",
    "S_TROO_XDIE8",
    "S_TROO_RAISE1",
    "S_TROO_RAISE2",
    "S_TROO_RAISE3",
    "S_TROO_RAISE4",
    "S_TROO_RAISE5",
    "S_SARG_STND",
    "S_SARG_STND2",
    "S_SARG_RUN1",
    "S_SARG_RUN2",
    "S_SARG_RUN3",
    "S_SARG_RUN4",
    "S_SARG_RUN5",
    "S_SARG_RUN6",
    "S_SARG_RUN7",
    "S_SARG_RUN8",
    "S_SARG_ATK1",
    "S_SARG_ATK2",
    "S_SARG_ATK3",
    "S_SARG_PAIN",
    "S_SARG_PAIN2",
    "S_SARG_DIE1",
    "S_SARG_DIE2",
    "S_SARG_DIE3",
    "S_SARG_DIE4",
    "S_SARG_DIE5",
    "S_SARG_DIE6",
    "S_SARG_RAISE1",
    "S_SARG_RAISE2",
    "S_SARG_RAISE3",
    "S_SARG_RAISE4",
    "S_SARG_RAISE5",
    "S_SARG_RAISE6",
    "S_HEAD_STND",
    "S_HEAD_RUN1",
    "S_HEAD_ATK1",
    "S_HEAD_ATK2",
    "S_HEAD_ATK3",
    "S_HEAD_PAIN",
    "S_HEAD_PAIN2",
    "S_HEAD_PAIN3",
    "S_HEAD_DIE1",
    "S_HEAD_DIE2",
    "S_HEAD_DIE3",
    "S_HEAD_DIE4",
    "S_HEAD_DIE5",
    "S_HEAD_DIE6",
    "S_HEAD_RAISE1",
    "S_HEAD_RAISE2",
    "S_HEAD_RAISE3",
    "S_HEAD_RAISE4",
    "S_HEAD_RAISE5",
    "S_HEAD_RAISE6",
    "S_BRBALL1",
    "S_BRBALL2",
    "S_BRBALLX1",
    "S_BRBALLX2",
    "S_BRBALLX3",
    "S_BOSS_STND",
    "S_BOSS_STND2",
    "S_BOSS_RUN1",
    "S_BOSS_RUN2",
    "S_BOSS_RUN3",
    "S_BOSS_RUN4",
    "S_BOSS_RUN5",
    "S_BOSS_RUN6",
    "S_BOSS_RUN7",
    "S_BOSS_RUN8",
    "S_BOSS_ATK1",
    "S_BOSS_ATK2",
    "S_BOSS_ATK3",
    "S_BOSS_PAIN",
    "S_BOSS_PAIN2",
    "S_BOSS_DIE1",
    "S_BOSS_DIE2",
    "S_BOSS_DIE3",
    "S_BOSS_DIE4",
    "S_BOSS_DIE5",
    "S_BOSS_DIE6",
    "S_BOSS_DIE7",
    "S_BOSS_RAISE1",
    "S_BOSS_RAISE2",
    "S_BOSS_RAISE3",
    "S_BOSS_RAISE4",
    "S_BOSS_RAISE5",
    "S_BOSS_RAISE6",
    "S_BOSS_RAISE7",
    "S_BOS2_STND",
    "S_BOS2_STND2",
    "S_BOS2_RUN1",
    "S_BOS2_RUN2",
    "S_BOS2_RUN3",
    "S_BOS2_RUN4",
    "S_BOS2_RUN5",
    "S_BOS2_RUN6",
    "S_BOS2_RUN7",
    "S_BOS2_RUN8",
    "S_BOS2_ATK1",
    "S_BOS2_ATK2",
    "S_BOS2_ATK3",
    "S_BOS2_PAIN",
    "S_BOS2_PAIN2",
    "S_BOS2_DIE1",
    "S_BOS2_DIE2",
    "S_BOS2_DIE3",
    "S_BOS2_DIE4",
    "S_BOS2_DIE5",
    "S_BOS2_DIE6",
    "S_BOS2_DIE7",
    "S_BOS2_RAISE1",
    "S_BOS2_RAISE2",
    "S_BOS2_RAISE3",
    "S_BOS2_RAISE4",
    "S_BOS2_RAISE5",
    "S_BOS2_RAISE6",
    "S_BOS2_RAISE7",
    "S_SKULL_STND",
    "S_SKULL_STND2",
    "S_SKULL_RUN1",
    "S_SKULL_RUN2",
    "S_SKULL_ATK1",
    "S_SKULL_ATK2",
    "S_SKULL_ATK3",
    "S_SKULL_ATK4",
    "S_SKULL_PAIN",
    "S_SKULL_PAIN2",
    "S_SKULL_DIE1",
    "S_SKULL_DIE2",
    "S_SKULL_DIE3",
    "S_SKULL_DIE4",
    "S_SKULL_DIE5",
    "S_SKULL_DIE6",
    "S_SPID_STND",
    "S_SPID_STND2",
    "S_SPID_RUN1",
    "S_SPID_RUN2",
    "S_SPID_RUN3",
    "S_SPID_RUN4",
    "S_SPID_RUN5",
    "S_SPID_RUN6",
    "S_SPID_RUN7",
    "S_SPID_RUN8",
    "S_SPID_RUN9",
    "S_SPID_RUN10",
    "S_SPID_RUN11",
    "S_SPID_RUN12",
    "S_SPID_ATK1",
    "S_SPID_ATK2",
    "S_SPID_ATK3",
    "S_SPID_ATK4",
    "S_SPID_PAIN",
    "S_SPID_PAIN2",
    "S_SPID_DIE1",
    "S_SPID_DIE2",
    "S_SPID_DIE3",
    "S_SPID_DIE4",
    "S_SPID_DIE5",
    "S_SPID_DIE6",
    "S_SPID_DIE7",
    "S_SPID_DIE8",
    "S_SPID_DIE9",
    "S_SPID_DIE10",
    "S_SPID_DIE11",
    "S_BSPI_STND",
    "S_BSPI_STND2",
    "S_BSPI_SIGHT",
    "S_BSPI_RUN1",
    "S_BSPI_RUN2",
    "S_BSPI_RUN3",
    "S_BSPI_RUN4",
    "S_BSPI_RUN5",
    "S_BSPI_RUN6",
    "S_BSPI_RUN7",
    "S_BSPI_RUN8",
    "S_BSPI_RUN9",
    "S_BSPI_RUN10",
    "S_BSPI_RUN11",
    "S_BSPI_RUN12",
    "S_BSPI_ATK1",
    "S_BSPI_ATK2",
    "S_BSPI_ATK3",
    "S_BSPI_ATK4",
    "S_BSPI_PAIN",
    "S_BSPI_PAIN2",
    "S_BSPI_DIE1",
    "S_BSPI_DIE2",
    "S_BSPI_DIE3",
    "S_BSPI_DIE4",
    "S_BSPI_DIE5",
    "S_BSPI_DIE6",
    "S_BSPI_DIE7",
    "S_BSPI_RAISE1",
    "S_BSPI_RAISE2",
    "S_BSPI_RAISE3",
    "S_BSPI_RAISE4",
    "S_BSPI_RAISE5",
    "S_BSPI_RAISE6",
    "S_BSPI_RAISE7",
    "S_ARACH_PLAZ",
    "S_ARACH_PLAZ2",
    "S_ARACH_PLEX",
    "S_ARACH_PLEX2",
    "S_ARACH_PLEX3",
    "S_ARACH_PLEX4",
    "S_ARACH_PLEX5",
    "S_CYBER_STND",
    "S_CYBER_STND2",
    "S_CYBER_RUN1",
    "S_CYBER_RUN2",
    "S_CYBER_RUN3",
    "S_CYBER_RUN4",
    "S_CYBER_RUN5",
    "S_CYBER_RUN6",
    "S_CYBER_RUN7",
    "S_CYBER_RUN8",
    "S_CYBER_ATK1",
    "S_CYBER_ATK2",
    "S_CYBER_ATK3",
    "S_CYBER_ATK4",
    "S_CYBER_ATK5",
    "S_CYBER_ATK6",
    "S_CYBER_PAIN",
    "S_CYBER_DIE1",
    "S_CYBER_DIE2",
    "S_CYBER_DIE3",
    "S_CYBER_DIE4",
    "S_CYBER_DIE5",
    "S_CYBER_DIE6",
    "S_CYBER_DIE7",
    "S_CYBER_DIE8",
    "S_CYBER_DIE9",
    "S_CYBER_DIE10",
    "S_PAIN_STND",
    "S_PAIN_RUN1",
    "S_PAIN_RUN2",
    "S_PAIN_RUN3",
    "S_PAIN_RUN4",
    "S_PAIN_RUN5",
    "S_PAIN_RUN6",
    "S_PAIN_ATK1",
    "S_PAIN_ATK2",
    "S_PAIN_ATK3",
    "S_PAIN_ATK4",
    "S_PAIN_PAIN",
    "S_PAIN_PAIN2",
    "S_PAIN_DIE1",
    "S_PAIN_DIE2",
    "S_PAIN_DIE3",
    "S_PAIN_DIE4",
    "S_PAIN_DIE5",
    "S_PAIN_DIE6",
    "S_PAIN_RAISE1",
    "S_PAIN_RAISE2",
    "S_PAIN_RAISE3",
    "S_PAIN_RAISE4",
    "S_PAIN_RAISE5",
    "S_PAIN_RAISE6",
    "S_SSWV_STND",
    "S_SSWV_STND2",
    "S_SSWV_RUN1",
    "S_SSWV_RUN2",
    "S_SSWV_RUN3",
    "S_SSWV_RUN4",
    "S_SSWV_RUN5",
    "S_SSWV_RUN6",
    "S_SSWV_RUN7",
    "S_SSWV_RUN8",
    "S_SSWV_ATK1",
    "S_SSWV_ATK2",
    "S_SSWV_ATK3",
    "S_SSWV_ATK4",
    "S_SSWV_ATK5",
    "S_SSWV_ATK6",
    "S_SSWV_PAIN",
    "S_SSWV_PAIN2",
    "S_SSWV_DIE1",
    "S_SSWV_DIE2",
    "S_SSWV_DIE3",
    "S_SSWV_DIE4",
    "S_SSWV_DIE5",
    "S_SSWV_XDIE1",
    "S_SSWV_XDIE2",
    "S_SSWV_XDIE3",
    "S_SSWV_XDIE4",
    "S_SSWV_XDIE5",
    "S_SSWV_XDIE6",
    "S_SSWV_XDIE7",
    "S_SSWV_XDIE8",
    "S_SSWV_XDIE9",
    "S_SSWV_RAISE1",
    "S_SSWV_RAISE2",
    "S_SSWV_RAISE3",
    "S_SSWV_RAISE4",
    "S_SSWV_RAISE5",
    "S_KEENSTND",
    "S_COMMKEEN",
    "S_COMMKEEN2",
    "S_COMMKEEN3",
    "S_COMMKEEN4",
    "S_COMMKEEN5",
    "S_COMMKEEN6",
    "S_COMMKEEN7",
    "S_COMMKEEN8",
    "S_COMMKEEN9",
    "S_COMMKEEN10",
    "S_COMMKEEN11",
    "S_COMMKEEN12",
    "S_KEENPAIN",
    "S_KEENPAIN2",
    "S_BRAIN",
    "S_BRAIN_PAIN",
    "S_BRAIN_DIE1",
    "S_BRAIN_DIE2",
    "S_BRAIN_DIE3",
    "S_BRAIN_DIE4",
    "S_BRAINEYE",
    "S_BRAINEYESEE",
    "S_BRAINEYE1",
    "S_SPAWN1",
    "S_SPAWN2",
    "S_SPAWN3",
    "S_SPAWN4",
    "S_SPAWNFIRE1",
    "S_SPAWNFIRE2",
    "S_SPAWNFIRE3",
    "S_SPAWNFIRE4",
    "S_SPAWNFIRE5",
    "S_SPAWNFIRE6",
    "S_SPAWNFIRE7",
    "S_SPAWNFIRE8",
    "S_BRAINEXPLODE1",
    "S_BRAINEXPLODE2",
    "S_BRAINEXPLODE3",
    "S_ARM1",
    "S_ARM1A",
    "S_ARM2",
    "S_ARM2A",
    "S_BAR1",
    "S_BAR2",
    "S_BEXP",
    "S_BEXP2",
    "S_BEXP3",
    "S_BEXP4",
    "S_BEXP5",
    "S_BBAR1",
    "S_BBAR2",
    "S_BBAR3",
    "S_BON1",
    "S_BON1A",
    "S_BON1B",
    "S_BON1C",
    "S_BON1D",
    "S_BON1E",
    "S_BON2",
    "S_BON2A",
    "S_BON2B",
    "S_BON2C",
    "S_BON2D",
    "S_BON2E",
    "S_BKEY",
    "S_BKEY2",
    "S_RKEY",
    "S_RKEY2",
    "S_YKEY",
    "S_YKEY2",
    "S_BSKULL",
    "S_BSKULL2",
    "S_RSKULL",
    "S_RSKULL2",
    "S_YSKULL",
    "S_YSKULL2",
    "S_STIM",
    "S_MEDI",
    "S_SOUL",
    "S_SOUL2",
    "S_SOUL3",
    "S_SOUL4",
    "S_SOUL5",
    "S_SOUL6",
    "S_PINV",
    "S_PINV2",
    "S_PINV3",
    "S_PINV4",
    "S_PSTR",
    "S_PINS",
    "S_PINS2",
    "S_PINS3",
    "S_PINS4",
    "S_MEGA",
    "S_MEGA2",
    "S_MEGA3",
    "S_MEGA4",
    "S_SUIT",
    "S_PMAP",
    "S_PMAP2",
    "S_PMAP3",
    "S_PMAP4",
    "S_PMAP5",
    "S_PMAP6",
    "S_PVIS",
    "S_PVIS2",
    "S_CLIP",
    "S_AMMO",
    "S_ROCK",
    "S_BROK",
    "S_CELL",
    "S_CELP",
    "S_SHEL",
    "S_SBOX",
    "S_BPAK",
    "S_BFUG",
    "S_MGUN",
    "S_CSAW",
    "S_LAUN",
    "S_PLAS",
    "S_SHOT",
    "S_SHOT2",
    "S_COLU",
    "S_STALAG",
    "S_BLOODYTWITCH",
    "S_BLOODYTWITCH2",
    "S_BLOODYTWITCH3",
    "S_BLOODYTWITCH4",
    "S_DEADTORSO",
    "S_DEADBOTTOM",
    "S_HEADSONSTICK",
    "S_GIBS",
    "S_HEADONASTICK",
    "S_HEADCANDLES",
    "S_HEADCANDLES2",
    "S_DEADSTICK",
    "S_LIVESTICK",
    "S_LIVESTICK2",
    "S_MEAT2",
    "S_MEAT3",
    "S_MEAT4",
    "S_MEAT5",
    "S_STALAGTITE",
    "S_TALLGRNCOL",
    "S_SHRTGRNCOL",
    "S_TALLREDCOL",
    "S_SHRTREDCOL",
    "S_CANDLESTIK",
    "S_CANDELABRA",
    "S_SKULLCOL",
    "S_TORCHTREE",
    "S_BIGTREE",
    "S_TECHPILLAR",
    "S_EVILEYE",
    "S_EVILEYE2",
    "S_EVILEYE3",
    "S_EVILEYE4",
    "S_FLOATSKULL",
    "S_FLOATSKULL2",
    "S_FLOATSKULL3",
    "S_HEARTCOL",
    "S_HEARTCOL2",
    "S_BLUETORCH",
    "S_BLUETORCH2",
    "S_BLUETORCH3",
    "S_BLUETORCH4",
    "S_GREENTORCH",
    "S_GREENTORCH2",
    "S_GREENTORCH3",
    "S_GREENTORCH4",
    "S_REDTORCH",
    "S_REDTORCH2",
    "S_REDTORCH3",
    "S_REDTORCH4",
    "S_BTORCHSHRT",
    "S_BTORCHSHRT2",
    "S_BTORCHSHRT3",
    "S_BTORCHSHRT4",
    "S_GTORCHSHRT",
    "S_GTORCHSHRT2",
    "S_GTORCHSHRT3",
    "S_GTORCHSHRT4",
    "S_RTORCHSHRT",
    "S_RTORCHSHRT2",
    "S_RTORCHSHRT3",
    "S_RTORCHSHRT4",
    "S_HANGNOGUTS",
    "S_HANGBNOBRAIN",
    "S_HANGTLOOKDN",
    "S_HANGTSKULL",
    "S_HANGTLOOKUP",
    "S_HANGTNOBRAIN",
    "S_COLONGIBS",
    "S_SMALLPOOL",
    "S_BRAINSTEM",
    "S_TECHLAMP",
    "S_TECHLAMP2",
    "S_TECHLAMP3",
    "S_TECHLAMP4",
    "S_TECH2LAMP",
    "S_TECH2LAMP2",
    "S_TECH2LAMP3",
    "S_TECH2LAMP4",
]

for i, name in enumerate(STATE_NAMES):
    globals()[name] = i


STATES = [
    State(SPR_TROO, 0, -1, None, S_NULL),  # S_NULL
    State(SPR_SHTG, 4, 0, A_Light0, S_NULL),  # S_LIGHTDONE
    State(SPR_PUNG, 0, 1, A_WeaponReady, S_PUNCH),  # S_PUNCH
    State(SPR_PUNG, 0, 1, A_Lower, S_PUNCHDOWN),  # S_PUNCHDOWN
    State(SPR_PUNG, 0, 1, A_Raise, S_PUNCHUP),  # S_PUNCHUP
    State(SPR_PUNG, 1, 4, None, S_PUNCH2),  # S_PUNCH1
    State(SPR_PUNG, 2, 4, A_Punch, S_PUNCH3),  # S_PUNCH2
    State(SPR_PUNG, 3, 5, None, S_PUNCH4),  # S_PUNCH3
    State(SPR_PUNG, 2, 4, None, S_PUNCH5),  # S_PUNCH4
    State(SPR_PUNG, 1, 5, A_ReFire, S_PUNCH),  # S_PUNCH5
    State(SPR_PISG, 0, 1, A_WeaponReady, S_PISTOL),  # S_PISTOL
    State(SPR_PISG, 0, 1, A_Lower, S_PISTOLDOWN),  # S_PISTOLDOWN
    State(SPR_PISG, 0, 1, A_Raise, S_PISTOLUP),  # S_PISTOLUP
    State(SPR_PISG, 0, 4, None, S_PISTOL2),  # S_PISTOL1
    State(SPR_PISG, 1, 6, A_FirePistol, S_PISTOL3),  # S_PISTOL2
    State(SPR_PISG, 2, 4, None, S_PISTOL4),  # S_PISTOL3
    State(SPR_PISG, 1, 5, A_ReFire, S_PISTOL),  # S_PISTOL4
    State(SPR_PISF, 32768, 7, A_Light1, S_LIGHTDONE),  # S_PISTOLFLASH
    State(SPR_SHTG, 0, 1, A_WeaponReady, S_SGUN),  # S_SGUN
    State(SPR_SHTG, 0, 1, A_Lower, S_SGUNDOWN),  # S_SGUNDOWN
    State(SPR_SHTG, 0, 1, A_Raise, S_SGUNUP),  # S_SGUNUP
    State(SPR_SHTG, 0, 3, None, S_SGUN2),  # S_SGUN1
    State(SPR_SHTG, 0, 7, A_FireShotgun, S_SGUN3),  # S_SGUN2
    State(SPR_SHTG, 1, 5, None, S_SGUN4),  # S_SGUN3
    State(SPR_SHTG, 2, 5, None, S_SGUN5),  # S_SGUN4
    State(SPR_SHTG, 3, 4, None, S_SGUN6),  # S_SGUN5
    State(SPR_SHTG, 2, 5, None, S_SGUN7),  # S_SGUN6
    State(SPR_SHTG, 1, 5, None, S_SGUN8),  # S_SGUN7
    State(SPR_SHTG, 0, 3, None, S_SGUN9),  # S_SGUN8
    State(SPR_SHTG, 0, 7, A_ReFire, S_SGUN),  # S_SGUN9
    State(SPR_SHTF, 32768, 4, A_Light1, S_SGUNFLASH2),  # S_SGUNFLASH1
    State(SPR_SHTF, 32769, 3, A_Light2, S_LIGHTDONE),  # S_SGUNFLASH2
    State(SPR_SHT2, 0, 1, A_WeaponReady, S_DSGUN),  # S_DSGUN
    State(SPR_SHT2, 0, 1, A_Lower, S_DSGUNDOWN),  # S_DSGUNDOWN
    State(SPR_SHT2, 0, 1, A_Raise, S_DSGUNUP),  # S_DSGUNUP
    State(SPR_SHT2, 0, 3, None, S_DSGUN2),  # S_DSGUN1
    State(SPR_SHT2, 0, 7, A_FireShotgun2, S_DSGUN3),  # S_DSGUN2
    State(SPR_SHT2, 1, 7, None, S_DSGUN4),  # S_DSGUN3
    State(SPR_SHT2, 2, 7, A_CheckReload, S_DSGUN5),  # S_DSGUN4
    State(SPR_SHT2, 3, 7, A_OpenShotgun2, S_DSGUN6),  # S_DSGUN5
    State(SPR_SHT2, 4, 7, None, S_DSGUN7),  # S_DSGUN6
    State(SPR_SHT2, 5, 7, A_LoadShotgun2, S_DSGUN8),  # S_DSGUN7
    State(SPR_SHT2, 6, 6, None, S_DSGUN9),  # S_DSGUN8
    State(SPR_SHT2, 7, 6, A_CloseShotgun2, S_DSGUN10),  # S_DSGUN9
    State(SPR_SHT2, 0, 5, A_ReFire, S_DSGUN),  # S_DSGUN10
    State(SPR_SHT2, 1, 7, None, S_DSNR2),  # S_DSNR1
    State(SPR_SHT2, 0, 3, None, S_DSGUNDOWN),  # S_DSNR2
    State(SPR_SHT2, 32776, 5, A_Light1, S_DSGUNFLASH2),  # S_DSGUNFLASH1
    State(SPR_SHT2, 32777, 4, A_Light2, S_LIGHTDONE),  # S_DSGUNFLASH2
    State(SPR_CHGG, 0, 1, A_WeaponReady, S_CHAIN),  # S_CHAIN
    State(SPR_CHGG, 0, 1, A_Lower, S_CHAINDOWN),  # S_CHAINDOWN
    State(SPR_CHGG, 0, 1, A_Raise, S_CHAINUP),  # S_CHAINUP
    State(SPR_CHGG, 0, 4, A_FireCGun, S_CHAIN2),  # S_CHAIN1
    State(SPR_CHGG, 1, 4, A_FireCGun, S_CHAIN3),  # S_CHAIN2
    State(SPR_CHGG, 1, 0, A_ReFire, S_CHAIN),  # S_CHAIN3
    State(SPR_CHGF, 32768, 5, A_Light1, S_LIGHTDONE),  # S_CHAINFLASH1
    State(SPR_CHGF, 32769, 5, A_Light2, S_LIGHTDONE),  # S_CHAINFLASH2
    State(SPR_MISG, 0, 1, A_WeaponReady, S_MISSILE),  # S_MISSILE
    State(SPR_MISG, 0, 1, A_Lower, S_MISSILEDOWN),  # S_MISSILEDOWN
    State(SPR_MISG, 0, 1, A_Raise, S_MISSILEUP),  # S_MISSILEUP
    State(SPR_MISG, 1, 8, A_GunFlash, S_MISSILE2),  # S_MISSILE1
    State(SPR_MISG, 1, 12, A_FireMissile, S_MISSILE3),  # S_MISSILE2
    State(SPR_MISG, 1, 0, A_ReFire, S_MISSILE),  # S_MISSILE3
    State(SPR_MISF, 32768, 3, A_Light1, S_MISSILEFLASH2),  # S_MISSILEFLASH1
    State(SPR_MISF, 32769, 4, None, S_MISSILEFLASH3),  # S_MISSILEFLASH2
    State(SPR_MISF, 32770, 4, A_Light2, S_MISSILEFLASH4),  # S_MISSILEFLASH3
    State(SPR_MISF, 32771, 4, A_Light2, S_LIGHTDONE),  # S_MISSILEFLASH4
    State(SPR_SAWG, 2, 4, A_WeaponReady, S_SAWB),  # S_SAW
    State(SPR_SAWG, 3, 4, A_WeaponReady, S_SAW),  # S_SAWB
    State(SPR_SAWG, 2, 1, A_Lower, S_SAWDOWN),  # S_SAWDOWN
    State(SPR_SAWG, 2, 1, A_Raise, S_SAWUP),  # S_SAWUP
    State(SPR_SAWG, 0, 4, A_Saw, S_SAW2),  # S_SAW1
    State(SPR_SAWG, 1, 4, A_Saw, S_SAW3),  # S_SAW2
    State(SPR_SAWG, 1, 0, A_ReFire, S_SAW),  # S_SAW3
    State(SPR_PLSG, 0, 1, A_WeaponReady, S_PLASMA),  # S_PLASMA
    State(SPR_PLSG, 0, 1, A_Lower, S_PLASMADOWN),  # S_PLASMADOWN
    State(SPR_PLSG, 0, 1, A_Raise, S_PLASMAUP),  # S_PLASMAUP
    State(SPR_PLSG, 0, 3, A_FirePlasma, S_PLASMA2),  # S_PLASMA1
    State(SPR_PLSG, 1, 20, A_ReFire, S_PLASMA),  # S_PLASMA2
    State(SPR_PLSF, 32768, 4, A_Light1, S_LIGHTDONE),  # S_PLASMAFLASH1
    State(SPR_PLSF, 32769, 4, A_Light1, S_LIGHTDONE),  # S_PLASMAFLASH2
    State(SPR_BFGG, 0, 1, A_WeaponReady, S_BFG),  # S_BFG
    State(SPR_BFGG, 0, 1, A_Lower, S_BFGDOWN),  # S_BFGDOWN
    State(SPR_BFGG, 0, 1, A_Raise, S_BFGUP),  # S_BFGUP
    State(SPR_BFGG, 0, 20, A_BFGsound, S_BFG2),  # S_BFG1
    State(SPR_BFGG, 1, 10, A_GunFlash, S_BFG3),  # S_BFG2
    State(SPR_BFGG, 1, 10, A_FireBFG, S_BFG4),  # S_BFG3
    State(SPR_BFGG, 1, 20, A_ReFire, S_BFG),  # S_BFG4
    State(SPR_BFGF, 32768, 11, A_Light1, S_BFGFLASH2),  # S_BFGFLASH1
    State(SPR_BFGF, 32769, 6, A_Light2, S_LIGHTDONE),  # S_BFGFLASH2
    State(SPR_BLUD, 2, 8, None, S_BLOOD2),  # S_BLOOD1
    State(SPR_BLUD, 1, 8, None, S_BLOOD3),  # S_BLOOD2
    State(SPR_BLUD, 0, 8, None, S_NULL),  # S_BLOOD3
    State(SPR_PUFF, 32768, 4, None, S_PUFF2),  # S_PUFF1
    State(SPR_PUFF, 1, 4, None, S_PUFF3),  # S_PUFF2
    State(SPR_PUFF, 2, 4, None, S_PUFF4),  # S_PUFF3
    State(SPR_PUFF, 3, 4, None, S_NULL),  # S_PUFF4
    State(SPR_BAL1, 32768, 4, None, S_TBALL2),  # S_TBALL1
    State(SPR_BAL1, 32769, 4, None, S_TBALL1),  # S_TBALL2
    State(SPR_BAL1, 32770, 6, None, S_TBALLX2),  # S_TBALLX1
    State(SPR_BAL1, 32771, 6, None, S_TBALLX3),  # S_TBALLX2
    State(SPR_BAL1, 32772, 6, None, S_NULL),  # S_TBALLX3
    State(SPR_BAL2, 32768, 4, None, S_RBALL2),  # S_RBALL1
    State(SPR_BAL2, 32769, 4, None, S_RBALL1),  # S_RBALL2
    State(SPR_BAL2, 32770, 6, None, S_RBALLX2),  # S_RBALLX1
    State(SPR_BAL2, 32771, 6, None, S_RBALLX3),  # S_RBALLX2
    State(SPR_BAL2, 32772, 6, None, S_NULL),  # S_RBALLX3
    State(SPR_PLSS, 32768, 6, None, S_PLASBALL2),  # S_PLASBALL
    State(SPR_PLSS, 32769, 6, None, S_PLASBALL),  # S_PLASBALL2
    State(SPR_PLSE, 32768, 4, None, S_PLASEXP2),  # S_PLASEXP
    State(SPR_PLSE, 32769, 4, None, S_PLASEXP3),  # S_PLASEXP2
    State(SPR_PLSE, 32770, 4, None, S_PLASEXP4),  # S_PLASEXP3
    State(SPR_PLSE, 32771, 4, None, S_PLASEXP5),  # S_PLASEXP4
    State(SPR_PLSE, 32772, 4, None, S_NULL),  # S_PLASEXP5
    State(SPR_MISL, 32768, 1, None, S_ROCKET),  # S_ROCKET
    State(SPR_BFS1, 32768, 4, None, S_BFGSHOT2),  # S_BFGSHOT
    State(SPR_BFS1, 32769, 4, None, S_BFGSHOT),  # S_BFGSHOT2
    State(SPR_BFE1, 32768, 8, None, S_BFGLAND2),  # S_BFGLAND
    State(SPR_BFE1, 32769, 8, None, S_BFGLAND3),  # S_BFGLAND2
    State(SPR_BFE1, 32770, 8, A_BFGSpray, S_BFGLAND4),  # S_BFGLAND3
    State(SPR_BFE1, 32771, 8, None, S_BFGLAND5),  # S_BFGLAND4
    State(SPR_BFE1, 32772, 8, None, S_BFGLAND6),  # S_BFGLAND5
    State(SPR_BFE1, 32773, 8, None, S_NULL),  # S_BFGLAND6
    State(SPR_BFE2, 32768, 8, None, S_BFGEXP2),  # S_BFGEXP
    State(SPR_BFE2, 32769, 8, None, S_BFGEXP3),  # S_BFGEXP2
    State(SPR_BFE2, 32770, 8, None, S_BFGEXP4),  # S_BFGEXP3
    State(SPR_BFE2, 32771, 8, None, S_NULL),  # S_BFGEXP4
    State(SPR_MISL, 32769, 8, A_Explode, S_EXPLODE2),  # S_EXPLODE1
    State(SPR_MISL, 32770, 6, None, S_EXPLODE3),  # S_EXPLODE2
    State(SPR_MISL, 32771, 4, None, S_NULL),  # S_EXPLODE3
    State(SPR_TFOG, 32768, 6, None, S_TFOG01),  # S_TFOG
    State(SPR_TFOG, 32769, 6, None, S_TFOG02),  # S_TFOG01
    State(SPR_TFOG, 32768, 6, None, S_TFOG2),  # S_TFOG02
    State(SPR_TFOG, 32769, 6, None, S_TFOG3),  # S_TFOG2
    State(SPR_TFOG, 32770, 6, None, S_TFOG4),  # S_TFOG3
    State(SPR_TFOG, 32771, 6, None, S_TFOG5),  # S_TFOG4
    State(SPR_TFOG, 32772, 6, None, S_TFOG6),  # S_TFOG5
    State(SPR_TFOG, 32773, 6, None, S_TFOG7),  # S_TFOG6
    State(SPR_TFOG, 32774, 6, None, S_TFOG8),  # S_TFOG7
    State(SPR_TFOG, 32775, 6, None, S_TFOG9),  # S_TFOG8
    State(SPR_TFOG, 32776, 6, None, S_TFOG10),  # S_TFOG9
    State(SPR_TFOG, 32777, 6, None, S_NULL),  # S_TFOG10
    State(SPR_IFOG, 32768, 6, None, S_IFOG01),  # S_IFOG
    State(SPR_IFOG, 32769, 6, None, S_IFOG02),  # S_IFOG01
    State(SPR_IFOG, 32768, 6, None, S_IFOG2),  # S_IFOG02
    State(SPR_IFOG, 32769, 6, None, S_IFOG3),  # S_IFOG2
    State(SPR_IFOG, 32770, 6, None, S_IFOG4),  # S_IFOG3
    State(SPR_IFOG, 32771, 6, None, S_IFOG5),  # S_IFOG4
    State(SPR_IFOG, 32772, 6, None, S_NULL),  # S_IFOG5
    State(SPR_PLAY, 0, -1, None, S_NULL),  # S_PLAY
    State(SPR_PLAY, 0, 4, None, S_PLAY_RUN2),  # S_PLAY_RUN1
    State(SPR_PLAY, 1, 4, None, S_PLAY_RUN3),  # S_PLAY_RUN2
    State(SPR_PLAY, 2, 4, None, S_PLAY_RUN4),  # S_PLAY_RUN3
    State(SPR_PLAY, 3, 4, None, S_PLAY_RUN1),  # S_PLAY_RUN4
    State(SPR_PLAY, 4, 12, None, S_PLAY),  # S_PLAY_ATK1
    State(SPR_PLAY, 32773, 6, None, S_PLAY_ATK1),  # S_PLAY_ATK2
    State(SPR_PLAY, 6, 4, None, S_PLAY_PAIN2),  # S_PLAY_PAIN
    State(SPR_PLAY, 6, 4, A_Pain, S_PLAY),  # S_PLAY_PAIN2
    State(SPR_PLAY, 7, 10, None, S_PLAY_DIE2),  # S_PLAY_DIE1
    State(SPR_PLAY, 8, 10, A_PlayerScream, S_PLAY_DIE3),  # S_PLAY_DIE2
    State(SPR_PLAY, 9, 10, A_Fall, S_PLAY_DIE4),  # S_PLAY_DIE3
    State(SPR_PLAY, 10, 10, None, S_PLAY_DIE5),  # S_PLAY_DIE4
    State(SPR_PLAY, 11, 10, None, S_PLAY_DIE6),  # S_PLAY_DIE5
    State(SPR_PLAY, 12, 10, None, S_PLAY_DIE7),  # S_PLAY_DIE6
    State(SPR_PLAY, 13, -1, None, S_NULL),  # S_PLAY_DIE7
    State(SPR_PLAY, 14, 5, None, S_PLAY_XDIE2),  # S_PLAY_XDIE1
    State(SPR_PLAY, 15, 5, A_XScream, S_PLAY_XDIE3),  # S_PLAY_XDIE2
    State(SPR_PLAY, 16, 5, A_Fall, S_PLAY_XDIE4),  # S_PLAY_XDIE3
    State(SPR_PLAY, 17, 5, None, S_PLAY_XDIE5),  # S_PLAY_XDIE4
    State(SPR_PLAY, 18, 5, None, S_PLAY_XDIE6),  # S_PLAY_XDIE5
    State(SPR_PLAY, 19, 5, None, S_PLAY_XDIE7),  # S_PLAY_XDIE6
    State(SPR_PLAY, 20, 5, None, S_PLAY_XDIE8),  # S_PLAY_XDIE7
    State(SPR_PLAY, 21, 5, None, S_PLAY_XDIE9),  # S_PLAY_XDIE8
    State(SPR_PLAY, 22, -1, None, S_NULL),  # S_PLAY_XDIE9
    State(SPR_POSS, 0, 10, A_Look, S_POSS_STND2),  # S_POSS_STND
    State(SPR_POSS, 1, 10, A_Look, S_POSS_STND),  # S_POSS_STND2
    State(SPR_POSS, 0, 4, A_Chase, S_POSS_RUN2),  # S_POSS_RUN1
    State(SPR_POSS, 0, 4, A_Chase, S_POSS_RUN3),  # S_POSS_RUN2
    State(SPR_POSS, 1, 4, A_Chase, S_POSS_RUN4),  # S_POSS_RUN3
    State(SPR_POSS, 1, 4, A_Chase, S_POSS_RUN5),  # S_POSS_RUN4
    State(SPR_POSS, 2, 4, A_Chase, S_POSS_RUN6),  # S_POSS_RUN5
    State(SPR_POSS, 2, 4, A_Chase, S_POSS_RUN7),  # S_POSS_RUN6
    State(SPR_POSS, 3, 4, A_Chase, S_POSS_RUN8),  # S_POSS_RUN7
    State(SPR_POSS, 3, 4, A_Chase, S_POSS_RUN1),  # S_POSS_RUN8
    State(SPR_POSS, 4, 10, A_FaceTarget, S_POSS_ATK2),  # S_POSS_ATK1
    State(SPR_POSS, 5, 8, A_PosAttack, S_POSS_ATK3),  # S_POSS_ATK2
    State(SPR_POSS, 4, 8, None, S_POSS_RUN1),  # S_POSS_ATK3
    State(SPR_POSS, 6, 3, None, S_POSS_PAIN2),  # S_POSS_PAIN
    State(SPR_POSS, 6, 3, A_Pain, S_POSS_RUN1),  # S_POSS_PAIN2
    State(SPR_POSS, 7, 5, None, S_POSS_DIE2),  # S_POSS_DIE1
    State(SPR_POSS, 8, 5, A_Scream, S_POSS_DIE3),  # S_POSS_DIE2
    State(SPR_POSS, 9, 5, A_Fall, S_POSS_DIE4),  # S_POSS_DIE3
    State(SPR_POSS, 10, 5, None, S_POSS_DIE5),  # S_POSS_DIE4
    State(SPR_POSS, 11, -1, None, S_NULL),  # S_POSS_DIE5
    State(SPR_POSS, 12, 5, None, S_POSS_XDIE2),  # S_POSS_XDIE1
    State(SPR_POSS, 13, 5, A_XScream, S_POSS_XDIE3),  # S_POSS_XDIE2
    State(SPR_POSS, 14, 5, A_Fall, S_POSS_XDIE4),  # S_POSS_XDIE3
    State(SPR_POSS, 15, 5, None, S_POSS_XDIE5),  # S_POSS_XDIE4
    State(SPR_POSS, 16, 5, None, S_POSS_XDIE6),  # S_POSS_XDIE5
    State(SPR_POSS, 17, 5, None, S_POSS_XDIE7),  # S_POSS_XDIE6
    State(SPR_POSS, 18, 5, None, S_POSS_XDIE8),  # S_POSS_XDIE7
    State(SPR_POSS, 19, 5, None, S_POSS_XDIE9),  # S_POSS_XDIE8
    State(SPR_POSS, 20, -1, None, S_NULL),  # S_POSS_XDIE9
    State(SPR_POSS, 10, 5, None, S_POSS_RAISE2),  # S_POSS_RAISE1
    State(SPR_POSS, 9, 5, None, S_POSS_RAISE3),  # S_POSS_RAISE2
    State(SPR_POSS, 8, 5, None, S_POSS_RAISE4),  # S_POSS_RAISE3
    State(SPR_POSS, 7, 5, None, S_POSS_RUN1),  # S_POSS_RAISE4
    State(SPR_SPOS, 0, 10, A_Look, S_SPOS_STND2),  # S_SPOS_STND
    State(SPR_SPOS, 1, 10, A_Look, S_SPOS_STND),  # S_SPOS_STND2
    State(SPR_SPOS, 0, 3, A_Chase, S_SPOS_RUN2),  # S_SPOS_RUN1
    State(SPR_SPOS, 0, 3, A_Chase, S_SPOS_RUN3),  # S_SPOS_RUN2
    State(SPR_SPOS, 1, 3, A_Chase, S_SPOS_RUN4),  # S_SPOS_RUN3
    State(SPR_SPOS, 1, 3, A_Chase, S_SPOS_RUN5),  # S_SPOS_RUN4
    State(SPR_SPOS, 2, 3, A_Chase, S_SPOS_RUN6),  # S_SPOS_RUN5
    State(SPR_SPOS, 2, 3, A_Chase, S_SPOS_RUN7),  # S_SPOS_RUN6
    State(SPR_SPOS, 3, 3, A_Chase, S_SPOS_RUN8),  # S_SPOS_RUN7
    State(SPR_SPOS, 3, 3, A_Chase, S_SPOS_RUN1),  # S_SPOS_RUN8
    State(SPR_SPOS, 4, 10, A_FaceTarget, S_SPOS_ATK2),  # S_SPOS_ATK1
    State(SPR_SPOS, 32773, 10, A_SPosAttack, S_SPOS_ATK3),  # S_SPOS_ATK2
    State(SPR_SPOS, 4, 10, None, S_SPOS_RUN1),  # S_SPOS_ATK3
    State(SPR_SPOS, 6, 3, None, S_SPOS_PAIN2),  # S_SPOS_PAIN
    State(SPR_SPOS, 6, 3, A_Pain, S_SPOS_RUN1),  # S_SPOS_PAIN2
    State(SPR_SPOS, 7, 5, None, S_SPOS_DIE2),  # S_SPOS_DIE1
    State(SPR_SPOS, 8, 5, A_Scream, S_SPOS_DIE3),  # S_SPOS_DIE2
    State(SPR_SPOS, 9, 5, A_Fall, S_SPOS_DIE4),  # S_SPOS_DIE3
    State(SPR_SPOS, 10, 5, None, S_SPOS_DIE5),  # S_SPOS_DIE4
    State(SPR_SPOS, 11, -1, None, S_NULL),  # S_SPOS_DIE5
    State(SPR_SPOS, 12, 5, None, S_SPOS_XDIE2),  # S_SPOS_XDIE1
    State(SPR_SPOS, 13, 5, A_XScream, S_SPOS_XDIE3),  # S_SPOS_XDIE2
    State(SPR_SPOS, 14, 5, A_Fall, S_SPOS_XDIE4),  # S_SPOS_XDIE3
    State(SPR_SPOS, 15, 5, None, S_SPOS_XDIE5),  # S_SPOS_XDIE4
    State(SPR_SPOS, 16, 5, None, S_SPOS_XDIE6),  # S_SPOS_XDIE5
    State(SPR_SPOS, 17, 5, None, S_SPOS_XDIE7),  # S_SPOS_XDIE6
    State(SPR_SPOS, 18, 5, None, S_SPOS_XDIE8),  # S_SPOS_XDIE7
    State(SPR_SPOS, 19, 5, None, S_SPOS_XDIE9),  # S_SPOS_XDIE8
    State(SPR_SPOS, 20, -1, None, S_NULL),  # S_SPOS_XDIE9
    State(SPR_SPOS, 11, 5, None, S_SPOS_RAISE2),  # S_SPOS_RAISE1
    State(SPR_SPOS, 10, 5, None, S_SPOS_RAISE3),  # S_SPOS_RAISE2
    State(SPR_SPOS, 9, 5, None, S_SPOS_RAISE4),  # S_SPOS_RAISE3
    State(SPR_SPOS, 8, 5, None, S_SPOS_RAISE5),  # S_SPOS_RAISE4
    State(SPR_SPOS, 7, 5, None, S_SPOS_RUN1),  # S_SPOS_RAISE5
    State(SPR_VILE, 0, 10, A_Look, S_VILE_STND2),  # S_VILE_STND
    State(SPR_VILE, 1, 10, A_Look, S_VILE_STND),  # S_VILE_STND2
    State(SPR_VILE, 0, 2, A_VileChase, S_VILE_RUN2),  # S_VILE_RUN1
    State(SPR_VILE, 0, 2, A_VileChase, S_VILE_RUN3),  # S_VILE_RUN2
    State(SPR_VILE, 1, 2, A_VileChase, S_VILE_RUN4),  # S_VILE_RUN3
    State(SPR_VILE, 1, 2, A_VileChase, S_VILE_RUN5),  # S_VILE_RUN4
    State(SPR_VILE, 2, 2, A_VileChase, S_VILE_RUN6),  # S_VILE_RUN5
    State(SPR_VILE, 2, 2, A_VileChase, S_VILE_RUN7),  # S_VILE_RUN6
    State(SPR_VILE, 3, 2, A_VileChase, S_VILE_RUN8),  # S_VILE_RUN7
    State(SPR_VILE, 3, 2, A_VileChase, S_VILE_RUN9),  # S_VILE_RUN8
    State(SPR_VILE, 4, 2, A_VileChase, S_VILE_RUN10),  # S_VILE_RUN9
    State(SPR_VILE, 4, 2, A_VileChase, S_VILE_RUN11),  # S_VILE_RUN10
    State(SPR_VILE, 5, 2, A_VileChase, S_VILE_RUN12),  # S_VILE_RUN11
    State(SPR_VILE, 5, 2, A_VileChase, S_VILE_RUN1),  # S_VILE_RUN12
    State(SPR_VILE, 32774, 0, A_VileStart, S_VILE_ATK2),  # S_VILE_ATK1
    State(SPR_VILE, 32774, 10, A_FaceTarget, S_VILE_ATK3),  # S_VILE_ATK2
    State(SPR_VILE, 32775, 8, A_VileTarget, S_VILE_ATK4),  # S_VILE_ATK3
    State(SPR_VILE, 32776, 8, A_FaceTarget, S_VILE_ATK5),  # S_VILE_ATK4
    State(SPR_VILE, 32777, 8, A_FaceTarget, S_VILE_ATK6),  # S_VILE_ATK5
    State(SPR_VILE, 32778, 8, A_FaceTarget, S_VILE_ATK7),  # S_VILE_ATK6
    State(SPR_VILE, 32779, 8, A_FaceTarget, S_VILE_ATK8),  # S_VILE_ATK7
    State(SPR_VILE, 32780, 8, A_FaceTarget, S_VILE_ATK9),  # S_VILE_ATK8
    State(SPR_VILE, 32781, 8, A_FaceTarget, S_VILE_ATK10),  # S_VILE_ATK9
    State(SPR_VILE, 32782, 8, A_VileAttack, S_VILE_ATK11),  # S_VILE_ATK10
    State(SPR_VILE, 32783, 20, None, S_VILE_RUN1),  # S_VILE_ATK11
    State(SPR_VILE, 32794, 10, None, S_VILE_HEAL2),  # S_VILE_HEAL1
    State(SPR_VILE, 32795, 10, None, S_VILE_HEAL3),  # S_VILE_HEAL2
    State(SPR_VILE, 32796, 10, None, S_VILE_RUN1),  # S_VILE_HEAL3
    State(SPR_VILE, 16, 5, None, S_VILE_PAIN2),  # S_VILE_PAIN
    State(SPR_VILE, 16, 5, A_Pain, S_VILE_RUN1),  # S_VILE_PAIN2
    State(SPR_VILE, 16, 7, None, S_VILE_DIE2),  # S_VILE_DIE1
    State(SPR_VILE, 17, 7, A_Scream, S_VILE_DIE3),  # S_VILE_DIE2
    State(SPR_VILE, 18, 7, A_Fall, S_VILE_DIE4),  # S_VILE_DIE3
    State(SPR_VILE, 19, 7, None, S_VILE_DIE5),  # S_VILE_DIE4
    State(SPR_VILE, 20, 7, None, S_VILE_DIE6),  # S_VILE_DIE5
    State(SPR_VILE, 21, 7, None, S_VILE_DIE7),  # S_VILE_DIE6
    State(SPR_VILE, 22, 7, None, S_VILE_DIE8),  # S_VILE_DIE7
    State(SPR_VILE, 23, 5, None, S_VILE_DIE9),  # S_VILE_DIE8
    State(SPR_VILE, 24, 5, None, S_VILE_DIE10),  # S_VILE_DIE9
    State(SPR_VILE, 25, -1, None, S_NULL),  # S_VILE_DIE10
    State(SPR_FIRE, 32768, 2, A_StartFire, S_FIRE2),  # S_FIRE1
    State(SPR_FIRE, 32769, 2, A_Fire, S_FIRE3),  # S_FIRE2
    State(SPR_FIRE, 32768, 2, A_Fire, S_FIRE4),  # S_FIRE3
    State(SPR_FIRE, 32769, 2, A_Fire, S_FIRE5),  # S_FIRE4
    State(SPR_FIRE, 32770, 2, A_FireCrackle, S_FIRE6),  # S_FIRE5
    State(SPR_FIRE, 32769, 2, A_Fire, S_FIRE7),  # S_FIRE6
    State(SPR_FIRE, 32770, 2, A_Fire, S_FIRE8),  # S_FIRE7
    State(SPR_FIRE, 32769, 2, A_Fire, S_FIRE9),  # S_FIRE8
    State(SPR_FIRE, 32770, 2, A_Fire, S_FIRE10),  # S_FIRE9
    State(SPR_FIRE, 32771, 2, A_Fire, S_FIRE11),  # S_FIRE10
    State(SPR_FIRE, 32770, 2, A_Fire, S_FIRE12),  # S_FIRE11
    State(SPR_FIRE, 32771, 2, A_Fire, S_FIRE13),  # S_FIRE12
    State(SPR_FIRE, 32770, 2, A_Fire, S_FIRE14),  # S_FIRE13
    State(SPR_FIRE, 32771, 2, A_Fire, S_FIRE15),  # S_FIRE14
    State(SPR_FIRE, 32772, 2, A_Fire, S_FIRE16),  # S_FIRE15
    State(SPR_FIRE, 32771, 2, A_Fire, S_FIRE17),  # S_FIRE16
    State(SPR_FIRE, 32772, 2, A_Fire, S_FIRE18),  # S_FIRE17
    State(SPR_FIRE, 32771, 2, A_Fire, S_FIRE19),  # S_FIRE18
    State(SPR_FIRE, 32772, 2, A_FireCrackle, S_FIRE20),  # S_FIRE19
    State(SPR_FIRE, 32773, 2, A_Fire, S_FIRE21),  # S_FIRE20
    State(SPR_FIRE, 32772, 2, A_Fire, S_FIRE22),  # S_FIRE21
    State(SPR_FIRE, 32773, 2, A_Fire, S_FIRE23),  # S_FIRE22
    State(SPR_FIRE, 32772, 2, A_Fire, S_FIRE24),  # S_FIRE23
    State(SPR_FIRE, 32773, 2, A_Fire, S_FIRE25),  # S_FIRE24
    State(SPR_FIRE, 32774, 2, A_Fire, S_FIRE26),  # S_FIRE25
    State(SPR_FIRE, 32775, 2, A_Fire, S_FIRE27),  # S_FIRE26
    State(SPR_FIRE, 32774, 2, A_Fire, S_FIRE28),  # S_FIRE27
    State(SPR_FIRE, 32775, 2, A_Fire, S_FIRE29),  # S_FIRE28
    State(SPR_FIRE, 32774, 2, A_Fire, S_FIRE30),  # S_FIRE29
    State(SPR_FIRE, 32775, 2, A_Fire, S_NULL),  # S_FIRE30
    State(SPR_PUFF, 1, 4, None, S_SMOKE2),  # S_SMOKE1
    State(SPR_PUFF, 2, 4, None, S_SMOKE3),  # S_SMOKE2
    State(SPR_PUFF, 1, 4, None, S_SMOKE4),  # S_SMOKE3
    State(SPR_PUFF, 2, 4, None, S_SMOKE5),  # S_SMOKE4
    State(SPR_PUFF, 3, 4, None, S_NULL),  # S_SMOKE5
    State(SPR_FATB, 32768, 2, A_Tracer, S_TRACER2),  # S_TRACER
    State(SPR_FATB, 32769, 2, A_Tracer, S_TRACER),  # S_TRACER2
    State(SPR_FBXP, 32768, 8, None, S_TRACEEXP2),  # S_TRACEEXP1
    State(SPR_FBXP, 32769, 6, None, S_TRACEEXP3),  # S_TRACEEXP2
    State(SPR_FBXP, 32770, 4, None, S_NULL),  # S_TRACEEXP3
    State(SPR_SKEL, 0, 10, A_Look, S_SKEL_STND2),  # S_SKEL_STND
    State(SPR_SKEL, 1, 10, A_Look, S_SKEL_STND),  # S_SKEL_STND2
    State(SPR_SKEL, 0, 2, A_Chase, S_SKEL_RUN2),  # S_SKEL_RUN1
    State(SPR_SKEL, 0, 2, A_Chase, S_SKEL_RUN3),  # S_SKEL_RUN2
    State(SPR_SKEL, 1, 2, A_Chase, S_SKEL_RUN4),  # S_SKEL_RUN3
    State(SPR_SKEL, 1, 2, A_Chase, S_SKEL_RUN5),  # S_SKEL_RUN4
    State(SPR_SKEL, 2, 2, A_Chase, S_SKEL_RUN6),  # S_SKEL_RUN5
    State(SPR_SKEL, 2, 2, A_Chase, S_SKEL_RUN7),  # S_SKEL_RUN6
    State(SPR_SKEL, 3, 2, A_Chase, S_SKEL_RUN8),  # S_SKEL_RUN7
    State(SPR_SKEL, 3, 2, A_Chase, S_SKEL_RUN9),  # S_SKEL_RUN8
    State(SPR_SKEL, 4, 2, A_Chase, S_SKEL_RUN10),  # S_SKEL_RUN9
    State(SPR_SKEL, 4, 2, A_Chase, S_SKEL_RUN11),  # S_SKEL_RUN10
    State(SPR_SKEL, 5, 2, A_Chase, S_SKEL_RUN12),  # S_SKEL_RUN11
    State(SPR_SKEL, 5, 2, A_Chase, S_SKEL_RUN1),  # S_SKEL_RUN12
    State(SPR_SKEL, 6, 0, A_FaceTarget, S_SKEL_FIST2),  # S_SKEL_FIST1
    State(SPR_SKEL, 6, 6, A_SkelWhoosh, S_SKEL_FIST3),  # S_SKEL_FIST2
    State(SPR_SKEL, 7, 6, A_FaceTarget, S_SKEL_FIST4),  # S_SKEL_FIST3
    State(SPR_SKEL, 8, 6, A_SkelFist, S_SKEL_RUN1),  # S_SKEL_FIST4
    State(SPR_SKEL, 32777, 0, A_FaceTarget, S_SKEL_MISS2),  # S_SKEL_MISS1
    State(SPR_SKEL, 32777, 10, A_FaceTarget, S_SKEL_MISS3),  # S_SKEL_MISS2
    State(SPR_SKEL, 10, 10, A_SkelMissile, S_SKEL_MISS4),  # S_SKEL_MISS3
    State(SPR_SKEL, 10, 10, A_FaceTarget, S_SKEL_RUN1),  # S_SKEL_MISS4
    State(SPR_SKEL, 11, 5, None, S_SKEL_PAIN2),  # S_SKEL_PAIN
    State(SPR_SKEL, 11, 5, A_Pain, S_SKEL_RUN1),  # S_SKEL_PAIN2
    State(SPR_SKEL, 11, 7, None, S_SKEL_DIE2),  # S_SKEL_DIE1
    State(SPR_SKEL, 12, 7, None, S_SKEL_DIE3),  # S_SKEL_DIE2
    State(SPR_SKEL, 13, 7, A_Scream, S_SKEL_DIE4),  # S_SKEL_DIE3
    State(SPR_SKEL, 14, 7, A_Fall, S_SKEL_DIE5),  # S_SKEL_DIE4
    State(SPR_SKEL, 15, 7, None, S_SKEL_DIE6),  # S_SKEL_DIE5
    State(SPR_SKEL, 16, -1, None, S_NULL),  # S_SKEL_DIE6
    State(SPR_SKEL, 16, 5, None, S_SKEL_RAISE2),  # S_SKEL_RAISE1
    State(SPR_SKEL, 15, 5, None, S_SKEL_RAISE3),  # S_SKEL_RAISE2
    State(SPR_SKEL, 14, 5, None, S_SKEL_RAISE4),  # S_SKEL_RAISE3
    State(SPR_SKEL, 13, 5, None, S_SKEL_RAISE5),  # S_SKEL_RAISE4
    State(SPR_SKEL, 12, 5, None, S_SKEL_RAISE6),  # S_SKEL_RAISE5
    State(SPR_SKEL, 11, 5, None, S_SKEL_RUN1),  # S_SKEL_RAISE6
    State(SPR_MANF, 32768, 4, None, S_FATSHOT2),  # S_FATSHOT1
    State(SPR_MANF, 32769, 4, None, S_FATSHOT1),  # S_FATSHOT2
    State(SPR_MISL, 32769, 8, None, S_FATSHOTX2),  # S_FATSHOTX1
    State(SPR_MISL, 32770, 6, None, S_FATSHOTX3),  # S_FATSHOTX2
    State(SPR_MISL, 32771, 4, None, S_NULL),  # S_FATSHOTX3
    State(SPR_FATT, 0, 15, A_Look, S_FATT_STND2),  # S_FATT_STND
    State(SPR_FATT, 1, 15, A_Look, S_FATT_STND),  # S_FATT_STND2
    State(SPR_FATT, 0, 4, A_Chase, S_FATT_RUN2),  # S_FATT_RUN1
    State(SPR_FATT, 0, 4, A_Chase, S_FATT_RUN3),  # S_FATT_RUN2
    State(SPR_FATT, 1, 4, A_Chase, S_FATT_RUN4),  # S_FATT_RUN3
    State(SPR_FATT, 1, 4, A_Chase, S_FATT_RUN5),  # S_FATT_RUN4
    State(SPR_FATT, 2, 4, A_Chase, S_FATT_RUN6),  # S_FATT_RUN5
    State(SPR_FATT, 2, 4, A_Chase, S_FATT_RUN7),  # S_FATT_RUN6
    State(SPR_FATT, 3, 4, A_Chase, S_FATT_RUN8),  # S_FATT_RUN7
    State(SPR_FATT, 3, 4, A_Chase, S_FATT_RUN9),  # S_FATT_RUN8
    State(SPR_FATT, 4, 4, A_Chase, S_FATT_RUN10),  # S_FATT_RUN9
    State(SPR_FATT, 4, 4, A_Chase, S_FATT_RUN11),  # S_FATT_RUN10
    State(SPR_FATT, 5, 4, A_Chase, S_FATT_RUN12),  # S_FATT_RUN11
    State(SPR_FATT, 5, 4, A_Chase, S_FATT_RUN1),  # S_FATT_RUN12
    State(SPR_FATT, 6, 20, A_FatRaise, S_FATT_ATK2),  # S_FATT_ATK1
    State(SPR_FATT, 32775, 10, A_FatAttack1, S_FATT_ATK3),  # S_FATT_ATK2
    State(SPR_FATT, 8, 5, A_FaceTarget, S_FATT_ATK4),  # S_FATT_ATK3
    State(SPR_FATT, 6, 5, A_FaceTarget, S_FATT_ATK5),  # S_FATT_ATK4
    State(SPR_FATT, 32775, 10, A_FatAttack2, S_FATT_ATK6),  # S_FATT_ATK5
    State(SPR_FATT, 8, 5, A_FaceTarget, S_FATT_ATK7),  # S_FATT_ATK6
    State(SPR_FATT, 6, 5, A_FaceTarget, S_FATT_ATK8),  # S_FATT_ATK7
    State(SPR_FATT, 32775, 10, A_FatAttack3, S_FATT_ATK9),  # S_FATT_ATK8
    State(SPR_FATT, 8, 5, A_FaceTarget, S_FATT_ATK10),  # S_FATT_ATK9
    State(SPR_FATT, 6, 5, A_FaceTarget, S_FATT_RUN1),  # S_FATT_ATK10
    State(SPR_FATT, 9, 3, None, S_FATT_PAIN2),  # S_FATT_PAIN
    State(SPR_FATT, 9, 3, A_Pain, S_FATT_RUN1),  # S_FATT_PAIN2
    State(SPR_FATT, 10, 6, None, S_FATT_DIE2),  # S_FATT_DIE1
    State(SPR_FATT, 11, 6, A_Scream, S_FATT_DIE3),  # S_FATT_DIE2
    State(SPR_FATT, 12, 6, A_Fall, S_FATT_DIE4),  # S_FATT_DIE3
    State(SPR_FATT, 13, 6, None, S_FATT_DIE5),  # S_FATT_DIE4
    State(SPR_FATT, 14, 6, None, S_FATT_DIE6),  # S_FATT_DIE5
    State(SPR_FATT, 15, 6, None, S_FATT_DIE7),  # S_FATT_DIE6
    State(SPR_FATT, 16, 6, None, S_FATT_DIE8),  # S_FATT_DIE7
    State(SPR_FATT, 17, 6, None, S_FATT_DIE9),  # S_FATT_DIE8
    State(SPR_FATT, 18, 6, None, S_FATT_DIE10),  # S_FATT_DIE9
    State(SPR_FATT, 19, -1, A_BossDeath, S_NULL),  # S_FATT_DIE10
    State(SPR_FATT, 17, 5, None, S_FATT_RAISE2),  # S_FATT_RAISE1
    State(SPR_FATT, 16, 5, None, S_FATT_RAISE3),  # S_FATT_RAISE2
    State(SPR_FATT, 15, 5, None, S_FATT_RAISE4),  # S_FATT_RAISE3
    State(SPR_FATT, 14, 5, None, S_FATT_RAISE5),  # S_FATT_RAISE4
    State(SPR_FATT, 13, 5, None, S_FATT_RAISE6),  # S_FATT_RAISE5
    State(SPR_FATT, 12, 5, None, S_FATT_RAISE7),  # S_FATT_RAISE6
    State(SPR_FATT, 11, 5, None, S_FATT_RAISE8),  # S_FATT_RAISE7
    State(SPR_FATT, 10, 5, None, S_FATT_RUN1),  # S_FATT_RAISE8
    State(SPR_CPOS, 0, 10, A_Look, S_CPOS_STND2),  # S_CPOS_STND
    State(SPR_CPOS, 1, 10, A_Look, S_CPOS_STND),  # S_CPOS_STND2
    State(SPR_CPOS, 0, 3, A_Chase, S_CPOS_RUN2),  # S_CPOS_RUN1
    State(SPR_CPOS, 0, 3, A_Chase, S_CPOS_RUN3),  # S_CPOS_RUN2
    State(SPR_CPOS, 1, 3, A_Chase, S_CPOS_RUN4),  # S_CPOS_RUN3
    State(SPR_CPOS, 1, 3, A_Chase, S_CPOS_RUN5),  # S_CPOS_RUN4
    State(SPR_CPOS, 2, 3, A_Chase, S_CPOS_RUN6),  # S_CPOS_RUN5
    State(SPR_CPOS, 2, 3, A_Chase, S_CPOS_RUN7),  # S_CPOS_RUN6
    State(SPR_CPOS, 3, 3, A_Chase, S_CPOS_RUN8),  # S_CPOS_RUN7
    State(SPR_CPOS, 3, 3, A_Chase, S_CPOS_RUN1),  # S_CPOS_RUN8
    State(SPR_CPOS, 4, 10, A_FaceTarget, S_CPOS_ATK2),  # S_CPOS_ATK1
    State(SPR_CPOS, 32773, 4, A_CPosAttack, S_CPOS_ATK3),  # S_CPOS_ATK2
    State(SPR_CPOS, 32772, 4, A_CPosAttack, S_CPOS_ATK4),  # S_CPOS_ATK3
    State(SPR_CPOS, 5, 1, A_CPosRefire, S_CPOS_ATK2),  # S_CPOS_ATK4
    State(SPR_CPOS, 6, 3, None, S_CPOS_PAIN2),  # S_CPOS_PAIN
    State(SPR_CPOS, 6, 3, A_Pain, S_CPOS_RUN1),  # S_CPOS_PAIN2
    State(SPR_CPOS, 7, 5, None, S_CPOS_DIE2),  # S_CPOS_DIE1
    State(SPR_CPOS, 8, 5, A_Scream, S_CPOS_DIE3),  # S_CPOS_DIE2
    State(SPR_CPOS, 9, 5, A_Fall, S_CPOS_DIE4),  # S_CPOS_DIE3
    State(SPR_CPOS, 10, 5, None, S_CPOS_DIE5),  # S_CPOS_DIE4
    State(SPR_CPOS, 11, 5, None, S_CPOS_DIE6),  # S_CPOS_DIE5
    State(SPR_CPOS, 12, 5, None, S_CPOS_DIE7),  # S_CPOS_DIE6
    State(SPR_CPOS, 13, -1, None, S_NULL),  # S_CPOS_DIE7
    State(SPR_CPOS, 14, 5, None, S_CPOS_XDIE2),  # S_CPOS_XDIE1
    State(SPR_CPOS, 15, 5, A_XScream, S_CPOS_XDIE3),  # S_CPOS_XDIE2
    State(SPR_CPOS, 16, 5, A_Fall, S_CPOS_XDIE4),  # S_CPOS_XDIE3
    State(SPR_CPOS, 17, 5, None, S_CPOS_XDIE5),  # S_CPOS_XDIE4
    State(SPR_CPOS, 18, 5, None, S_CPOS_XDIE6),  # S_CPOS_XDIE5
    State(SPR_CPOS, 19, -1, None, S_NULL),  # S_CPOS_XDIE6
    State(SPR_CPOS, 13, 5, None, S_CPOS_RAISE2),  # S_CPOS_RAISE1
    State(SPR_CPOS, 12, 5, None, S_CPOS_RAISE3),  # S_CPOS_RAISE2
    State(SPR_CPOS, 11, 5, None, S_CPOS_RAISE4),  # S_CPOS_RAISE3
    State(SPR_CPOS, 10, 5, None, S_CPOS_RAISE5),  # S_CPOS_RAISE4
    State(SPR_CPOS, 9, 5, None, S_CPOS_RAISE6),  # S_CPOS_RAISE5
    State(SPR_CPOS, 8, 5, None, S_CPOS_RAISE7),  # S_CPOS_RAISE6
    State(SPR_CPOS, 7, 5, None, S_CPOS_RUN1),  # S_CPOS_RAISE7
    State(SPR_TROO, 0, 10, A_Look, S_TROO_STND2),  # S_TROO_STND
    State(SPR_TROO, 1, 10, A_Look, S_TROO_STND),  # S_TROO_STND2
    State(SPR_TROO, 0, 3, A_Chase, S_TROO_RUN2),  # S_TROO_RUN1
    State(SPR_TROO, 0, 3, A_Chase, S_TROO_RUN3),  # S_TROO_RUN2
    State(SPR_TROO, 1, 3, A_Chase, S_TROO_RUN4),  # S_TROO_RUN3
    State(SPR_TROO, 1, 3, A_Chase, S_TROO_RUN5),  # S_TROO_RUN4
    State(SPR_TROO, 2, 3, A_Chase, S_TROO_RUN6),  # S_TROO_RUN5
    State(SPR_TROO, 2, 3, A_Chase, S_TROO_RUN7),  # S_TROO_RUN6
    State(SPR_TROO, 3, 3, A_Chase, S_TROO_RUN8),  # S_TROO_RUN7
    State(SPR_TROO, 3, 3, A_Chase, S_TROO_RUN1),  # S_TROO_RUN8
    State(SPR_TROO, 4, 8, A_FaceTarget, S_TROO_ATK2),  # S_TROO_ATK1
    State(SPR_TROO, 5, 8, A_FaceTarget, S_TROO_ATK3),  # S_TROO_ATK2
    State(SPR_TROO, 6, 6, A_TroopAttack, S_TROO_RUN1),  # S_TROO_ATK3
    State(SPR_TROO, 7, 2, None, S_TROO_PAIN2),  # S_TROO_PAIN
    State(SPR_TROO, 7, 2, A_Pain, S_TROO_RUN1),  # S_TROO_PAIN2
    State(SPR_TROO, 8, 8, None, S_TROO_DIE2),  # S_TROO_DIE1
    State(SPR_TROO, 9, 8, A_Scream, S_TROO_DIE3),  # S_TROO_DIE2
    State(SPR_TROO, 10, 6, None, S_TROO_DIE4),  # S_TROO_DIE3
    State(SPR_TROO, 11, 6, A_Fall, S_TROO_DIE5),  # S_TROO_DIE4
    State(SPR_TROO, 12, -1, None, S_NULL),  # S_TROO_DIE5
    State(SPR_TROO, 13, 5, None, S_TROO_XDIE2),  # S_TROO_XDIE1
    State(SPR_TROO, 14, 5, A_XScream, S_TROO_XDIE3),  # S_TROO_XDIE2
    State(SPR_TROO, 15, 5, None, S_TROO_XDIE4),  # S_TROO_XDIE3
    State(SPR_TROO, 16, 5, A_Fall, S_TROO_XDIE5),  # S_TROO_XDIE4
    State(SPR_TROO, 17, 5, None, S_TROO_XDIE6),  # S_TROO_XDIE5
    State(SPR_TROO, 18, 5, None, S_TROO_XDIE7),  # S_TROO_XDIE6
    State(SPR_TROO, 19, 5, None, S_TROO_XDIE8),  # S_TROO_XDIE7
    State(SPR_TROO, 20, -1, None, S_NULL),  # S_TROO_XDIE8
    State(SPR_TROO, 12, 8, None, S_TROO_RAISE2),  # S_TROO_RAISE1
    State(SPR_TROO, 11, 8, None, S_TROO_RAISE3),  # S_TROO_RAISE2
    State(SPR_TROO, 10, 6, None, S_TROO_RAISE4),  # S_TROO_RAISE3
    State(SPR_TROO, 9, 6, None, S_TROO_RAISE5),  # S_TROO_RAISE4
    State(SPR_TROO, 8, 6, None, S_TROO_RUN1),  # S_TROO_RAISE5
    State(SPR_SARG, 0, 10, A_Look, S_SARG_STND2),  # S_SARG_STND
    State(SPR_SARG, 1, 10, A_Look, S_SARG_STND),  # S_SARG_STND2
    State(SPR_SARG, 0, 2, A_Chase, S_SARG_RUN2),  # S_SARG_RUN1
    State(SPR_SARG, 0, 2, A_Chase, S_SARG_RUN3),  # S_SARG_RUN2
    State(SPR_SARG, 1, 2, A_Chase, S_SARG_RUN4),  # S_SARG_RUN3
    State(SPR_SARG, 1, 2, A_Chase, S_SARG_RUN5),  # S_SARG_RUN4
    State(SPR_SARG, 2, 2, A_Chase, S_SARG_RUN6),  # S_SARG_RUN5
    State(SPR_SARG, 2, 2, A_Chase, S_SARG_RUN7),  # S_SARG_RUN6
    State(SPR_SARG, 3, 2, A_Chase, S_SARG_RUN8),  # S_SARG_RUN7
    State(SPR_SARG, 3, 2, A_Chase, S_SARG_RUN1),  # S_SARG_RUN8
    State(SPR_SARG, 4, 8, A_FaceTarget, S_SARG_ATK2),  # S_SARG_ATK1
    State(SPR_SARG, 5, 8, A_FaceTarget, S_SARG_ATK3),  # S_SARG_ATK2
    State(SPR_SARG, 6, 8, A_SargAttack, S_SARG_RUN1),  # S_SARG_ATK3
    State(SPR_SARG, 7, 2, None, S_SARG_PAIN2),  # S_SARG_PAIN
    State(SPR_SARG, 7, 2, A_Pain, S_SARG_RUN1),  # S_SARG_PAIN2
    State(SPR_SARG, 8, 8, None, S_SARG_DIE2),  # S_SARG_DIE1
    State(SPR_SARG, 9, 8, A_Scream, S_SARG_DIE3),  # S_SARG_DIE2
    State(SPR_SARG, 10, 4, None, S_SARG_DIE4),  # S_SARG_DIE3
    State(SPR_SARG, 11, 4, A_Fall, S_SARG_DIE5),  # S_SARG_DIE4
    State(SPR_SARG, 12, 4, None, S_SARG_DIE6),  # S_SARG_DIE5
    State(SPR_SARG, 13, -1, None, S_NULL),  # S_SARG_DIE6
    State(SPR_SARG, 13, 5, None, S_SARG_RAISE2),  # S_SARG_RAISE1
    State(SPR_SARG, 12, 5, None, S_SARG_RAISE3),  # S_SARG_RAISE2
    State(SPR_SARG, 11, 5, None, S_SARG_RAISE4),  # S_SARG_RAISE3
    State(SPR_SARG, 10, 5, None, S_SARG_RAISE5),  # S_SARG_RAISE4
    State(SPR_SARG, 9, 5, None, S_SARG_RAISE6),  # S_SARG_RAISE5
    State(SPR_SARG, 8, 5, None, S_SARG_RUN1),  # S_SARG_RAISE6
    State(SPR_HEAD, 0, 10, A_Look, S_HEAD_STND),  # S_HEAD_STND
    State(SPR_HEAD, 0, 3, A_Chase, S_HEAD_RUN1),  # S_HEAD_RUN1
    State(SPR_HEAD, 1, 5, A_FaceTarget, S_HEAD_ATK2),  # S_HEAD_ATK1
    State(SPR_HEAD, 2, 5, A_FaceTarget, S_HEAD_ATK3),  # S_HEAD_ATK2
    State(SPR_HEAD, 32771, 5, A_HeadAttack, S_HEAD_RUN1),  # S_HEAD_ATK3
    State(SPR_HEAD, 4, 3, None, S_HEAD_PAIN2),  # S_HEAD_PAIN
    State(SPR_HEAD, 4, 3, A_Pain, S_HEAD_PAIN3),  # S_HEAD_PAIN2
    State(SPR_HEAD, 5, 6, None, S_HEAD_RUN1),  # S_HEAD_PAIN3
    State(SPR_HEAD, 6, 8, None, S_HEAD_DIE2),  # S_HEAD_DIE1
    State(SPR_HEAD, 7, 8, A_Scream, S_HEAD_DIE3),  # S_HEAD_DIE2
    State(SPR_HEAD, 8, 8, None, S_HEAD_DIE4),  # S_HEAD_DIE3
    State(SPR_HEAD, 9, 8, None, S_HEAD_DIE5),  # S_HEAD_DIE4
    State(SPR_HEAD, 10, 8, A_Fall, S_HEAD_DIE6),  # S_HEAD_DIE5
    State(SPR_HEAD, 11, -1, None, S_NULL),  # S_HEAD_DIE6
    State(SPR_HEAD, 11, 8, None, S_HEAD_RAISE2),  # S_HEAD_RAISE1
    State(SPR_HEAD, 10, 8, None, S_HEAD_RAISE3),  # S_HEAD_RAISE2
    State(SPR_HEAD, 9, 8, None, S_HEAD_RAISE4),  # S_HEAD_RAISE3
    State(SPR_HEAD, 8, 8, None, S_HEAD_RAISE5),  # S_HEAD_RAISE4
    State(SPR_HEAD, 7, 8, None, S_HEAD_RAISE6),  # S_HEAD_RAISE5
    State(SPR_HEAD, 6, 8, None, S_HEAD_RUN1),  # S_HEAD_RAISE6
    State(SPR_BAL7, 32768, 4, None, S_BRBALL2),  # S_BRBALL1
    State(SPR_BAL7, 32769, 4, None, S_BRBALL1),  # S_BRBALL2
    State(SPR_BAL7, 32770, 6, None, S_BRBALLX2),  # S_BRBALLX1
    State(SPR_BAL7, 32771, 6, None, S_BRBALLX3),  # S_BRBALLX2
    State(SPR_BAL7, 32772, 6, None, S_NULL),  # S_BRBALLX3
    State(SPR_BOSS, 0, 10, A_Look, S_BOSS_STND2),  # S_BOSS_STND
    State(SPR_BOSS, 1, 10, A_Look, S_BOSS_STND),  # S_BOSS_STND2
    State(SPR_BOSS, 0, 3, A_Chase, S_BOSS_RUN2),  # S_BOSS_RUN1
    State(SPR_BOSS, 0, 3, A_Chase, S_BOSS_RUN3),  # S_BOSS_RUN2
    State(SPR_BOSS, 1, 3, A_Chase, S_BOSS_RUN4),  # S_BOSS_RUN3
    State(SPR_BOSS, 1, 3, A_Chase, S_BOSS_RUN5),  # S_BOSS_RUN4
    State(SPR_BOSS, 2, 3, A_Chase, S_BOSS_RUN6),  # S_BOSS_RUN5
    State(SPR_BOSS, 2, 3, A_Chase, S_BOSS_RUN7),  # S_BOSS_RUN6
    State(SPR_BOSS, 3, 3, A_Chase, S_BOSS_RUN8),  # S_BOSS_RUN7
    State(SPR_BOSS, 3, 3, A_Chase, S_BOSS_RUN1),  # S_BOSS_RUN8
    State(SPR_BOSS, 4, 8, A_FaceTarget, S_BOSS_ATK2),  # S_BOSS_ATK1
    State(SPR_BOSS, 5, 8, A_FaceTarget, S_BOSS_ATK3),  # S_BOSS_ATK2
    State(SPR_BOSS, 6, 8, A_BruisAttack, S_BOSS_RUN1),  # S_BOSS_ATK3
    State(SPR_BOSS, 7, 2, None, S_BOSS_PAIN2),  # S_BOSS_PAIN
    State(SPR_BOSS, 7, 2, A_Pain, S_BOSS_RUN1),  # S_BOSS_PAIN2
    State(SPR_BOSS, 8, 8, None, S_BOSS_DIE2),  # S_BOSS_DIE1
    State(SPR_BOSS, 9, 8, A_Scream, S_BOSS_DIE3),  # S_BOSS_DIE2
    State(SPR_BOSS, 10, 8, None, S_BOSS_DIE4),  # S_BOSS_DIE3
    State(SPR_BOSS, 11, 8, A_Fall, S_BOSS_DIE5),  # S_BOSS_DIE4
    State(SPR_BOSS, 12, 8, None, S_BOSS_DIE6),  # S_BOSS_DIE5
    State(SPR_BOSS, 13, 8, None, S_BOSS_DIE7),  # S_BOSS_DIE6
    State(SPR_BOSS, 14, -1, A_BossDeath, S_NULL),  # S_BOSS_DIE7
    State(SPR_BOSS, 14, 8, None, S_BOSS_RAISE2),  # S_BOSS_RAISE1
    State(SPR_BOSS, 13, 8, None, S_BOSS_RAISE3),  # S_BOSS_RAISE2
    State(SPR_BOSS, 12, 8, None, S_BOSS_RAISE4),  # S_BOSS_RAISE3
    State(SPR_BOSS, 11, 8, None, S_BOSS_RAISE5),  # S_BOSS_RAISE4
    State(SPR_BOSS, 10, 8, None, S_BOSS_RAISE6),  # S_BOSS_RAISE5
    State(SPR_BOSS, 9, 8, None, S_BOSS_RAISE7),  # S_BOSS_RAISE6
    State(SPR_BOSS, 8, 8, None, S_BOSS_RUN1),  # S_BOSS_RAISE7
    State(SPR_BOS2, 0, 10, A_Look, S_BOS2_STND2),  # S_BOS2_STND
    State(SPR_BOS2, 1, 10, A_Look, S_BOS2_STND),  # S_BOS2_STND2
    State(SPR_BOS2, 0, 3, A_Chase, S_BOS2_RUN2),  # S_BOS2_RUN1
    State(SPR_BOS2, 0, 3, A_Chase, S_BOS2_RUN3),  # S_BOS2_RUN2
    State(SPR_BOS2, 1, 3, A_Chase, S_BOS2_RUN4),  # S_BOS2_RUN3
    State(SPR_BOS2, 1, 3, A_Chase, S_BOS2_RUN5),  # S_BOS2_RUN4
    State(SPR_BOS2, 2, 3, A_Chase, S_BOS2_RUN6),  # S_BOS2_RUN5
    State(SPR_BOS2, 2, 3, A_Chase, S_BOS2_RUN7),  # S_BOS2_RUN6
    State(SPR_BOS2, 3, 3, A_Chase, S_BOS2_RUN8),  # S_BOS2_RUN7
    State(SPR_BOS2, 3, 3, A_Chase, S_BOS2_RUN1),  # S_BOS2_RUN8
    State(SPR_BOS2, 4, 8, A_FaceTarget, S_BOS2_ATK2),  # S_BOS2_ATK1
    State(SPR_BOS2, 5, 8, A_FaceTarget, S_BOS2_ATK3),  # S_BOS2_ATK2
    State(SPR_BOS2, 6, 8, A_BruisAttack, S_BOS2_RUN1),  # S_BOS2_ATK3
    State(SPR_BOS2, 7, 2, None, S_BOS2_PAIN2),  # S_BOS2_PAIN
    State(SPR_BOS2, 7, 2, A_Pain, S_BOS2_RUN1),  # S_BOS2_PAIN2
    State(SPR_BOS2, 8, 8, None, S_BOS2_DIE2),  # S_BOS2_DIE1
    State(SPR_BOS2, 9, 8, A_Scream, S_BOS2_DIE3),  # S_BOS2_DIE2
    State(SPR_BOS2, 10, 8, None, S_BOS2_DIE4),  # S_BOS2_DIE3
    State(SPR_BOS2, 11, 8, A_Fall, S_BOS2_DIE5),  # S_BOS2_DIE4
    State(SPR_BOS2, 12, 8, None, S_BOS2_DIE6),  # S_BOS2_DIE5
    State(SPR_BOS2, 13, 8, None, S_BOS2_DIE7),  # S_BOS2_DIE6
    State(SPR_BOS2, 14, -1, None, S_NULL),  # S_BOS2_DIE7
    State(SPR_BOS2, 14, 8, None, S_BOS2_RAISE2),  # S_BOS2_RAISE1
    State(SPR_BOS2, 13, 8, None, S_BOS2_RAISE3),  # S_BOS2_RAISE2
    State(SPR_BOS2, 12, 8, None, S_BOS2_RAISE4),  # S_BOS2_RAISE3
    State(SPR_BOS2, 11, 8, None, S_BOS2_RAISE5),  # S_BOS2_RAISE4
    State(SPR_BOS2, 10, 8, None, S_BOS2_RAISE6),  # S_BOS2_RAISE5
    State(SPR_BOS2, 9, 8, None, S_BOS2_RAISE7),  # S_BOS2_RAISE6
    State(SPR_BOS2, 8, 8, None, S_BOS2_RUN1),  # S_BOS2_RAISE7
    State(SPR_SKUL, 32768, 10, A_Look, S_SKULL_STND2),  # S_SKULL_STND
    State(SPR_SKUL, 32769, 10, A_Look, S_SKULL_STND),  # S_SKULL_STND2
    State(SPR_SKUL, 32768, 6, A_Chase, S_SKULL_RUN2),  # S_SKULL_RUN1
    State(SPR_SKUL, 32769, 6, A_Chase, S_SKULL_RUN1),  # S_SKULL_RUN2
    State(SPR_SKUL, 32770, 10, A_FaceTarget, S_SKULL_ATK2),  # S_SKULL_ATK1
    State(SPR_SKUL, 32771, 4, A_SkullAttack, S_SKULL_ATK3),  # S_SKULL_ATK2
    State(SPR_SKUL, 32770, 4, None, S_SKULL_ATK4),  # S_SKULL_ATK3
    State(SPR_SKUL, 32771, 4, None, S_SKULL_ATK3),  # S_SKULL_ATK4
    State(SPR_SKUL, 32772, 3, None, S_SKULL_PAIN2),  # S_SKULL_PAIN
    State(SPR_SKUL, 32772, 3, A_Pain, S_SKULL_RUN1),  # S_SKULL_PAIN2
    State(SPR_SKUL, 32773, 6, None, S_SKULL_DIE2),  # S_SKULL_DIE1
    State(SPR_SKUL, 32774, 6, A_Scream, S_SKULL_DIE3),  # S_SKULL_DIE2
    State(SPR_SKUL, 32775, 6, None, S_SKULL_DIE4),  # S_SKULL_DIE3
    State(SPR_SKUL, 32776, 6, A_Fall, S_SKULL_DIE5),  # S_SKULL_DIE4
    State(SPR_SKUL, 9, 6, None, S_SKULL_DIE6),  # S_SKULL_DIE5
    State(SPR_SKUL, 10, 6, None, S_NULL),  # S_SKULL_DIE6
    State(SPR_SPID, 0, 10, A_Look, S_SPID_STND2),  # S_SPID_STND
    State(SPR_SPID, 1, 10, A_Look, S_SPID_STND),  # S_SPID_STND2
    State(SPR_SPID, 0, 3, A_Metal, S_SPID_RUN2),  # S_SPID_RUN1
    State(SPR_SPID, 0, 3, A_Chase, S_SPID_RUN3),  # S_SPID_RUN2
    State(SPR_SPID, 1, 3, A_Chase, S_SPID_RUN4),  # S_SPID_RUN3
    State(SPR_SPID, 1, 3, A_Chase, S_SPID_RUN5),  # S_SPID_RUN4
    State(SPR_SPID, 2, 3, A_Metal, S_SPID_RUN6),  # S_SPID_RUN5
    State(SPR_SPID, 2, 3, A_Chase, S_SPID_RUN7),  # S_SPID_RUN6
    State(SPR_SPID, 3, 3, A_Chase, S_SPID_RUN8),  # S_SPID_RUN7
    State(SPR_SPID, 3, 3, A_Chase, S_SPID_RUN9),  # S_SPID_RUN8
    State(SPR_SPID, 4, 3, A_Metal, S_SPID_RUN10),  # S_SPID_RUN9
    State(SPR_SPID, 4, 3, A_Chase, S_SPID_RUN11),  # S_SPID_RUN10
    State(SPR_SPID, 5, 3, A_Chase, S_SPID_RUN12),  # S_SPID_RUN11
    State(SPR_SPID, 5, 3, A_Chase, S_SPID_RUN1),  # S_SPID_RUN12
    State(SPR_SPID, 32768, 20, A_FaceTarget, S_SPID_ATK2),  # S_SPID_ATK1
    State(SPR_SPID, 32774, 4, A_SPosAttack, S_SPID_ATK3),  # S_SPID_ATK2
    State(SPR_SPID, 32775, 4, A_SPosAttack, S_SPID_ATK4),  # S_SPID_ATK3
    State(SPR_SPID, 32775, 1, A_SpidRefire, S_SPID_ATK2),  # S_SPID_ATK4
    State(SPR_SPID, 8, 3, None, S_SPID_PAIN2),  # S_SPID_PAIN
    State(SPR_SPID, 8, 3, A_Pain, S_SPID_RUN1),  # S_SPID_PAIN2
    State(SPR_SPID, 9, 20, A_Scream, S_SPID_DIE2),  # S_SPID_DIE1
    State(SPR_SPID, 10, 10, A_Fall, S_SPID_DIE3),  # S_SPID_DIE2
    State(SPR_SPID, 11, 10, None, S_SPID_DIE4),  # S_SPID_DIE3
    State(SPR_SPID, 12, 10, None, S_SPID_DIE5),  # S_SPID_DIE4
    State(SPR_SPID, 13, 10, None, S_SPID_DIE6),  # S_SPID_DIE5
    State(SPR_SPID, 14, 10, None, S_SPID_DIE7),  # S_SPID_DIE6
    State(SPR_SPID, 15, 10, None, S_SPID_DIE8),  # S_SPID_DIE7
    State(SPR_SPID, 16, 10, None, S_SPID_DIE9),  # S_SPID_DIE8
    State(SPR_SPID, 17, 10, None, S_SPID_DIE10),  # S_SPID_DIE9
    State(SPR_SPID, 18, 30, None, S_SPID_DIE11),  # S_SPID_DIE10
    State(SPR_SPID, 18, -1, A_BossDeath, S_NULL),  # S_SPID_DIE11
    State(SPR_BSPI, 0, 10, A_Look, S_BSPI_STND2),  # S_BSPI_STND
    State(SPR_BSPI, 1, 10, A_Look, S_BSPI_STND),  # S_BSPI_STND2
    State(SPR_BSPI, 0, 20, None, S_BSPI_RUN1),  # S_BSPI_SIGHT
    State(SPR_BSPI, 0, 3, A_BabyMetal, S_BSPI_RUN2),  # S_BSPI_RUN1
    State(SPR_BSPI, 0, 3, A_Chase, S_BSPI_RUN3),  # S_BSPI_RUN2
    State(SPR_BSPI, 1, 3, A_Chase, S_BSPI_RUN4),  # S_BSPI_RUN3
    State(SPR_BSPI, 1, 3, A_Chase, S_BSPI_RUN5),  # S_BSPI_RUN4
    State(SPR_BSPI, 2, 3, A_Chase, S_BSPI_RUN6),  # S_BSPI_RUN5
    State(SPR_BSPI, 2, 3, A_Chase, S_BSPI_RUN7),  # S_BSPI_RUN6
    State(SPR_BSPI, 3, 3, A_BabyMetal, S_BSPI_RUN8),  # S_BSPI_RUN7
    State(SPR_BSPI, 3, 3, A_Chase, S_BSPI_RUN9),  # S_BSPI_RUN8
    State(SPR_BSPI, 4, 3, A_Chase, S_BSPI_RUN10),  # S_BSPI_RUN9
    State(SPR_BSPI, 4, 3, A_Chase, S_BSPI_RUN11),  # S_BSPI_RUN10
    State(SPR_BSPI, 5, 3, A_Chase, S_BSPI_RUN12),  # S_BSPI_RUN11
    State(SPR_BSPI, 5, 3, A_Chase, S_BSPI_RUN1),  # S_BSPI_RUN12
    State(SPR_BSPI, 32768, 20, A_FaceTarget, S_BSPI_ATK2),  # S_BSPI_ATK1
    State(SPR_BSPI, 32774, 4, A_BspiAttack, S_BSPI_ATK3),  # S_BSPI_ATK2
    State(SPR_BSPI, 32775, 4, None, S_BSPI_ATK4),  # S_BSPI_ATK3
    State(SPR_BSPI, 32775, 1, A_SpidRefire, S_BSPI_ATK2),  # S_BSPI_ATK4
    State(SPR_BSPI, 8, 3, None, S_BSPI_PAIN2),  # S_BSPI_PAIN
    State(SPR_BSPI, 8, 3, A_Pain, S_BSPI_RUN1),  # S_BSPI_PAIN2
    State(SPR_BSPI, 9, 20, A_Scream, S_BSPI_DIE2),  # S_BSPI_DIE1
    State(SPR_BSPI, 10, 7, A_Fall, S_BSPI_DIE3),  # S_BSPI_DIE2
    State(SPR_BSPI, 11, 7, None, S_BSPI_DIE4),  # S_BSPI_DIE3
    State(SPR_BSPI, 12, 7, None, S_BSPI_DIE5),  # S_BSPI_DIE4
    State(SPR_BSPI, 13, 7, None, S_BSPI_DIE6),  # S_BSPI_DIE5
    State(SPR_BSPI, 14, 7, None, S_BSPI_DIE7),  # S_BSPI_DIE6
    State(SPR_BSPI, 15, -1, A_BossDeath, S_NULL),  # S_BSPI_DIE7
    State(SPR_BSPI, 15, 5, None, S_BSPI_RAISE2),  # S_BSPI_RAISE1
    State(SPR_BSPI, 14, 5, None, S_BSPI_RAISE3),  # S_BSPI_RAISE2
    State(SPR_BSPI, 13, 5, None, S_BSPI_RAISE4),  # S_BSPI_RAISE3
    State(SPR_BSPI, 12, 5, None, S_BSPI_RAISE5),  # S_BSPI_RAISE4
    State(SPR_BSPI, 11, 5, None, S_BSPI_RAISE6),  # S_BSPI_RAISE5
    State(SPR_BSPI, 10, 5, None, S_BSPI_RAISE7),  # S_BSPI_RAISE6
    State(SPR_BSPI, 9, 5, None, S_BSPI_RUN1),  # S_BSPI_RAISE7
    State(SPR_APLS, 32768, 5, None, S_ARACH_PLAZ2),  # S_ARACH_PLAZ
    State(SPR_APLS, 32769, 5, None, S_ARACH_PLAZ),  # S_ARACH_PLAZ2
    State(SPR_APBX, 32768, 5, None, S_ARACH_PLEX2),  # S_ARACH_PLEX
    State(SPR_APBX, 32769, 5, None, S_ARACH_PLEX3),  # S_ARACH_PLEX2
    State(SPR_APBX, 32770, 5, None, S_ARACH_PLEX4),  # S_ARACH_PLEX3
    State(SPR_APBX, 32771, 5, None, S_ARACH_PLEX5),  # S_ARACH_PLEX4
    State(SPR_APBX, 32772, 5, None, S_NULL),  # S_ARACH_PLEX5
    State(SPR_CYBR, 0, 10, A_Look, S_CYBER_STND2),  # S_CYBER_STND
    State(SPR_CYBR, 1, 10, A_Look, S_CYBER_STND),  # S_CYBER_STND2
    State(SPR_CYBR, 0, 3, A_Hoof, S_CYBER_RUN2),  # S_CYBER_RUN1
    State(SPR_CYBR, 0, 3, A_Chase, S_CYBER_RUN3),  # S_CYBER_RUN2
    State(SPR_CYBR, 1, 3, A_Chase, S_CYBER_RUN4),  # S_CYBER_RUN3
    State(SPR_CYBR, 1, 3, A_Chase, S_CYBER_RUN5),  # S_CYBER_RUN4
    State(SPR_CYBR, 2, 3, A_Chase, S_CYBER_RUN6),  # S_CYBER_RUN5
    State(SPR_CYBR, 2, 3, A_Chase, S_CYBER_RUN7),  # S_CYBER_RUN6
    State(SPR_CYBR, 3, 3, A_Metal, S_CYBER_RUN8),  # S_CYBER_RUN7
    State(SPR_CYBR, 3, 3, A_Chase, S_CYBER_RUN1),  # S_CYBER_RUN8
    State(SPR_CYBR, 4, 6, A_FaceTarget, S_CYBER_ATK2),  # S_CYBER_ATK1
    State(SPR_CYBR, 5, 12, A_CyberAttack, S_CYBER_ATK3),  # S_CYBER_ATK2
    State(SPR_CYBR, 4, 12, A_FaceTarget, S_CYBER_ATK4),  # S_CYBER_ATK3
    State(SPR_CYBR, 5, 12, A_CyberAttack, S_CYBER_ATK5),  # S_CYBER_ATK4
    State(SPR_CYBR, 4, 12, A_FaceTarget, S_CYBER_ATK6),  # S_CYBER_ATK5
    State(SPR_CYBR, 5, 12, A_CyberAttack, S_CYBER_RUN1),  # S_CYBER_ATK6
    State(SPR_CYBR, 6, 10, A_Pain, S_CYBER_RUN1),  # S_CYBER_PAIN
    State(SPR_CYBR, 7, 10, None, S_CYBER_DIE2),  # S_CYBER_DIE1
    State(SPR_CYBR, 8, 10, A_Scream, S_CYBER_DIE3),  # S_CYBER_DIE2
    State(SPR_CYBR, 9, 10, None, S_CYBER_DIE4),  # S_CYBER_DIE3
    State(SPR_CYBR, 10, 10, None, S_CYBER_DIE5),  # S_CYBER_DIE4
    State(SPR_CYBR, 11, 10, None, S_CYBER_DIE6),  # S_CYBER_DIE5
    State(SPR_CYBR, 12, 10, A_Fall, S_CYBER_DIE7),  # S_CYBER_DIE6
    State(SPR_CYBR, 13, 10, None, S_CYBER_DIE8),  # S_CYBER_DIE7
    State(SPR_CYBR, 14, 10, None, S_CYBER_DIE9),  # S_CYBER_DIE8
    State(SPR_CYBR, 15, 30, None, S_CYBER_DIE10),  # S_CYBER_DIE9
    State(SPR_CYBR, 15, -1, A_BossDeath, S_NULL),  # S_CYBER_DIE10
    State(SPR_PAIN, 0, 10, A_Look, S_PAIN_STND),  # S_PAIN_STND
    State(SPR_PAIN, 0, 3, A_Chase, S_PAIN_RUN2),  # S_PAIN_RUN1
    State(SPR_PAIN, 0, 3, A_Chase, S_PAIN_RUN3),  # S_PAIN_RUN2
    State(SPR_PAIN, 1, 3, A_Chase, S_PAIN_RUN4),  # S_PAIN_RUN3
    State(SPR_PAIN, 1, 3, A_Chase, S_PAIN_RUN5),  # S_PAIN_RUN4
    State(SPR_PAIN, 2, 3, A_Chase, S_PAIN_RUN6),  # S_PAIN_RUN5
    State(SPR_PAIN, 2, 3, A_Chase, S_PAIN_RUN1),  # S_PAIN_RUN6
    State(SPR_PAIN, 3, 5, A_FaceTarget, S_PAIN_ATK2),  # S_PAIN_ATK1
    State(SPR_PAIN, 4, 5, A_FaceTarget, S_PAIN_ATK3),  # S_PAIN_ATK2
    State(SPR_PAIN, 32773, 5, A_FaceTarget, S_PAIN_ATK4),  # S_PAIN_ATK3
    State(SPR_PAIN, 32773, 0, A_PainAttack, S_PAIN_RUN1),  # S_PAIN_ATK4
    State(SPR_PAIN, 6, 6, None, S_PAIN_PAIN2),  # S_PAIN_PAIN
    State(SPR_PAIN, 6, 6, A_Pain, S_PAIN_RUN1),  # S_PAIN_PAIN2
    State(SPR_PAIN, 32775, 8, None, S_PAIN_DIE2),  # S_PAIN_DIE1
    State(SPR_PAIN, 32776, 8, A_Scream, S_PAIN_DIE3),  # S_PAIN_DIE2
    State(SPR_PAIN, 32777, 8, None, S_PAIN_DIE4),  # S_PAIN_DIE3
    State(SPR_PAIN, 32778, 8, None, S_PAIN_DIE5),  # S_PAIN_DIE4
    State(SPR_PAIN, 32779, 8, A_PainDie, S_PAIN_DIE6),  # S_PAIN_DIE5
    State(SPR_PAIN, 32780, 8, None, S_NULL),  # S_PAIN_DIE6
    State(SPR_PAIN, 12, 8, None, S_PAIN_RAISE2),  # S_PAIN_RAISE1
    State(SPR_PAIN, 11, 8, None, S_PAIN_RAISE3),  # S_PAIN_RAISE2
    State(SPR_PAIN, 10, 8, None, S_PAIN_RAISE4),  # S_PAIN_RAISE3
    State(SPR_PAIN, 9, 8, None, S_PAIN_RAISE5),  # S_PAIN_RAISE4
    State(SPR_PAIN, 8, 8, None, S_PAIN_RAISE6),  # S_PAIN_RAISE5
    State(SPR_PAIN, 7, 8, None, S_PAIN_RUN1),  # S_PAIN_RAISE6
    State(SPR_SSWV, 0, 10, A_Look, S_SSWV_STND2),  # S_SSWV_STND
    State(SPR_SSWV, 1, 10, A_Look, S_SSWV_STND),  # S_SSWV_STND2
    State(SPR_SSWV, 0, 3, A_Chase, S_SSWV_RUN2),  # S_SSWV_RUN1
    State(SPR_SSWV, 0, 3, A_Chase, S_SSWV_RUN3),  # S_SSWV_RUN2
    State(SPR_SSWV, 1, 3, A_Chase, S_SSWV_RUN4),  # S_SSWV_RUN3
    State(SPR_SSWV, 1, 3, A_Chase, S_SSWV_RUN5),  # S_SSWV_RUN4
    State(SPR_SSWV, 2, 3, A_Chase, S_SSWV_RUN6),  # S_SSWV_RUN5
    State(SPR_SSWV, 2, 3, A_Chase, S_SSWV_RUN7),  # S_SSWV_RUN6
    State(SPR_SSWV, 3, 3, A_Chase, S_SSWV_RUN8),  # S_SSWV_RUN7
    State(SPR_SSWV, 3, 3, A_Chase, S_SSWV_RUN1),  # S_SSWV_RUN8
    State(SPR_SSWV, 4, 10, A_FaceTarget, S_SSWV_ATK2),  # S_SSWV_ATK1
    State(SPR_SSWV, 5, 10, A_FaceTarget, S_SSWV_ATK3),  # S_SSWV_ATK2
    State(SPR_SSWV, 32774, 4, A_CPosAttack, S_SSWV_ATK4),  # S_SSWV_ATK3
    State(SPR_SSWV, 5, 6, A_FaceTarget, S_SSWV_ATK5),  # S_SSWV_ATK4
    State(SPR_SSWV, 32774, 4, A_CPosAttack, S_SSWV_ATK6),  # S_SSWV_ATK5
    State(SPR_SSWV, 5, 1, A_CPosRefire, S_SSWV_ATK2),  # S_SSWV_ATK6
    State(SPR_SSWV, 7, 3, None, S_SSWV_PAIN2),  # S_SSWV_PAIN
    State(SPR_SSWV, 7, 3, A_Pain, S_SSWV_RUN1),  # S_SSWV_PAIN2
    State(SPR_SSWV, 8, 5, None, S_SSWV_DIE2),  # S_SSWV_DIE1
    State(SPR_SSWV, 9, 5, A_Scream, S_SSWV_DIE3),  # S_SSWV_DIE2
    State(SPR_SSWV, 10, 5, A_Fall, S_SSWV_DIE4),  # S_SSWV_DIE3
    State(SPR_SSWV, 11, 5, None, S_SSWV_DIE5),  # S_SSWV_DIE4
    State(SPR_SSWV, 12, -1, None, S_NULL),  # S_SSWV_DIE5
    State(SPR_SSWV, 13, 5, None, S_SSWV_XDIE2),  # S_SSWV_XDIE1
    State(SPR_SSWV, 14, 5, A_XScream, S_SSWV_XDIE3),  # S_SSWV_XDIE2
    State(SPR_SSWV, 15, 5, A_Fall, S_SSWV_XDIE4),  # S_SSWV_XDIE3
    State(SPR_SSWV, 16, 5, None, S_SSWV_XDIE5),  # S_SSWV_XDIE4
    State(SPR_SSWV, 17, 5, None, S_SSWV_XDIE6),  # S_SSWV_XDIE5
    State(SPR_SSWV, 18, 5, None, S_SSWV_XDIE7),  # S_SSWV_XDIE6
    State(SPR_SSWV, 19, 5, None, S_SSWV_XDIE8),  # S_SSWV_XDIE7
    State(SPR_SSWV, 20, 5, None, S_SSWV_XDIE9),  # S_SSWV_XDIE8
    State(SPR_SSWV, 21, -1, None, S_NULL),  # S_SSWV_XDIE9
    State(SPR_SSWV, 12, 5, None, S_SSWV_RAISE2),  # S_SSWV_RAISE1
    State(SPR_SSWV, 11, 5, None, S_SSWV_RAISE3),  # S_SSWV_RAISE2
    State(SPR_SSWV, 10, 5, None, S_SSWV_RAISE4),  # S_SSWV_RAISE3
    State(SPR_SSWV, 9, 5, None, S_SSWV_RAISE5),  # S_SSWV_RAISE4
    State(SPR_SSWV, 8, 5, None, S_SSWV_RUN1),  # S_SSWV_RAISE5
    State(SPR_KEEN, 0, -1, None, S_KEENSTND),  # S_KEENSTND
    State(SPR_KEEN, 0, 6, None, S_COMMKEEN2),  # S_COMMKEEN
    State(SPR_KEEN, 1, 6, None, S_COMMKEEN3),  # S_COMMKEEN2
    State(SPR_KEEN, 2, 6, A_Scream, S_COMMKEEN4),  # S_COMMKEEN3
    State(SPR_KEEN, 3, 6, None, S_COMMKEEN5),  # S_COMMKEEN4
    State(SPR_KEEN, 4, 6, None, S_COMMKEEN6),  # S_COMMKEEN5
    State(SPR_KEEN, 5, 6, None, S_COMMKEEN7),  # S_COMMKEEN6
    State(SPR_KEEN, 6, 6, None, S_COMMKEEN8),  # S_COMMKEEN7
    State(SPR_KEEN, 7, 6, None, S_COMMKEEN9),  # S_COMMKEEN8
    State(SPR_KEEN, 8, 6, None, S_COMMKEEN10),  # S_COMMKEEN9
    State(SPR_KEEN, 9, 6, None, S_COMMKEEN11),  # S_COMMKEEN10
    State(SPR_KEEN, 10, 6, A_KeenDie, S_COMMKEEN12),  # S_COMMKEEN11
    State(SPR_KEEN, 11, -1, None, S_NULL),  # S_COMMKEEN12
    State(SPR_KEEN, 12, 4, None, S_KEENPAIN2),  # S_KEENPAIN
    State(SPR_KEEN, 12, 8, A_Pain, S_KEENSTND),  # S_KEENPAIN2
    State(SPR_BBRN, 0, -1, None, S_NULL),  # S_BRAIN
    State(SPR_BBRN, 1, 36, A_BrainPain, S_BRAIN),  # S_BRAIN_PAIN
    State(SPR_BBRN, 0, 100, A_BrainScream, S_BRAIN_DIE2),  # S_BRAIN_DIE1
    State(SPR_BBRN, 0, 10, None, S_BRAIN_DIE3),  # S_BRAIN_DIE2
    State(SPR_BBRN, 0, 10, None, S_BRAIN_DIE4),  # S_BRAIN_DIE3
    State(SPR_BBRN, 0, -1, A_BrainDie, S_NULL),  # S_BRAIN_DIE4
    State(SPR_SSWV, 0, 10, A_Look, S_BRAINEYE),  # S_BRAINEYE
    State(SPR_SSWV, 0, 181, A_BrainAwake, S_BRAINEYE1),  # S_BRAINEYESEE
    State(SPR_SSWV, 0, 150, A_BrainSpit, S_BRAINEYE1),  # S_BRAINEYE1
    State(SPR_BOSF, 32768, 3, A_SpawnSound, S_SPAWN2),  # S_SPAWN1
    State(SPR_BOSF, 32769, 3, A_SpawnFly, S_SPAWN3),  # S_SPAWN2
    State(SPR_BOSF, 32770, 3, A_SpawnFly, S_SPAWN4),  # S_SPAWN3
    State(SPR_BOSF, 32771, 3, A_SpawnFly, S_SPAWN1),  # S_SPAWN4
    State(SPR_FIRE, 32768, 4, A_Fire, S_SPAWNFIRE2),  # S_SPAWNFIRE1
    State(SPR_FIRE, 32769, 4, A_Fire, S_SPAWNFIRE3),  # S_SPAWNFIRE2
    State(SPR_FIRE, 32770, 4, A_Fire, S_SPAWNFIRE4),  # S_SPAWNFIRE3
    State(SPR_FIRE, 32771, 4, A_Fire, S_SPAWNFIRE5),  # S_SPAWNFIRE4
    State(SPR_FIRE, 32772, 4, A_Fire, S_SPAWNFIRE6),  # S_SPAWNFIRE5
    State(SPR_FIRE, 32773, 4, A_Fire, S_SPAWNFIRE7),  # S_SPAWNFIRE6
    State(SPR_FIRE, 32774, 4, A_Fire, S_SPAWNFIRE8),  # S_SPAWNFIRE7
    State(SPR_FIRE, 32775, 4, A_Fire, S_NULL),  # S_SPAWNFIRE8
    State(SPR_MISL, 32769, 10, None, S_BRAINEXPLODE2),  # S_BRAINEXPLODE1
    State(SPR_MISL, 32770, 10, None, S_BRAINEXPLODE3),  # S_BRAINEXPLODE2
    State(SPR_MISL, 32771, 10, A_BrainExplode, S_NULL),  # S_BRAINEXPLODE3
    State(SPR_ARM1, 0, 6, None, S_ARM1A),  # S_ARM1
    State(SPR_ARM1, 32769, 7, None, S_ARM1),  # S_ARM1A
    State(SPR_ARM2, 0, 6, None, S_ARM2A),  # S_ARM2
    State(SPR_ARM2, 32769, 6, None, S_ARM2),  # S_ARM2A
    State(SPR_BAR1, 0, 6, None, S_BAR2),  # S_BAR1
    State(SPR_BAR1, 1, 6, None, S_BAR1),  # S_BAR2
    State(SPR_BEXP, 32768, 5, None, S_BEXP2),  # S_BEXP
    State(SPR_BEXP, 32769, 5, A_Scream, S_BEXP3),  # S_BEXP2
    State(SPR_BEXP, 32770, 5, None, S_BEXP4),  # S_BEXP3
    State(SPR_BEXP, 32771, 10, A_Explode, S_BEXP5),  # S_BEXP4
    State(SPR_BEXP, 32772, 10, None, S_NULL),  # S_BEXP5
    State(SPR_FCAN, 32768, 4, None, S_BBAR2),  # S_BBAR1
    State(SPR_FCAN, 32769, 4, None, S_BBAR3),  # S_BBAR2
    State(SPR_FCAN, 32770, 4, None, S_BBAR1),  # S_BBAR3
    State(SPR_BON1, 0, 6, None, S_BON1A),  # S_BON1
    State(SPR_BON1, 1, 6, None, S_BON1B),  # S_BON1A
    State(SPR_BON1, 2, 6, None, S_BON1C),  # S_BON1B
    State(SPR_BON1, 3, 6, None, S_BON1D),  # S_BON1C
    State(SPR_BON1, 2, 6, None, S_BON1E),  # S_BON1D
    State(SPR_BON1, 1, 6, None, S_BON1),  # S_BON1E
    State(SPR_BON2, 0, 6, None, S_BON2A),  # S_BON2
    State(SPR_BON2, 1, 6, None, S_BON2B),  # S_BON2A
    State(SPR_BON2, 2, 6, None, S_BON2C),  # S_BON2B
    State(SPR_BON2, 3, 6, None, S_BON2D),  # S_BON2C
    State(SPR_BON2, 2, 6, None, S_BON2E),  # S_BON2D
    State(SPR_BON2, 1, 6, None, S_BON2),  # S_BON2E
    State(SPR_BKEY, 0, 10, None, S_BKEY2),  # S_BKEY
    State(SPR_BKEY, 32769, 10, None, S_BKEY),  # S_BKEY2
    State(SPR_RKEY, 0, 10, None, S_RKEY2),  # S_RKEY
    State(SPR_RKEY, 32769, 10, None, S_RKEY),  # S_RKEY2
    State(SPR_YKEY, 0, 10, None, S_YKEY2),  # S_YKEY
    State(SPR_YKEY, 32769, 10, None, S_YKEY),  # S_YKEY2
    State(SPR_BSKU, 0, 10, None, S_BSKULL2),  # S_BSKULL
    State(SPR_BSKU, 32769, 10, None, S_BSKULL),  # S_BSKULL2
    State(SPR_RSKU, 0, 10, None, S_RSKULL2),  # S_RSKULL
    State(SPR_RSKU, 32769, 10, None, S_RSKULL),  # S_RSKULL2
    State(SPR_YSKU, 0, 10, None, S_YSKULL2),  # S_YSKULL
    State(SPR_YSKU, 32769, 10, None, S_YSKULL),  # S_YSKULL2
    State(SPR_STIM, 0, -1, None, S_NULL),  # S_STIM
    State(SPR_MEDI, 0, -1, None, S_NULL),  # S_MEDI
    State(SPR_SOUL, 32768, 6, None, S_SOUL2),  # S_SOUL
    State(SPR_SOUL, 32769, 6, None, S_SOUL3),  # S_SOUL2
    State(SPR_SOUL, 32770, 6, None, S_SOUL4),  # S_SOUL3
    State(SPR_SOUL, 32771, 6, None, S_SOUL5),  # S_SOUL4
    State(SPR_SOUL, 32770, 6, None, S_SOUL6),  # S_SOUL5
    State(SPR_SOUL, 32769, 6, None, S_SOUL),  # S_SOUL6
    State(SPR_PINV, 32768, 6, None, S_PINV2),  # S_PINV
    State(SPR_PINV, 32769, 6, None, S_PINV3),  # S_PINV2
    State(SPR_PINV, 32770, 6, None, S_PINV4),  # S_PINV3
    State(SPR_PINV, 32771, 6, None, S_PINV),  # S_PINV4
    State(SPR_PSTR, 32768, -1, None, S_NULL),  # S_PSTR
    State(SPR_PINS, 32768, 6, None, S_PINS2),  # S_PINS
    State(SPR_PINS, 32769, 6, None, S_PINS3),  # S_PINS2
    State(SPR_PINS, 32770, 6, None, S_PINS4),  # S_PINS3
    State(SPR_PINS, 32771, 6, None, S_PINS),  # S_PINS4
    State(SPR_MEGA, 32768, 6, None, S_MEGA2),  # S_MEGA
    State(SPR_MEGA, 32769, 6, None, S_MEGA3),  # S_MEGA2
    State(SPR_MEGA, 32770, 6, None, S_MEGA4),  # S_MEGA3
    State(SPR_MEGA, 32771, 6, None, S_MEGA),  # S_MEGA4
    State(SPR_SUIT, 32768, -1, None, S_NULL),  # S_SUIT
    State(SPR_PMAP, 32768, 6, None, S_PMAP2),  # S_PMAP
    State(SPR_PMAP, 32769, 6, None, S_PMAP3),  # S_PMAP2
    State(SPR_PMAP, 32770, 6, None, S_PMAP4),  # S_PMAP3
    State(SPR_PMAP, 32771, 6, None, S_PMAP5),  # S_PMAP4
    State(SPR_PMAP, 32770, 6, None, S_PMAP6),  # S_PMAP5
    State(SPR_PMAP, 32769, 6, None, S_PMAP),  # S_PMAP6
    State(SPR_PVIS, 32768, 6, None, S_PVIS2),  # S_PVIS
    State(SPR_PVIS, 1, 6, None, S_PVIS),  # S_PVIS2
    State(SPR_CLIP, 0, -1, None, S_NULL),  # S_CLIP
    State(SPR_AMMO, 0, -1, None, S_NULL),  # S_AMMO
    State(SPR_ROCK, 0, -1, None, S_NULL),  # S_ROCK
    State(SPR_BROK, 0, -1, None, S_NULL),  # S_BROK
    State(SPR_CELL, 0, -1, None, S_NULL),  # S_CELL
    State(SPR_CELP, 0, -1, None, S_NULL),  # S_CELP
    State(SPR_SHEL, 0, -1, None, S_NULL),  # S_SHEL
    State(SPR_SBOX, 0, -1, None, S_NULL),  # S_SBOX
    State(SPR_BPAK, 0, -1, None, S_NULL),  # S_BPAK
    State(SPR_BFUG, 0, -1, None, S_NULL),  # S_BFUG
    State(SPR_MGUN, 0, -1, None, S_NULL),  # S_MGUN
    State(SPR_CSAW, 0, -1, None, S_NULL),  # S_CSAW
    State(SPR_LAUN, 0, -1, None, S_NULL),  # S_LAUN
    State(SPR_PLAS, 0, -1, None, S_NULL),  # S_PLAS
    State(SPR_SHOT, 0, -1, None, S_NULL),  # S_SHOT
    State(SPR_SGN2, 0, -1, None, S_NULL),  # S_SHOT2
    State(SPR_COLU, 32768, -1, None, S_NULL),  # S_COLU
    State(SPR_SMT2, 0, -1, None, S_NULL),  # S_STALAG
    State(SPR_GOR1, 0, 10, None, S_BLOODYTWITCH2),  # S_BLOODYTWITCH
    State(SPR_GOR1, 1, 15, None, S_BLOODYTWITCH3),  # S_BLOODYTWITCH2
    State(SPR_GOR1, 2, 8, None, S_BLOODYTWITCH4),  # S_BLOODYTWITCH3
    State(SPR_GOR1, 1, 6, None, S_BLOODYTWITCH),  # S_BLOODYTWITCH4
    State(SPR_PLAY, 13, -1, None, S_NULL),  # S_DEADTORSO
    State(SPR_PLAY, 18, -1, None, S_NULL),  # S_DEADBOTTOM
    State(SPR_POL2, 0, -1, None, S_NULL),  # S_HEADSONSTICK
    State(SPR_POL5, 0, -1, None, S_NULL),  # S_GIBS
    State(SPR_POL4, 0, -1, None, S_NULL),  # S_HEADONASTICK
    State(SPR_POL3, 32768, 6, None, S_HEADCANDLES2),  # S_HEADCANDLES
    State(SPR_POL3, 32769, 6, None, S_HEADCANDLES),  # S_HEADCANDLES2
    State(SPR_POL1, 0, -1, None, S_NULL),  # S_DEADSTICK
    State(SPR_POL6, 0, 6, None, S_LIVESTICK2),  # S_LIVESTICK
    State(SPR_POL6, 1, 8, None, S_LIVESTICK),  # S_LIVESTICK2
    State(SPR_GOR2, 0, -1, None, S_NULL),  # S_MEAT2
    State(SPR_GOR3, 0, -1, None, S_NULL),  # S_MEAT3
    State(SPR_GOR4, 0, -1, None, S_NULL),  # S_MEAT4
    State(SPR_GOR5, 0, -1, None, S_NULL),  # S_MEAT5
    State(SPR_SMIT, 0, -1, None, S_NULL),  # S_STALAGTITE
    State(SPR_COL1, 0, -1, None, S_NULL),  # S_TALLGRNCOL
    State(SPR_COL2, 0, -1, None, S_NULL),  # S_SHRTGRNCOL
    State(SPR_COL3, 0, -1, None, S_NULL),  # S_TALLREDCOL
    State(SPR_COL4, 0, -1, None, S_NULL),  # S_SHRTREDCOL
    State(SPR_CAND, 32768, -1, None, S_NULL),  # S_CANDLESTIK
    State(SPR_CBRA, 32768, -1, None, S_NULL),  # S_CANDELABRA
    State(SPR_COL6, 0, -1, None, S_NULL),  # S_SKULLCOL
    State(SPR_TRE1, 0, -1, None, S_NULL),  # S_TORCHTREE
    State(SPR_TRE2, 0, -1, None, S_NULL),  # S_BIGTREE
    State(SPR_ELEC, 0, -1, None, S_NULL),  # S_TECHPILLAR
    State(SPR_CEYE, 32768, 6, None, S_EVILEYE2),  # S_EVILEYE
    State(SPR_CEYE, 32769, 6, None, S_EVILEYE3),  # S_EVILEYE2
    State(SPR_CEYE, 32770, 6, None, S_EVILEYE4),  # S_EVILEYE3
    State(SPR_CEYE, 32769, 6, None, S_EVILEYE),  # S_EVILEYE4
    State(SPR_FSKU, 32768, 6, None, S_FLOATSKULL2),  # S_FLOATSKULL
    State(SPR_FSKU, 32769, 6, None, S_FLOATSKULL3),  # S_FLOATSKULL2
    State(SPR_FSKU, 32770, 6, None, S_FLOATSKULL),  # S_FLOATSKULL3
    State(SPR_COL5, 0, 14, None, S_HEARTCOL2),  # S_HEARTCOL
    State(SPR_COL5, 1, 14, None, S_HEARTCOL),  # S_HEARTCOL2
    State(SPR_TBLU, 32768, 4, None, S_BLUETORCH2),  # S_BLUETORCH
    State(SPR_TBLU, 32769, 4, None, S_BLUETORCH3),  # S_BLUETORCH2
    State(SPR_TBLU, 32770, 4, None, S_BLUETORCH4),  # S_BLUETORCH3
    State(SPR_TBLU, 32771, 4, None, S_BLUETORCH),  # S_BLUETORCH4
    State(SPR_TGRN, 32768, 4, None, S_GREENTORCH2),  # S_GREENTORCH
    State(SPR_TGRN, 32769, 4, None, S_GREENTORCH3),  # S_GREENTORCH2
    State(SPR_TGRN, 32770, 4, None, S_GREENTORCH4),  # S_GREENTORCH3
    State(SPR_TGRN, 32771, 4, None, S_GREENTORCH),  # S_GREENTORCH4
    State(SPR_TRED, 32768, 4, None, S_REDTORCH2),  # S_REDTORCH
    State(SPR_TRED, 32769, 4, None, S_REDTORCH3),  # S_REDTORCH2
    State(SPR_TRED, 32770, 4, None, S_REDTORCH4),  # S_REDTORCH3
    State(SPR_TRED, 32771, 4, None, S_REDTORCH),  # S_REDTORCH4
    State(SPR_SMBT, 32768, 4, None, S_BTORCHSHRT2),  # S_BTORCHSHRT
    State(SPR_SMBT, 32769, 4, None, S_BTORCHSHRT3),  # S_BTORCHSHRT2
    State(SPR_SMBT, 32770, 4, None, S_BTORCHSHRT4),  # S_BTORCHSHRT3
    State(SPR_SMBT, 32771, 4, None, S_BTORCHSHRT),  # S_BTORCHSHRT4
    State(SPR_SMGT, 32768, 4, None, S_GTORCHSHRT2),  # S_GTORCHSHRT
    State(SPR_SMGT, 32769, 4, None, S_GTORCHSHRT3),  # S_GTORCHSHRT2
    State(SPR_SMGT, 32770, 4, None, S_GTORCHSHRT4),  # S_GTORCHSHRT3
    State(SPR_SMGT, 32771, 4, None, S_GTORCHSHRT),  # S_GTORCHSHRT4
    State(SPR_SMRT, 32768, 4, None, S_RTORCHSHRT2),  # S_RTORCHSHRT
    State(SPR_SMRT, 32769, 4, None, S_RTORCHSHRT3),  # S_RTORCHSHRT2
    State(SPR_SMRT, 32770, 4, None, S_RTORCHSHRT4),  # S_RTORCHSHRT3
    State(SPR_SMRT, 32771, 4, None, S_RTORCHSHRT),  # S_RTORCHSHRT4
    State(SPR_HDB1, 0, -1, None, S_NULL),  # S_HANGNOGUTS
    State(SPR_HDB2, 0, -1, None, S_NULL),  # S_HANGBNOBRAIN
    State(SPR_HDB3, 0, -1, None, S_NULL),  # S_HANGTLOOKDN
    State(SPR_HDB4, 0, -1, None, S_NULL),  # S_HANGTSKULL
    State(SPR_HDB5, 0, -1, None, S_NULL),  # S_HANGTLOOKUP
    State(SPR_HDB6, 0, -1, None, S_NULL),  # S_HANGTNOBRAIN
    State(SPR_POB1, 0, -1, None, S_NULL),  # S_COLONGIBS
    State(SPR_POB2, 0, -1, None, S_NULL),  # S_SMALLPOOL
    State(SPR_BRS1, 0, -1, None, S_NULL),  # S_BRAINSTEM
    State(SPR_TLMP, 32768, 4, None, S_TECHLAMP2),  # S_TECHLAMP
    State(SPR_TLMP, 32769, 4, None, S_TECHLAMP3),  # S_TECHLAMP2
    State(SPR_TLMP, 32770, 4, None, S_TECHLAMP4),  # S_TECHLAMP3
    State(SPR_TLMP, 32771, 4, None, S_TECHLAMP),  # S_TECHLAMP4
    State(SPR_TLP2, 32768, 4, None, S_TECH2LAMP2),  # S_TECH2LAMP
    State(SPR_TLP2, 32769, 4, None, S_TECH2LAMP3),  # S_TECH2LAMP2
    State(SPR_TLP2, 32770, 4, None, S_TECH2LAMP4),  # S_TECH2LAMP3
    State(SPR_TLP2, 32771, 4, None, S_TECH2LAMP),  # S_TECH2LAMP4
]

