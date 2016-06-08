
import actions
import sprites

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

DEFAULT_STATES = [
    ("TROO", 0, -1, None, "S_NULL"),  # S_NULL
    ("SHTG", 4, 0, actions.A_Light0, "S_NULL"),  # S_LIGHTDONE
    ("PUNG", 0, 1, actions.A_WeaponReady, "S_PUNCH"),  # S_PUNCH
    ("PUNG", 0, 1, actions.A_Lower, "S_PUNCHDOWN"),  # S_PUNCHDOWN
    ("PUNG", 0, 1, actions.A_Raise, "S_PUNCHUP"),  # S_PUNCHUP
    ("PUNG", 1, 4, None, "S_PUNCH2"),  # S_PUNCH1
    ("PUNG", 2, 4, actions.A_Punch, "S_PUNCH3"),  # S_PUNCH2
    ("PUNG", 3, 5, None, "S_PUNCH4"),  # S_PUNCH3
    ("PUNG", 2, 4, None, "S_PUNCH5"),  # S_PUNCH4
    ("PUNG", 1, 5, actions.A_ReFire, "S_PUNCH"),  # S_PUNCH5
    ("PISG", 0, 1, actions.A_WeaponReady, "S_PISTOL"),  # S_PISTOL
    ("PISG", 0, 1, actions.A_Lower, "S_PISTOLDOWN"),  # S_PISTOLDOWN
    ("PISG", 0, 1, actions.A_Raise, "S_PISTOLUP"),  # S_PISTOLUP
    ("PISG", 0, 4, None, "S_PISTOL2"),  # S_PISTOL1
    ("PISG", 1, 6, actions.A_FirePistol, "S_PISTOL3"),  # S_PISTOL2
    ("PISG", 2, 4, None, "S_PISTOL4"),  # S_PISTOL3
    ("PISG", 1, 5, actions.A_ReFire, "S_PISTOL"),  # S_PISTOL4
    ("PISF", 32768, 7, actions.A_Light1, "S_LIGHTDONE"),  # S_PISTOLFLASH
    ("SHTG", 0, 1, actions.A_WeaponReady, "S_SGUN"),  # S_SGUN
    ("SHTG", 0, 1, actions.A_Lower, "S_SGUNDOWN"),  # S_SGUNDOWN
    ("SHTG", 0, 1, actions.A_Raise, "S_SGUNUP"),  # S_SGUNUP
    ("SHTG", 0, 3, None, "S_SGUN2"),  # S_SGUN1
    ("SHTG", 0, 7, actions.A_FireShotgun, "S_SGUN3"),  # S_SGUN2
    ("SHTG", 1, 5, None, "S_SGUN4"),  # S_SGUN3
    ("SHTG", 2, 5, None, "S_SGUN5"),  # S_SGUN4
    ("SHTG", 3, 4, None, "S_SGUN6"),  # S_SGUN5
    ("SHTG", 2, 5, None, "S_SGUN7"),  # S_SGUN6
    ("SHTG", 1, 5, None, "S_SGUN8"),  # S_SGUN7
    ("SHTG", 0, 3, None, "S_SGUN9"),  # S_SGUN8
    ("SHTG", 0, 7, actions.A_ReFire, "S_SGUN"),  # S_SGUN9
    ("SHTF", 32768, 4, actions.A_Light1, "S_SGUNFLASH2"),  # S_SGUNFLASH1
    ("SHTF", 32769, 3, actions.A_Light2, "S_LIGHTDONE"),  # S_SGUNFLASH2
    ("SHT2", 0, 1, actions.A_WeaponReady, "S_DSGUN"),  # S_DSGUN
    ("SHT2", 0, 1, actions.A_Lower, "S_DSGUNDOWN"),  # S_DSGUNDOWN
    ("SHT2", 0, 1, actions.A_Raise, "S_DSGUNUP"),  # S_DSGUNUP
    ("SHT2", 0, 3, None, "S_DSGUN2"),  # S_DSGUN1
    ("SHT2", 0, 7, actions.A_FireShotgun2, "S_DSGUN3"),  # S_DSGUN2
    ("SHT2", 1, 7, None, "S_DSGUN4"),  # S_DSGUN3
    ("SHT2", 2, 7, actions.A_CheckReload, "S_DSGUN5"),  # S_DSGUN4
    ("SHT2", 3, 7, actions.A_OpenShotgun2, "S_DSGUN6"),  # S_DSGUN5
    ("SHT2", 4, 7, None, "S_DSGUN7"),  # S_DSGUN6
    ("SHT2", 5, 7, actions.A_LoadShotgun2, "S_DSGUN8"),  # S_DSGUN7
    ("SHT2", 6, 6, None, "S_DSGUN9"),  # S_DSGUN8
    ("SHT2", 7, 6, actions.A_CloseShotgun2, "S_DSGUN10"),  # S_DSGUN9
    ("SHT2", 0, 5, actions.A_ReFire, "S_DSGUN"),  # S_DSGUN10
    ("SHT2", 1, 7, None, "S_DSNR2"),  # S_DSNR1
    ("SHT2", 0, 3, None, "S_DSGUNDOWN"),  # S_DSNR2
    ("SHT2", 32776, 5, actions.A_Light1, "S_DSGUNFLASH2"),  # S_DSGUNFLASH1
    ("SHT2", 32777, 4, actions.A_Light2, "S_LIGHTDONE"),  # S_DSGUNFLASH2
    ("CHGG", 0, 1, actions.A_WeaponReady, "S_CHAIN"),  # S_CHAIN
    ("CHGG", 0, 1, actions.A_Lower, "S_CHAINDOWN"),  # S_CHAINDOWN
    ("CHGG", 0, 1, actions.A_Raise, "S_CHAINUP"),  # S_CHAINUP
    ("CHGG", 0, 4, actions.A_FireCGun, "S_CHAIN2"),  # S_CHAIN1
    ("CHGG", 1, 4, actions.A_FireCGun, "S_CHAIN3"),  # S_CHAIN2
    ("CHGG", 1, 0, actions.A_ReFire, "S_CHAIN"),  # S_CHAIN3
    ("CHGF", 32768, 5, actions.A_Light1, "S_LIGHTDONE"),  # S_CHAINFLASH1
    ("CHGF", 32769, 5, actions.A_Light2, "S_LIGHTDONE"),  # S_CHAINFLASH2
    ("MISG", 0, 1, actions.A_WeaponReady, "S_MISSILE"),  # S_MISSILE
    ("MISG", 0, 1, actions.A_Lower, "S_MISSILEDOWN"),  # S_MISSILEDOWN
    ("MISG", 0, 1, actions.A_Raise, "S_MISSILEUP"),  # S_MISSILEUP
    ("MISG", 1, 8, actions.A_GunFlash, "S_MISSILE2"),  # S_MISSILE1
    ("MISG", 1, 12, actions.A_FireMissile, "S_MISSILE3"),  # S_MISSILE2
    ("MISG", 1, 0, actions.A_ReFire, "S_MISSILE"),  # S_MISSILE3
    ("MISF", 32768, 3, actions.A_Light1, "S_MISSILEFLASH2"),  # S_MISSILEFLASH1
    ("MISF", 32769, 4, None, "S_MISSILEFLASH3"),  # S_MISSILEFLASH2
    ("MISF", 32770, 4, actions.A_Light2, "S_MISSILEFLASH4"),  # S_MISSILEFLASH3
    ("MISF", 32771, 4, actions.A_Light2, "S_LIGHTDONE"),  # S_MISSILEFLASH4
    ("SAWG", 2, 4, actions.A_WeaponReady, "S_SAWB"),  # S_SAW
    ("SAWG", 3, 4, actions.A_WeaponReady, "S_SAW"),  # S_SAWB
    ("SAWG", 2, 1, actions.A_Lower, "S_SAWDOWN"),  # S_SAWDOWN
    ("SAWG", 2, 1, actions.A_Raise, "S_SAWUP"),  # S_SAWUP
    ("SAWG", 0, 4, actions.A_Saw, "S_SAW2"),  # S_SAW1
    ("SAWG", 1, 4, actions.A_Saw, "S_SAW3"),  # S_SAW2
    ("SAWG", 1, 0, actions.A_ReFire, "S_SAW"),  # S_SAW3
    ("PLSG", 0, 1, actions.A_WeaponReady, "S_PLASMA"),  # S_PLASMA
    ("PLSG", 0, 1, actions.A_Lower, "S_PLASMADOWN"),  # S_PLASMADOWN
    ("PLSG", 0, 1, actions.A_Raise, "S_PLASMAUP"),  # S_PLASMAUP
    ("PLSG", 0, 3, actions.A_FirePlasma, "S_PLASMA2"),  # S_PLASMA1
    ("PLSG", 1, 20, actions.A_ReFire, "S_PLASMA"),  # S_PLASMA2
    ("PLSF", 32768, 4, actions.A_Light1, "S_LIGHTDONE"),  # S_PLASMAFLASH1
    ("PLSF", 32769, 4, actions.A_Light1, "S_LIGHTDONE"),  # S_PLASMAFLASH2
    ("BFGG", 0, 1, actions.A_WeaponReady, "S_BFG"),  # S_BFG
    ("BFGG", 0, 1, actions.A_Lower, "S_BFGDOWN"),  # S_BFGDOWN
    ("BFGG", 0, 1, actions.A_Raise, "S_BFGUP"),  # S_BFGUP
    ("BFGG", 0, 20, actions.A_BFGsound, "S_BFG2"),  # S_BFG1
    ("BFGG", 1, 10, actions.A_GunFlash, "S_BFG3"),  # S_BFG2
    ("BFGG", 1, 10, actions.A_FireBFG, "S_BFG4"),  # S_BFG3
    ("BFGG", 1, 20, actions.A_ReFire, "S_BFG"),  # S_BFG4
    ("BFGF", 32768, 11, actions.A_Light1, "S_BFGFLASH2"),  # S_BFGFLASH1
    ("BFGF", 32769, 6, actions.A_Light2, "S_LIGHTDONE"),  # S_BFGFLASH2
    ("BLUD", 2, 8, None, "S_BLOOD2"),  # S_BLOOD1
    ("BLUD", 1, 8, None, "S_BLOOD3"),  # S_BLOOD2
    ("BLUD", 0, 8, None, "S_NULL"),  # S_BLOOD3
    ("PUFF", 32768, 4, None, "S_PUFF2"),  # S_PUFF1
    ("PUFF", 1, 4, None, "S_PUFF3"),  # S_PUFF2
    ("PUFF", 2, 4, None, "S_PUFF4"),  # S_PUFF3
    ("PUFF", 3, 4, None, "S_NULL"),  # S_PUFF4
    ("BAL1", 32768, 4, None, "S_TBALL2"),  # S_TBALL1
    ("BAL1", 32769, 4, None, "S_TBALL1"),  # S_TBALL2
    ("BAL1", 32770, 6, None, "S_TBALLX2"),  # S_TBALLX1
    ("BAL1", 32771, 6, None, "S_TBALLX3"),  # S_TBALLX2
    ("BAL1", 32772, 6, None, "S_NULL"),  # S_TBALLX3
    ("BAL2", 32768, 4, None, "S_RBALL2"),  # S_RBALL1
    ("BAL2", 32769, 4, None, "S_RBALL1"),  # S_RBALL2
    ("BAL2", 32770, 6, None, "S_RBALLX2"),  # S_RBALLX1
    ("BAL2", 32771, 6, None, "S_RBALLX3"),  # S_RBALLX2
    ("BAL2", 32772, 6, None, "S_NULL"),  # S_RBALLX3
    ("PLSS", 32768, 6, None, "S_PLASBALL2"),  # S_PLASBALL
    ("PLSS", 32769, 6, None, "S_PLASBALL"),  # S_PLASBALL2
    ("PLSE", 32768, 4, None, "S_PLASEXP2"),  # S_PLASEXP
    ("PLSE", 32769, 4, None, "S_PLASEXP3"),  # S_PLASEXP2
    ("PLSE", 32770, 4, None, "S_PLASEXP4"),  # S_PLASEXP3
    ("PLSE", 32771, 4, None, "S_PLASEXP5"),  # S_PLASEXP4
    ("PLSE", 32772, 4, None, "S_NULL"),  # S_PLASEXP5
    ("MISL", 32768, 1, None, "S_ROCKET"),  # S_ROCKET
    ("BFS1", 32768, 4, None, "S_BFGSHOT2"),  # S_BFGSHOT
    ("BFS1", 32769, 4, None, "S_BFGSHOT"),  # S_BFGSHOT2
    ("BFE1", 32768, 8, None, "S_BFGLAND2"),  # S_BFGLAND
    ("BFE1", 32769, 8, None, "S_BFGLAND3"),  # S_BFGLAND2
    ("BFE1", 32770, 8, actions.A_BFGSpray, "S_BFGLAND4"),  # S_BFGLAND3
    ("BFE1", 32771, 8, None, "S_BFGLAND5"),  # S_BFGLAND4
    ("BFE1", 32772, 8, None, "S_BFGLAND6"),  # S_BFGLAND5
    ("BFE1", 32773, 8, None, "S_NULL"),  # S_BFGLAND6
    ("BFE2", 32768, 8, None, "S_BFGEXP2"),  # S_BFGEXP
    ("BFE2", 32769, 8, None, "S_BFGEXP3"),  # S_BFGEXP2
    ("BFE2", 32770, 8, None, "S_BFGEXP4"),  # S_BFGEXP3
    ("BFE2", 32771, 8, None, "S_NULL"),  # S_BFGEXP4
    ("MISL", 32769, 8, actions.A_Explode, "S_EXPLODE2"),  # S_EXPLODE1
    ("MISL", 32770, 6, None, "S_EXPLODE3"),  # S_EXPLODE2
    ("MISL", 32771, 4, None, "S_NULL"),  # S_EXPLODE3
    ("TFOG", 32768, 6, None, "S_TFOG01"),  # S_TFOG
    ("TFOG", 32769, 6, None, "S_TFOG02"),  # S_TFOG01
    ("TFOG", 32768, 6, None, "S_TFOG2"),  # S_TFOG02
    ("TFOG", 32769, 6, None, "S_TFOG3"),  # S_TFOG2
    ("TFOG", 32770, 6, None, "S_TFOG4"),  # S_TFOG3
    ("TFOG", 32771, 6, None, "S_TFOG5"),  # S_TFOG4
    ("TFOG", 32772, 6, None, "S_TFOG6"),  # S_TFOG5
    ("TFOG", 32773, 6, None, "S_TFOG7"),  # S_TFOG6
    ("TFOG", 32774, 6, None, "S_TFOG8"),  # S_TFOG7
    ("TFOG", 32775, 6, None, "S_TFOG9"),  # S_TFOG8
    ("TFOG", 32776, 6, None, "S_TFOG10"),  # S_TFOG9
    ("TFOG", 32777, 6, None, "S_NULL"),  # S_TFOG10
    ("IFOG", 32768, 6, None, "S_IFOG01"),  # S_IFOG
    ("IFOG", 32769, 6, None, "S_IFOG02"),  # S_IFOG01
    ("IFOG", 32768, 6, None, "S_IFOG2"),  # S_IFOG02
    ("IFOG", 32769, 6, None, "S_IFOG3"),  # S_IFOG2
    ("IFOG", 32770, 6, None, "S_IFOG4"),  # S_IFOG3
    ("IFOG", 32771, 6, None, "S_IFOG5"),  # S_IFOG4
    ("IFOG", 32772, 6, None, "S_NULL"),  # S_IFOG5
    ("PLAY", 0, -1, None, "S_NULL"),  # S_PLAY
    ("PLAY", 0, 4, None, "S_PLAY_RUN2"),  # S_PLAY_RUN1
    ("PLAY", 1, 4, None, "S_PLAY_RUN3"),  # S_PLAY_RUN2
    ("PLAY", 2, 4, None, "S_PLAY_RUN4"),  # S_PLAY_RUN3
    ("PLAY", 3, 4, None, "S_PLAY_RUN1"),  # S_PLAY_RUN4
    ("PLAY", 4, 12, None, "S_PLAY"),  # S_PLAY_ATK1
    ("PLAY", 32773, 6, None, "S_PLAY_ATK1"),  # S_PLAY_ATK2
    ("PLAY", 6, 4, None, "S_PLAY_PAIN2"),  # S_PLAY_PAIN
    ("PLAY", 6, 4, actions.A_Pain, "S_PLAY"),  # S_PLAY_PAIN2
    ("PLAY", 7, 10, None, "S_PLAY_DIE2"),  # S_PLAY_DIE1
    ("PLAY", 8, 10, actions.A_PlayerScream, "S_PLAY_DIE3"),  # S_PLAY_DIE2
    ("PLAY", 9, 10, actions.A_Fall, "S_PLAY_DIE4"),  # S_PLAY_DIE3
    ("PLAY", 10, 10, None, "S_PLAY_DIE5"),  # S_PLAY_DIE4
    ("PLAY", 11, 10, None, "S_PLAY_DIE6"),  # S_PLAY_DIE5
    ("PLAY", 12, 10, None, "S_PLAY_DIE7"),  # S_PLAY_DIE6
    ("PLAY", 13, -1, None, "S_NULL"),  # S_PLAY_DIE7
    ("PLAY", 14, 5, None, "S_PLAY_XDIE2"),  # S_PLAY_XDIE1
    ("PLAY", 15, 5, actions.A_XScream, "S_PLAY_XDIE3"),  # S_PLAY_XDIE2
    ("PLAY", 16, 5, actions.A_Fall, "S_PLAY_XDIE4"),  # S_PLAY_XDIE3
    ("PLAY", 17, 5, None, "S_PLAY_XDIE5"),  # S_PLAY_XDIE4
    ("PLAY", 18, 5, None, "S_PLAY_XDIE6"),  # S_PLAY_XDIE5
    ("PLAY", 19, 5, None, "S_PLAY_XDIE7"),  # S_PLAY_XDIE6
    ("PLAY", 20, 5, None, "S_PLAY_XDIE8"),  # S_PLAY_XDIE7
    ("PLAY", 21, 5, None, "S_PLAY_XDIE9"),  # S_PLAY_XDIE8
    ("PLAY", 22, -1, None, "S_NULL"),  # S_PLAY_XDIE9
    ("POSS", 0, 10, actions.A_Look, "S_POSS_STND2"),  # S_POSS_STND
    ("POSS", 1, 10, actions.A_Look, "S_POSS_STND"),  # S_POSS_STND2
    ("POSS", 0, 4, actions.A_Chase, "S_POSS_RUN2"),  # S_POSS_RUN1
    ("POSS", 0, 4, actions.A_Chase, "S_POSS_RUN3"),  # S_POSS_RUN2
    ("POSS", 1, 4, actions.A_Chase, "S_POSS_RUN4"),  # S_POSS_RUN3
    ("POSS", 1, 4, actions.A_Chase, "S_POSS_RUN5"),  # S_POSS_RUN4
    ("POSS", 2, 4, actions.A_Chase, "S_POSS_RUN6"),  # S_POSS_RUN5
    ("POSS", 2, 4, actions.A_Chase, "S_POSS_RUN7"),  # S_POSS_RUN6
    ("POSS", 3, 4, actions.A_Chase, "S_POSS_RUN8"),  # S_POSS_RUN7
    ("POSS", 3, 4, actions.A_Chase, "S_POSS_RUN1"),  # S_POSS_RUN8
    ("POSS", 4, 10, actions.A_FaceTarget, "S_POSS_ATK2"),  # S_POSS_ATK1
    ("POSS", 5, 8, actions.A_PosAttack, "S_POSS_ATK3"),  # S_POSS_ATK2
    ("POSS", 4, 8, None, "S_POSS_RUN1"),  # S_POSS_ATK3
    ("POSS", 6, 3, None, "S_POSS_PAIN2"),  # S_POSS_PAIN
    ("POSS", 6, 3, actions.A_Pain, "S_POSS_RUN1"),  # S_POSS_PAIN2
    ("POSS", 7, 5, None, "S_POSS_DIE2"),  # S_POSS_DIE1
    ("POSS", 8, 5, actions.A_Scream, "S_POSS_DIE3"),  # S_POSS_DIE2
    ("POSS", 9, 5, actions.A_Fall, "S_POSS_DIE4"),  # S_POSS_DIE3
    ("POSS", 10, 5, None, "S_POSS_DIE5"),  # S_POSS_DIE4
    ("POSS", 11, -1, None, "S_NULL"),  # S_POSS_DIE5
    ("POSS", 12, 5, None, "S_POSS_XDIE2"),  # S_POSS_XDIE1
    ("POSS", 13, 5, actions.A_XScream, "S_POSS_XDIE3"),  # S_POSS_XDIE2
    ("POSS", 14, 5, actions.A_Fall, "S_POSS_XDIE4"),  # S_POSS_XDIE3
    ("POSS", 15, 5, None, "S_POSS_XDIE5"),  # S_POSS_XDIE4
    ("POSS", 16, 5, None, "S_POSS_XDIE6"),  # S_POSS_XDIE5
    ("POSS", 17, 5, None, "S_POSS_XDIE7"),  # S_POSS_XDIE6
    ("POSS", 18, 5, None, "S_POSS_XDIE8"),  # S_POSS_XDIE7
    ("POSS", 19, 5, None, "S_POSS_XDIE9"),  # S_POSS_XDIE8
    ("POSS", 20, -1, None, "S_NULL"),  # S_POSS_XDIE9
    ("POSS", 10, 5, None, "S_POSS_RAISE2"),  # S_POSS_RAISE1
    ("POSS", 9, 5, None, "S_POSS_RAISE3"),  # S_POSS_RAISE2
    ("POSS", 8, 5, None, "S_POSS_RAISE4"),  # S_POSS_RAISE3
    ("POSS", 7, 5, None, "S_POSS_RUN1"),  # S_POSS_RAISE4
    ("SPOS", 0, 10, actions.A_Look, "S_SPOS_STND2"),  # S_SPOS_STND
    ("SPOS", 1, 10, actions.A_Look, "S_SPOS_STND"),  # S_SPOS_STND2
    ("SPOS", 0, 3, actions.A_Chase, "S_SPOS_RUN2"),  # S_SPOS_RUN1
    ("SPOS", 0, 3, actions.A_Chase, "S_SPOS_RUN3"),  # S_SPOS_RUN2
    ("SPOS", 1, 3, actions.A_Chase, "S_SPOS_RUN4"),  # S_SPOS_RUN3
    ("SPOS", 1, 3, actions.A_Chase, "S_SPOS_RUN5"),  # S_SPOS_RUN4
    ("SPOS", 2, 3, actions.A_Chase, "S_SPOS_RUN6"),  # S_SPOS_RUN5
    ("SPOS", 2, 3, actions.A_Chase, "S_SPOS_RUN7"),  # S_SPOS_RUN6
    ("SPOS", 3, 3, actions.A_Chase, "S_SPOS_RUN8"),  # S_SPOS_RUN7
    ("SPOS", 3, 3, actions.A_Chase, "S_SPOS_RUN1"),  # S_SPOS_RUN8
    ("SPOS", 4, 10, actions.A_FaceTarget, "S_SPOS_ATK2"),  # S_SPOS_ATK1
    ("SPOS", 32773, 10, actions.A_SPosAttack, "S_SPOS_ATK3"),  # S_SPOS_ATK2
    ("SPOS", 4, 10, None, "S_SPOS_RUN1"),  # S_SPOS_ATK3
    ("SPOS", 6, 3, None, "S_SPOS_PAIN2"),  # S_SPOS_PAIN
    ("SPOS", 6, 3, actions.A_Pain, "S_SPOS_RUN1"),  # S_SPOS_PAIN2
    ("SPOS", 7, 5, None, "S_SPOS_DIE2"),  # S_SPOS_DIE1
    ("SPOS", 8, 5, actions.A_Scream, "S_SPOS_DIE3"),  # S_SPOS_DIE2
    ("SPOS", 9, 5, actions.A_Fall, "S_SPOS_DIE4"),  # S_SPOS_DIE3
    ("SPOS", 10, 5, None, "S_SPOS_DIE5"),  # S_SPOS_DIE4
    ("SPOS", 11, -1, None, "S_NULL"),  # S_SPOS_DIE5
    ("SPOS", 12, 5, None, "S_SPOS_XDIE2"),  # S_SPOS_XDIE1
    ("SPOS", 13, 5, actions.A_XScream, "S_SPOS_XDIE3"),  # S_SPOS_XDIE2
    ("SPOS", 14, 5, actions.A_Fall, "S_SPOS_XDIE4"),  # S_SPOS_XDIE3
    ("SPOS", 15, 5, None, "S_SPOS_XDIE5"),  # S_SPOS_XDIE4
    ("SPOS", 16, 5, None, "S_SPOS_XDIE6"),  # S_SPOS_XDIE5
    ("SPOS", 17, 5, None, "S_SPOS_XDIE7"),  # S_SPOS_XDIE6
    ("SPOS", 18, 5, None, "S_SPOS_XDIE8"),  # S_SPOS_XDIE7
    ("SPOS", 19, 5, None, "S_SPOS_XDIE9"),  # S_SPOS_XDIE8
    ("SPOS", 20, -1, None, "S_NULL"),  # S_SPOS_XDIE9
    ("SPOS", 11, 5, None, "S_SPOS_RAISE2"),  # S_SPOS_RAISE1
    ("SPOS", 10, 5, None, "S_SPOS_RAISE3"),  # S_SPOS_RAISE2
    ("SPOS", 9, 5, None, "S_SPOS_RAISE4"),  # S_SPOS_RAISE3
    ("SPOS", 8, 5, None, "S_SPOS_RAISE5"),  # S_SPOS_RAISE4
    ("SPOS", 7, 5, None, "S_SPOS_RUN1"),  # S_SPOS_RAISE5
    ("VILE", 0, 10, actions.A_Look, "S_VILE_STND2"),  # S_VILE_STND
    ("VILE", 1, 10, actions.A_Look, "S_VILE_STND"),  # S_VILE_STND2
    ("VILE", 0, 2, actions.A_VileChase, "S_VILE_RUN2"),  # S_VILE_RUN1
    ("VILE", 0, 2, actions.A_VileChase, "S_VILE_RUN3"),  # S_VILE_RUN2
    ("VILE", 1, 2, actions.A_VileChase, "S_VILE_RUN4"),  # S_VILE_RUN3
    ("VILE", 1, 2, actions.A_VileChase, "S_VILE_RUN5"),  # S_VILE_RUN4
    ("VILE", 2, 2, actions.A_VileChase, "S_VILE_RUN6"),  # S_VILE_RUN5
    ("VILE", 2, 2, actions.A_VileChase, "S_VILE_RUN7"),  # S_VILE_RUN6
    ("VILE", 3, 2, actions.A_VileChase, "S_VILE_RUN8"),  # S_VILE_RUN7
    ("VILE", 3, 2, actions.A_VileChase, "S_VILE_RUN9"),  # S_VILE_RUN8
    ("VILE", 4, 2, actions.A_VileChase, "S_VILE_RUN10"),  # S_VILE_RUN9
    ("VILE", 4, 2, actions.A_VileChase, "S_VILE_RUN11"),  # S_VILE_RUN10
    ("VILE", 5, 2, actions.A_VileChase, "S_VILE_RUN12"),  # S_VILE_RUN11
    ("VILE", 5, 2, actions.A_VileChase, "S_VILE_RUN1"),  # S_VILE_RUN12
    ("VILE", 32774, 0, actions.A_VileStart, "S_VILE_ATK2"),  # S_VILE_ATK1
    ("VILE", 32774, 10, actions.A_FaceTarget, "S_VILE_ATK3"),  # S_VILE_ATK2
    ("VILE", 32775, 8, actions.A_VileTarget, "S_VILE_ATK4"),  # S_VILE_ATK3
    ("VILE", 32776, 8, actions.A_FaceTarget, "S_VILE_ATK5"),  # S_VILE_ATK4
    ("VILE", 32777, 8, actions.A_FaceTarget, "S_VILE_ATK6"),  # S_VILE_ATK5
    ("VILE", 32778, 8, actions.A_FaceTarget, "S_VILE_ATK7"),  # S_VILE_ATK6
    ("VILE", 32779, 8, actions.A_FaceTarget, "S_VILE_ATK8"),  # S_VILE_ATK7
    ("VILE", 32780, 8, actions.A_FaceTarget, "S_VILE_ATK9"),  # S_VILE_ATK8
    ("VILE", 32781, 8, actions.A_FaceTarget, "S_VILE_ATK10"),  # S_VILE_ATK9
    ("VILE", 32782, 8, actions.A_VileAttack, "S_VILE_ATK11"),  # S_VILE_ATK10
    ("VILE", 32783, 20, None, "S_VILE_RUN1"),  # S_VILE_ATK11
    ("VILE", 32794, 10, None, "S_VILE_HEAL2"),  # S_VILE_HEAL1
    ("VILE", 32795, 10, None, "S_VILE_HEAL3"),  # S_VILE_HEAL2
    ("VILE", 32796, 10, None, "S_VILE_RUN1"),  # S_VILE_HEAL3
    ("VILE", 16, 5, None, "S_VILE_PAIN2"),  # S_VILE_PAIN
    ("VILE", 16, 5, actions.A_Pain, "S_VILE_RUN1"),  # S_VILE_PAIN2
    ("VILE", 16, 7, None, "S_VILE_DIE2"),  # S_VILE_DIE1
    ("VILE", 17, 7, actions.A_Scream, "S_VILE_DIE3"),  # S_VILE_DIE2
    ("VILE", 18, 7, actions.A_Fall, "S_VILE_DIE4"),  # S_VILE_DIE3
    ("VILE", 19, 7, None, "S_VILE_DIE5"),  # S_VILE_DIE4
    ("VILE", 20, 7, None, "S_VILE_DIE6"),  # S_VILE_DIE5
    ("VILE", 21, 7, None, "S_VILE_DIE7"),  # S_VILE_DIE6
    ("VILE", 22, 7, None, "S_VILE_DIE8"),  # S_VILE_DIE7
    ("VILE", 23, 5, None, "S_VILE_DIE9"),  # S_VILE_DIE8
    ("VILE", 24, 5, None, "S_VILE_DIE10"),  # S_VILE_DIE9
    ("VILE", 25, -1, None, "S_NULL"),  # S_VILE_DIE10
    ("FIRE", 32768, 2, actions.A_StartFire, "S_FIRE2"),  # S_FIRE1
    ("FIRE", 32769, 2, actions.A_Fire, "S_FIRE3"),  # S_FIRE2
    ("FIRE", 32768, 2, actions.A_Fire, "S_FIRE4"),  # S_FIRE3
    ("FIRE", 32769, 2, actions.A_Fire, "S_FIRE5"),  # S_FIRE4
    ("FIRE", 32770, 2, actions.A_FireCrackle, "S_FIRE6"),  # S_FIRE5
    ("FIRE", 32769, 2, actions.A_Fire, "S_FIRE7"),  # S_FIRE6
    ("FIRE", 32770, 2, actions.A_Fire, "S_FIRE8"),  # S_FIRE7
    ("FIRE", 32769, 2, actions.A_Fire, "S_FIRE9"),  # S_FIRE8
    ("FIRE", 32770, 2, actions.A_Fire, "S_FIRE10"),  # S_FIRE9
    ("FIRE", 32771, 2, actions.A_Fire, "S_FIRE11"),  # S_FIRE10
    ("FIRE", 32770, 2, actions.A_Fire, "S_FIRE12"),  # S_FIRE11
    ("FIRE", 32771, 2, actions.A_Fire, "S_FIRE13"),  # S_FIRE12
    ("FIRE", 32770, 2, actions.A_Fire, "S_FIRE14"),  # S_FIRE13
    ("FIRE", 32771, 2, actions.A_Fire, "S_FIRE15"),  # S_FIRE14
    ("FIRE", 32772, 2, actions.A_Fire, "S_FIRE16"),  # S_FIRE15
    ("FIRE", 32771, 2, actions.A_Fire, "S_FIRE17"),  # S_FIRE16
    ("FIRE", 32772, 2, actions.A_Fire, "S_FIRE18"),  # S_FIRE17
    ("FIRE", 32771, 2, actions.A_Fire, "S_FIRE19"),  # S_FIRE18
    ("FIRE", 32772, 2, actions.A_FireCrackle, "S_FIRE20"),  # S_FIRE19
    ("FIRE", 32773, 2, actions.A_Fire, "S_FIRE21"),  # S_FIRE20
    ("FIRE", 32772, 2, actions.A_Fire, "S_FIRE22"),  # S_FIRE21
    ("FIRE", 32773, 2, actions.A_Fire, "S_FIRE23"),  # S_FIRE22
    ("FIRE", 32772, 2, actions.A_Fire, "S_FIRE24"),  # S_FIRE23
    ("FIRE", 32773, 2, actions.A_Fire, "S_FIRE25"),  # S_FIRE24
    ("FIRE", 32774, 2, actions.A_Fire, "S_FIRE26"),  # S_FIRE25
    ("FIRE", 32775, 2, actions.A_Fire, "S_FIRE27"),  # S_FIRE26
    ("FIRE", 32774, 2, actions.A_Fire, "S_FIRE28"),  # S_FIRE27
    ("FIRE", 32775, 2, actions.A_Fire, "S_FIRE29"),  # S_FIRE28
    ("FIRE", 32774, 2, actions.A_Fire, "S_FIRE30"),  # S_FIRE29
    ("FIRE", 32775, 2, actions.A_Fire, "S_NULL"),  # S_FIRE30
    ("PUFF", 1, 4, None, "S_SMOKE2"),  # S_SMOKE1
    ("PUFF", 2, 4, None, "S_SMOKE3"),  # S_SMOKE2
    ("PUFF", 1, 4, None, "S_SMOKE4"),  # S_SMOKE3
    ("PUFF", 2, 4, None, "S_SMOKE5"),  # S_SMOKE4
    ("PUFF", 3, 4, None, "S_NULL"),  # S_SMOKE5
    ("FATB", 32768, 2, actions.A_Tracer, "S_TRACER2"),  # S_TRACER
    ("FATB", 32769, 2, actions.A_Tracer, "S_TRACER"),  # S_TRACER2
    ("FBXP", 32768, 8, None, "S_TRACEEXP2"),  # S_TRACEEXP1
    ("FBXP", 32769, 6, None, "S_TRACEEXP3"),  # S_TRACEEXP2
    ("FBXP", 32770, 4, None, "S_NULL"),  # S_TRACEEXP3
    ("SKEL", 0, 10, actions.A_Look, "S_SKEL_STND2"),  # S_SKEL_STND
    ("SKEL", 1, 10, actions.A_Look, "S_SKEL_STND"),  # S_SKEL_STND2
    ("SKEL", 0, 2, actions.A_Chase, "S_SKEL_RUN2"),  # S_SKEL_RUN1
    ("SKEL", 0, 2, actions.A_Chase, "S_SKEL_RUN3"),  # S_SKEL_RUN2
    ("SKEL", 1, 2, actions.A_Chase, "S_SKEL_RUN4"),  # S_SKEL_RUN3
    ("SKEL", 1, 2, actions.A_Chase, "S_SKEL_RUN5"),  # S_SKEL_RUN4
    ("SKEL", 2, 2, actions.A_Chase, "S_SKEL_RUN6"),  # S_SKEL_RUN5
    ("SKEL", 2, 2, actions.A_Chase, "S_SKEL_RUN7"),  # S_SKEL_RUN6
    ("SKEL", 3, 2, actions.A_Chase, "S_SKEL_RUN8"),  # S_SKEL_RUN7
    ("SKEL", 3, 2, actions.A_Chase, "S_SKEL_RUN9"),  # S_SKEL_RUN8
    ("SKEL", 4, 2, actions.A_Chase, "S_SKEL_RUN10"),  # S_SKEL_RUN9
    ("SKEL", 4, 2, actions.A_Chase, "S_SKEL_RUN11"),  # S_SKEL_RUN10
    ("SKEL", 5, 2, actions.A_Chase, "S_SKEL_RUN12"),  # S_SKEL_RUN11
    ("SKEL", 5, 2, actions.A_Chase, "S_SKEL_RUN1"),  # S_SKEL_RUN12
    ("SKEL", 6, 0, actions.A_FaceTarget, "S_SKEL_FIST2"),  # S_SKEL_FIST1
    ("SKEL", 6, 6, actions.A_SkelWhoosh, "S_SKEL_FIST3"),  # S_SKEL_FIST2
    ("SKEL", 7, 6, actions.A_FaceTarget, "S_SKEL_FIST4"),  # S_SKEL_FIST3
    ("SKEL", 8, 6, actions.A_SkelFist, "S_SKEL_RUN1"),  # S_SKEL_FIST4
    ("SKEL", 32777, 0, actions.A_FaceTarget, "S_SKEL_MISS2"),  # S_SKEL_MISS1
    ("SKEL", 32777, 10, actions.A_FaceTarget, "S_SKEL_MISS3"),  # S_SKEL_MISS2
    ("SKEL", 10, 10, actions.A_SkelMissile, "S_SKEL_MISS4"),  # S_SKEL_MISS3
    ("SKEL", 10, 10, actions.A_FaceTarget, "S_SKEL_RUN1"),  # S_SKEL_MISS4
    ("SKEL", 11, 5, None, "S_SKEL_PAIN2"),  # S_SKEL_PAIN
    ("SKEL", 11, 5, actions.A_Pain, "S_SKEL_RUN1"),  # S_SKEL_PAIN2
    ("SKEL", 11, 7, None, "S_SKEL_DIE2"),  # S_SKEL_DIE1
    ("SKEL", 12, 7, None, "S_SKEL_DIE3"),  # S_SKEL_DIE2
    ("SKEL", 13, 7, actions.A_Scream, "S_SKEL_DIE4"),  # S_SKEL_DIE3
    ("SKEL", 14, 7, actions.A_Fall, "S_SKEL_DIE5"),  # S_SKEL_DIE4
    ("SKEL", 15, 7, None, "S_SKEL_DIE6"),  # S_SKEL_DIE5
    ("SKEL", 16, -1, None, "S_NULL"),  # S_SKEL_DIE6
    ("SKEL", 16, 5, None, "S_SKEL_RAISE2"),  # S_SKEL_RAISE1
    ("SKEL", 15, 5, None, "S_SKEL_RAISE3"),  # S_SKEL_RAISE2
    ("SKEL", 14, 5, None, "S_SKEL_RAISE4"),  # S_SKEL_RAISE3
    ("SKEL", 13, 5, None, "S_SKEL_RAISE5"),  # S_SKEL_RAISE4
    ("SKEL", 12, 5, None, "S_SKEL_RAISE6"),  # S_SKEL_RAISE5
    ("SKEL", 11, 5, None, "S_SKEL_RUN1"),  # S_SKEL_RAISE6
    ("MANF", 32768, 4, None, "S_FATSHOT2"),  # S_FATSHOT1
    ("MANF", 32769, 4, None, "S_FATSHOT1"),  # S_FATSHOT2
    ("MISL", 32769, 8, None, "S_FATSHOTX2"),  # S_FATSHOTX1
    ("MISL", 32770, 6, None, "S_FATSHOTX3"),  # S_FATSHOTX2
    ("MISL", 32771, 4, None, "S_NULL"),  # S_FATSHOTX3
    ("FATT", 0, 15, actions.A_Look, "S_FATT_STND2"),  # S_FATT_STND
    ("FATT", 1, 15, actions.A_Look, "S_FATT_STND"),  # S_FATT_STND2
    ("FATT", 0, 4, actions.A_Chase, "S_FATT_RUN2"),  # S_FATT_RUN1
    ("FATT", 0, 4, actions.A_Chase, "S_FATT_RUN3"),  # S_FATT_RUN2
    ("FATT", 1, 4, actions.A_Chase, "S_FATT_RUN4"),  # S_FATT_RUN3
    ("FATT", 1, 4, actions.A_Chase, "S_FATT_RUN5"),  # S_FATT_RUN4
    ("FATT", 2, 4, actions.A_Chase, "S_FATT_RUN6"),  # S_FATT_RUN5
    ("FATT", 2, 4, actions.A_Chase, "S_FATT_RUN7"),  # S_FATT_RUN6
    ("FATT", 3, 4, actions.A_Chase, "S_FATT_RUN8"),  # S_FATT_RUN7
    ("FATT", 3, 4, actions.A_Chase, "S_FATT_RUN9"),  # S_FATT_RUN8
    ("FATT", 4, 4, actions.A_Chase, "S_FATT_RUN10"),  # S_FATT_RUN9
    ("FATT", 4, 4, actions.A_Chase, "S_FATT_RUN11"),  # S_FATT_RUN10
    ("FATT", 5, 4, actions.A_Chase, "S_FATT_RUN12"),  # S_FATT_RUN11
    ("FATT", 5, 4, actions.A_Chase, "S_FATT_RUN1"),  # S_FATT_RUN12
    ("FATT", 6, 20, actions.A_FatRaise, "S_FATT_ATK2"),  # S_FATT_ATK1
    ("FATT", 32775, 10, actions.A_FatAttack1, "S_FATT_ATK3"),  # S_FATT_ATK2
    ("FATT", 8, 5, actions.A_FaceTarget, "S_FATT_ATK4"),  # S_FATT_ATK3
    ("FATT", 6, 5, actions.A_FaceTarget, "S_FATT_ATK5"),  # S_FATT_ATK4
    ("FATT", 32775, 10, actions.A_FatAttack2, "S_FATT_ATK6"),  # S_FATT_ATK5
    ("FATT", 8, 5, actions.A_FaceTarget, "S_FATT_ATK7"),  # S_FATT_ATK6
    ("FATT", 6, 5, actions.A_FaceTarget, "S_FATT_ATK8"),  # S_FATT_ATK7
    ("FATT", 32775, 10, actions.A_FatAttack3, "S_FATT_ATK9"),  # S_FATT_ATK8
    ("FATT", 8, 5, actions.A_FaceTarget, "S_FATT_ATK10"),  # S_FATT_ATK9
    ("FATT", 6, 5, actions.A_FaceTarget, "S_FATT_RUN1"),  # S_FATT_ATK10
    ("FATT", 9, 3, None, "S_FATT_PAIN2"),  # S_FATT_PAIN
    ("FATT", 9, 3, actions.A_Pain, "S_FATT_RUN1"),  # S_FATT_PAIN2
    ("FATT", 10, 6, None, "S_FATT_DIE2"),  # S_FATT_DIE1
    ("FATT", 11, 6, actions.A_Scream, "S_FATT_DIE3"),  # S_FATT_DIE2
    ("FATT", 12, 6, actions.A_Fall, "S_FATT_DIE4"),  # S_FATT_DIE3
    ("FATT", 13, 6, None, "S_FATT_DIE5"),  # S_FATT_DIE4
    ("FATT", 14, 6, None, "S_FATT_DIE6"),  # S_FATT_DIE5
    ("FATT", 15, 6, None, "S_FATT_DIE7"),  # S_FATT_DIE6
    ("FATT", 16, 6, None, "S_FATT_DIE8"),  # S_FATT_DIE7
    ("FATT", 17, 6, None, "S_FATT_DIE9"),  # S_FATT_DIE8
    ("FATT", 18, 6, None, "S_FATT_DIE10"),  # S_FATT_DIE9
    ("FATT", 19, -1, actions.A_BossDeath, "S_NULL"),  # S_FATT_DIE10
    ("FATT", 17, 5, None, "S_FATT_RAISE2"),  # S_FATT_RAISE1
    ("FATT", 16, 5, None, "S_FATT_RAISE3"),  # S_FATT_RAISE2
    ("FATT", 15, 5, None, "S_FATT_RAISE4"),  # S_FATT_RAISE3
    ("FATT", 14, 5, None, "S_FATT_RAISE5"),  # S_FATT_RAISE4
    ("FATT", 13, 5, None, "S_FATT_RAISE6"),  # S_FATT_RAISE5
    ("FATT", 12, 5, None, "S_FATT_RAISE7"),  # S_FATT_RAISE6
    ("FATT", 11, 5, None, "S_FATT_RAISE8"),  # S_FATT_RAISE7
    ("FATT", 10, 5, None, "S_FATT_RUN1"),  # S_FATT_RAISE8
    ("CPOS", 0, 10, actions.A_Look, "S_CPOS_STND2"),  # S_CPOS_STND
    ("CPOS", 1, 10, actions.A_Look, "S_CPOS_STND"),  # S_CPOS_STND2
    ("CPOS", 0, 3, actions.A_Chase, "S_CPOS_RUN2"),  # S_CPOS_RUN1
    ("CPOS", 0, 3, actions.A_Chase, "S_CPOS_RUN3"),  # S_CPOS_RUN2
    ("CPOS", 1, 3, actions.A_Chase, "S_CPOS_RUN4"),  # S_CPOS_RUN3
    ("CPOS", 1, 3, actions.A_Chase, "S_CPOS_RUN5"),  # S_CPOS_RUN4
    ("CPOS", 2, 3, actions.A_Chase, "S_CPOS_RUN6"),  # S_CPOS_RUN5
    ("CPOS", 2, 3, actions.A_Chase, "S_CPOS_RUN7"),  # S_CPOS_RUN6
    ("CPOS", 3, 3, actions.A_Chase, "S_CPOS_RUN8"),  # S_CPOS_RUN7
    ("CPOS", 3, 3, actions.A_Chase, "S_CPOS_RUN1"),  # S_CPOS_RUN8
    ("CPOS", 4, 10, actions.A_FaceTarget, "S_CPOS_ATK2"),  # S_CPOS_ATK1
    ("CPOS", 32773, 4, actions.A_CPosAttack, "S_CPOS_ATK3"),  # S_CPOS_ATK2
    ("CPOS", 32772, 4, actions.A_CPosAttack, "S_CPOS_ATK4"),  # S_CPOS_ATK3
    ("CPOS", 5, 1, actions.A_CPosRefire, "S_CPOS_ATK2"),  # S_CPOS_ATK4
    ("CPOS", 6, 3, None, "S_CPOS_PAIN2"),  # S_CPOS_PAIN
    ("CPOS", 6, 3, actions.A_Pain, "S_CPOS_RUN1"),  # S_CPOS_PAIN2
    ("CPOS", 7, 5, None, "S_CPOS_DIE2"),  # S_CPOS_DIE1
    ("CPOS", 8, 5, actions.A_Scream, "S_CPOS_DIE3"),  # S_CPOS_DIE2
    ("CPOS", 9, 5, actions.A_Fall, "S_CPOS_DIE4"),  # S_CPOS_DIE3
    ("CPOS", 10, 5, None, "S_CPOS_DIE5"),  # S_CPOS_DIE4
    ("CPOS", 11, 5, None, "S_CPOS_DIE6"),  # S_CPOS_DIE5
    ("CPOS", 12, 5, None, "S_CPOS_DIE7"),  # S_CPOS_DIE6
    ("CPOS", 13, -1, None, "S_NULL"),  # S_CPOS_DIE7
    ("CPOS", 14, 5, None, "S_CPOS_XDIE2"),  # S_CPOS_XDIE1
    ("CPOS", 15, 5, actions.A_XScream, "S_CPOS_XDIE3"),  # S_CPOS_XDIE2
    ("CPOS", 16, 5, actions.A_Fall, "S_CPOS_XDIE4"),  # S_CPOS_XDIE3
    ("CPOS", 17, 5, None, "S_CPOS_XDIE5"),  # S_CPOS_XDIE4
    ("CPOS", 18, 5, None, "S_CPOS_XDIE6"),  # S_CPOS_XDIE5
    ("CPOS", 19, -1, None, "S_NULL"),  # S_CPOS_XDIE6
    ("CPOS", 13, 5, None, "S_CPOS_RAISE2"),  # S_CPOS_RAISE1
    ("CPOS", 12, 5, None, "S_CPOS_RAISE3"),  # S_CPOS_RAISE2
    ("CPOS", 11, 5, None, "S_CPOS_RAISE4"),  # S_CPOS_RAISE3
    ("CPOS", 10, 5, None, "S_CPOS_RAISE5"),  # S_CPOS_RAISE4
    ("CPOS", 9, 5, None, "S_CPOS_RAISE6"),  # S_CPOS_RAISE5
    ("CPOS", 8, 5, None, "S_CPOS_RAISE7"),  # S_CPOS_RAISE6
    ("CPOS", 7, 5, None, "S_CPOS_RUN1"),  # S_CPOS_RAISE7
    ("TROO", 0, 10, actions.A_Look, "S_TROO_STND2"),  # S_TROO_STND
    ("TROO", 1, 10, actions.A_Look, "S_TROO_STND"),  # S_TROO_STND2
    ("TROO", 0, 3, actions.A_Chase, "S_TROO_RUN2"),  # S_TROO_RUN1
    ("TROO", 0, 3, actions.A_Chase, "S_TROO_RUN3"),  # S_TROO_RUN2
    ("TROO", 1, 3, actions.A_Chase, "S_TROO_RUN4"),  # S_TROO_RUN3
    ("TROO", 1, 3, actions.A_Chase, "S_TROO_RUN5"),  # S_TROO_RUN4
    ("TROO", 2, 3, actions.A_Chase, "S_TROO_RUN6"),  # S_TROO_RUN5
    ("TROO", 2, 3, actions.A_Chase, "S_TROO_RUN7"),  # S_TROO_RUN6
    ("TROO", 3, 3, actions.A_Chase, "S_TROO_RUN8"),  # S_TROO_RUN7
    ("TROO", 3, 3, actions.A_Chase, "S_TROO_RUN1"),  # S_TROO_RUN8
    ("TROO", 4, 8, actions.A_FaceTarget, "S_TROO_ATK2"),  # S_TROO_ATK1
    ("TROO", 5, 8, actions.A_FaceTarget, "S_TROO_ATK3"),  # S_TROO_ATK2
    ("TROO", 6, 6, actions.A_TroopAttack, "S_TROO_RUN1"),  # S_TROO_ATK3
    ("TROO", 7, 2, None, "S_TROO_PAIN2"),  # S_TROO_PAIN
    ("TROO", 7, 2, actions.A_Pain, "S_TROO_RUN1"),  # S_TROO_PAIN2
    ("TROO", 8, 8, None, "S_TROO_DIE2"),  # S_TROO_DIE1
    ("TROO", 9, 8, actions.A_Scream, "S_TROO_DIE3"),  # S_TROO_DIE2
    ("TROO", 10, 6, None, "S_TROO_DIE4"),  # S_TROO_DIE3
    ("TROO", 11, 6, actions.A_Fall, "S_TROO_DIE5"),  # S_TROO_DIE4
    ("TROO", 12, -1, None, "S_NULL"),  # S_TROO_DIE5
    ("TROO", 13, 5, None, "S_TROO_XDIE2"),  # S_TROO_XDIE1
    ("TROO", 14, 5, actions.A_XScream, "S_TROO_XDIE3"),  # S_TROO_XDIE2
    ("TROO", 15, 5, None, "S_TROO_XDIE4"),  # S_TROO_XDIE3
    ("TROO", 16, 5, actions.A_Fall, "S_TROO_XDIE5"),  # S_TROO_XDIE4
    ("TROO", 17, 5, None, "S_TROO_XDIE6"),  # S_TROO_XDIE5
    ("TROO", 18, 5, None, "S_TROO_XDIE7"),  # S_TROO_XDIE6
    ("TROO", 19, 5, None, "S_TROO_XDIE8"),  # S_TROO_XDIE7
    ("TROO", 20, -1, None, "S_NULL"),  # S_TROO_XDIE8
    ("TROO", 12, 8, None, "S_TROO_RAISE2"),  # S_TROO_RAISE1
    ("TROO", 11, 8, None, "S_TROO_RAISE3"),  # S_TROO_RAISE2
    ("TROO", 10, 6, None, "S_TROO_RAISE4"),  # S_TROO_RAISE3
    ("TROO", 9, 6, None, "S_TROO_RAISE5"),  # S_TROO_RAISE4
    ("TROO", 8, 6, None, "S_TROO_RUN1"),  # S_TROO_RAISE5
    ("SARG", 0, 10, actions.A_Look, "S_SARG_STND2"),  # S_SARG_STND
    ("SARG", 1, 10, actions.A_Look, "S_SARG_STND"),  # S_SARG_STND2
    ("SARG", 0, 2, actions.A_Chase, "S_SARG_RUN2"),  # S_SARG_RUN1
    ("SARG", 0, 2, actions.A_Chase, "S_SARG_RUN3"),  # S_SARG_RUN2
    ("SARG", 1, 2, actions.A_Chase, "S_SARG_RUN4"),  # S_SARG_RUN3
    ("SARG", 1, 2, actions.A_Chase, "S_SARG_RUN5"),  # S_SARG_RUN4
    ("SARG", 2, 2, actions.A_Chase, "S_SARG_RUN6"),  # S_SARG_RUN5
    ("SARG", 2, 2, actions.A_Chase, "S_SARG_RUN7"),  # S_SARG_RUN6
    ("SARG", 3, 2, actions.A_Chase, "S_SARG_RUN8"),  # S_SARG_RUN7
    ("SARG", 3, 2, actions.A_Chase, "S_SARG_RUN1"),  # S_SARG_RUN8
    ("SARG", 4, 8, actions.A_FaceTarget, "S_SARG_ATK2"),  # S_SARG_ATK1
    ("SARG", 5, 8, actions.A_FaceTarget, "S_SARG_ATK3"),  # S_SARG_ATK2
    ("SARG", 6, 8, actions.A_SargAttack, "S_SARG_RUN1"),  # S_SARG_ATK3
    ("SARG", 7, 2, None, "S_SARG_PAIN2"),  # S_SARG_PAIN
    ("SARG", 7, 2, actions.A_Pain, "S_SARG_RUN1"),  # S_SARG_PAIN2
    ("SARG", 8, 8, None, "S_SARG_DIE2"),  # S_SARG_DIE1
    ("SARG", 9, 8, actions.A_Scream, "S_SARG_DIE3"),  # S_SARG_DIE2
    ("SARG", 10, 4, None, "S_SARG_DIE4"),  # S_SARG_DIE3
    ("SARG", 11, 4, actions.A_Fall, "S_SARG_DIE5"),  # S_SARG_DIE4
    ("SARG", 12, 4, None, "S_SARG_DIE6"),  # S_SARG_DIE5
    ("SARG", 13, -1, None, "S_NULL"),  # S_SARG_DIE6
    ("SARG", 13, 5, None, "S_SARG_RAISE2"),  # S_SARG_RAISE1
    ("SARG", 12, 5, None, "S_SARG_RAISE3"),  # S_SARG_RAISE2
    ("SARG", 11, 5, None, "S_SARG_RAISE4"),  # S_SARG_RAISE3
    ("SARG", 10, 5, None, "S_SARG_RAISE5"),  # S_SARG_RAISE4
    ("SARG", 9, 5, None, "S_SARG_RAISE6"),  # S_SARG_RAISE5
    ("SARG", 8, 5, None, "S_SARG_RUN1"),  # S_SARG_RAISE6
    ("HEAD", 0, 10, actions.A_Look, "S_HEAD_STND"),  # S_HEAD_STND
    ("HEAD", 0, 3, actions.A_Chase, "S_HEAD_RUN1"),  # S_HEAD_RUN1
    ("HEAD", 1, 5, actions.A_FaceTarget, "S_HEAD_ATK2"),  # S_HEAD_ATK1
    ("HEAD", 2, 5, actions.A_FaceTarget, "S_HEAD_ATK3"),  # S_HEAD_ATK2
    ("HEAD", 32771, 5, actions.A_HeadAttack, "S_HEAD_RUN1"),  # S_HEAD_ATK3
    ("HEAD", 4, 3, None, "S_HEAD_PAIN2"),  # S_HEAD_PAIN
    ("HEAD", 4, 3, actions.A_Pain, "S_HEAD_PAIN3"),  # S_HEAD_PAIN2
    ("HEAD", 5, 6, None, "S_HEAD_RUN1"),  # S_HEAD_PAIN3
    ("HEAD", 6, 8, None, "S_HEAD_DIE2"),  # S_HEAD_DIE1
    ("HEAD", 7, 8, actions.A_Scream, "S_HEAD_DIE3"),  # S_HEAD_DIE2
    ("HEAD", 8, 8, None, "S_HEAD_DIE4"),  # S_HEAD_DIE3
    ("HEAD", 9, 8, None, "S_HEAD_DIE5"),  # S_HEAD_DIE4
    ("HEAD", 10, 8, actions.A_Fall, "S_HEAD_DIE6"),  # S_HEAD_DIE5
    ("HEAD", 11, -1, None, "S_NULL"),  # S_HEAD_DIE6
    ("HEAD", 11, 8, None, "S_HEAD_RAISE2"),  # S_HEAD_RAISE1
    ("HEAD", 10, 8, None, "S_HEAD_RAISE3"),  # S_HEAD_RAISE2
    ("HEAD", 9, 8, None, "S_HEAD_RAISE4"),  # S_HEAD_RAISE3
    ("HEAD", 8, 8, None, "S_HEAD_RAISE5"),  # S_HEAD_RAISE4
    ("HEAD", 7, 8, None, "S_HEAD_RAISE6"),  # S_HEAD_RAISE5
    ("HEAD", 6, 8, None, "S_HEAD_RUN1"),  # S_HEAD_RAISE6
    ("BAL7", 32768, 4, None, "S_BRBALL2"),  # S_BRBALL1
    ("BAL7", 32769, 4, None, "S_BRBALL1"),  # S_BRBALL2
    ("BAL7", 32770, 6, None, "S_BRBALLX2"),  # S_BRBALLX1
    ("BAL7", 32771, 6, None, "S_BRBALLX3"),  # S_BRBALLX2
    ("BAL7", 32772, 6, None, "S_NULL"),  # S_BRBALLX3
    ("BOSS", 0, 10, actions.A_Look, "S_BOSS_STND2"),  # S_BOSS_STND
    ("BOSS", 1, 10, actions.A_Look, "S_BOSS_STND"),  # S_BOSS_STND2
    ("BOSS", 0, 3, actions.A_Chase, "S_BOSS_RUN2"),  # S_BOSS_RUN1
    ("BOSS", 0, 3, actions.A_Chase, "S_BOSS_RUN3"),  # S_BOSS_RUN2
    ("BOSS", 1, 3, actions.A_Chase, "S_BOSS_RUN4"),  # S_BOSS_RUN3
    ("BOSS", 1, 3, actions.A_Chase, "S_BOSS_RUN5"),  # S_BOSS_RUN4
    ("BOSS", 2, 3, actions.A_Chase, "S_BOSS_RUN6"),  # S_BOSS_RUN5
    ("BOSS", 2, 3, actions.A_Chase, "S_BOSS_RUN7"),  # S_BOSS_RUN6
    ("BOSS", 3, 3, actions.A_Chase, "S_BOSS_RUN8"),  # S_BOSS_RUN7
    ("BOSS", 3, 3, actions.A_Chase, "S_BOSS_RUN1"),  # S_BOSS_RUN8
    ("BOSS", 4, 8, actions.A_FaceTarget, "S_BOSS_ATK2"),  # S_BOSS_ATK1
    ("BOSS", 5, 8, actions.A_FaceTarget, "S_BOSS_ATK3"),  # S_BOSS_ATK2
    ("BOSS", 6, 8, actions.A_BruisAttack, "S_BOSS_RUN1"),  # S_BOSS_ATK3
    ("BOSS", 7, 2, None, "S_BOSS_PAIN2"),  # S_BOSS_PAIN
    ("BOSS", 7, 2, actions.A_Pain, "S_BOSS_RUN1"),  # S_BOSS_PAIN2
    ("BOSS", 8, 8, None, "S_BOSS_DIE2"),  # S_BOSS_DIE1
    ("BOSS", 9, 8, actions.A_Scream, "S_BOSS_DIE3"),  # S_BOSS_DIE2
    ("BOSS", 10, 8, None, "S_BOSS_DIE4"),  # S_BOSS_DIE3
    ("BOSS", 11, 8, actions.A_Fall, "S_BOSS_DIE5"),  # S_BOSS_DIE4
    ("BOSS", 12, 8, None, "S_BOSS_DIE6"),  # S_BOSS_DIE5
    ("BOSS", 13, 8, None, "S_BOSS_DIE7"),  # S_BOSS_DIE6
    ("BOSS", 14, -1, actions.A_BossDeath, "S_NULL"),  # S_BOSS_DIE7
    ("BOSS", 14, 8, None, "S_BOSS_RAISE2"),  # S_BOSS_RAISE1
    ("BOSS", 13, 8, None, "S_BOSS_RAISE3"),  # S_BOSS_RAISE2
    ("BOSS", 12, 8, None, "S_BOSS_RAISE4"),  # S_BOSS_RAISE3
    ("BOSS", 11, 8, None, "S_BOSS_RAISE5"),  # S_BOSS_RAISE4
    ("BOSS", 10, 8, None, "S_BOSS_RAISE6"),  # S_BOSS_RAISE5
    ("BOSS", 9, 8, None, "S_BOSS_RAISE7"),  # S_BOSS_RAISE6
    ("BOSS", 8, 8, None, "S_BOSS_RUN1"),  # S_BOSS_RAISE7
    ("BOS2", 0, 10, actions.A_Look, "S_BOS2_STND2"),  # S_BOS2_STND
    ("BOS2", 1, 10, actions.A_Look, "S_BOS2_STND"),  # S_BOS2_STND2
    ("BOS2", 0, 3, actions.A_Chase, "S_BOS2_RUN2"),  # S_BOS2_RUN1
    ("BOS2", 0, 3, actions.A_Chase, "S_BOS2_RUN3"),  # S_BOS2_RUN2
    ("BOS2", 1, 3, actions.A_Chase, "S_BOS2_RUN4"),  # S_BOS2_RUN3
    ("BOS2", 1, 3, actions.A_Chase, "S_BOS2_RUN5"),  # S_BOS2_RUN4
    ("BOS2", 2, 3, actions.A_Chase, "S_BOS2_RUN6"),  # S_BOS2_RUN5
    ("BOS2", 2, 3, actions.A_Chase, "S_BOS2_RUN7"),  # S_BOS2_RUN6
    ("BOS2", 3, 3, actions.A_Chase, "S_BOS2_RUN8"),  # S_BOS2_RUN7
    ("BOS2", 3, 3, actions.A_Chase, "S_BOS2_RUN1"),  # S_BOS2_RUN8
    ("BOS2", 4, 8, actions.A_FaceTarget, "S_BOS2_ATK2"),  # S_BOS2_ATK1
    ("BOS2", 5, 8, actions.A_FaceTarget, "S_BOS2_ATK3"),  # S_BOS2_ATK2
    ("BOS2", 6, 8, actions.A_BruisAttack, "S_BOS2_RUN1"),  # S_BOS2_ATK3
    ("BOS2", 7, 2, None, "S_BOS2_PAIN2"),  # S_BOS2_PAIN
    ("BOS2", 7, 2, actions.A_Pain, "S_BOS2_RUN1"),  # S_BOS2_PAIN2
    ("BOS2", 8, 8, None, "S_BOS2_DIE2"),  # S_BOS2_DIE1
    ("BOS2", 9, 8, actions.A_Scream, "S_BOS2_DIE3"),  # S_BOS2_DIE2
    ("BOS2", 10, 8, None, "S_BOS2_DIE4"),  # S_BOS2_DIE3
    ("BOS2", 11, 8, actions.A_Fall, "S_BOS2_DIE5"),  # S_BOS2_DIE4
    ("BOS2", 12, 8, None, "S_BOS2_DIE6"),  # S_BOS2_DIE5
    ("BOS2", 13, 8, None, "S_BOS2_DIE7"),  # S_BOS2_DIE6
    ("BOS2", 14, -1, None, "S_NULL"),  # S_BOS2_DIE7
    ("BOS2", 14, 8, None, "S_BOS2_RAISE2"),  # S_BOS2_RAISE1
    ("BOS2", 13, 8, None, "S_BOS2_RAISE3"),  # S_BOS2_RAISE2
    ("BOS2", 12, 8, None, "S_BOS2_RAISE4"),  # S_BOS2_RAISE3
    ("BOS2", 11, 8, None, "S_BOS2_RAISE5"),  # S_BOS2_RAISE4
    ("BOS2", 10, 8, None, "S_BOS2_RAISE6"),  # S_BOS2_RAISE5
    ("BOS2", 9, 8, None, "S_BOS2_RAISE7"),  # S_BOS2_RAISE6
    ("BOS2", 8, 8, None, "S_BOS2_RUN1"),  # S_BOS2_RAISE7
    ("SKUL", 32768, 10, actions.A_Look, "S_SKULL_STND2"),  # S_SKULL_STND
    ("SKUL", 32769, 10, actions.A_Look, "S_SKULL_STND"),  # S_SKULL_STND2
    ("SKUL", 32768, 6, actions.A_Chase, "S_SKULL_RUN2"),  # S_SKULL_RUN1
    ("SKUL", 32769, 6, actions.A_Chase, "S_SKULL_RUN1"),  # S_SKULL_RUN2
    ("SKUL", 32770, 10, actions.A_FaceTarget, "S_SKULL_ATK2"),  # S_SKULL_ATK1
    ("SKUL", 32771, 4, actions.A_SkullAttack, "S_SKULL_ATK3"),  # S_SKULL_ATK2
    ("SKUL", 32770, 4, None, "S_SKULL_ATK4"),  # S_SKULL_ATK3
    ("SKUL", 32771, 4, None, "S_SKULL_ATK3"),  # S_SKULL_ATK4
    ("SKUL", 32772, 3, None, "S_SKULL_PAIN2"),  # S_SKULL_PAIN
    ("SKUL", 32772, 3, actions.A_Pain, "S_SKULL_RUN1"),  # S_SKULL_PAIN2
    ("SKUL", 32773, 6, None, "S_SKULL_DIE2"),  # S_SKULL_DIE1
    ("SKUL", 32774, 6, actions.A_Scream, "S_SKULL_DIE3"),  # S_SKULL_DIE2
    ("SKUL", 32775, 6, None, "S_SKULL_DIE4"),  # S_SKULL_DIE3
    ("SKUL", 32776, 6, actions.A_Fall, "S_SKULL_DIE5"),  # S_SKULL_DIE4
    ("SKUL", 9, 6, None, "S_SKULL_DIE6"),  # S_SKULL_DIE5
    ("SKUL", 10, 6, None, "S_NULL"),  # S_SKULL_DIE6
    ("SPID", 0, 10, actions.A_Look, "S_SPID_STND2"),  # S_SPID_STND
    ("SPID", 1, 10, actions.A_Look, "S_SPID_STND"),  # S_SPID_STND2
    ("SPID", 0, 3, actions.A_Metal, "S_SPID_RUN2"),  # S_SPID_RUN1
    ("SPID", 0, 3, actions.A_Chase, "S_SPID_RUN3"),  # S_SPID_RUN2
    ("SPID", 1, 3, actions.A_Chase, "S_SPID_RUN4"),  # S_SPID_RUN3
    ("SPID", 1, 3, actions.A_Chase, "S_SPID_RUN5"),  # S_SPID_RUN4
    ("SPID", 2, 3, actions.A_Metal, "S_SPID_RUN6"),  # S_SPID_RUN5
    ("SPID", 2, 3, actions.A_Chase, "S_SPID_RUN7"),  # S_SPID_RUN6
    ("SPID", 3, 3, actions.A_Chase, "S_SPID_RUN8"),  # S_SPID_RUN7
    ("SPID", 3, 3, actions.A_Chase, "S_SPID_RUN9"),  # S_SPID_RUN8
    ("SPID", 4, 3, actions.A_Metal, "S_SPID_RUN10"),  # S_SPID_RUN9
    ("SPID", 4, 3, actions.A_Chase, "S_SPID_RUN11"),  # S_SPID_RUN10
    ("SPID", 5, 3, actions.A_Chase, "S_SPID_RUN12"),  # S_SPID_RUN11
    ("SPID", 5, 3, actions.A_Chase, "S_SPID_RUN1"),  # S_SPID_RUN12
    ("SPID", 32768, 20, actions.A_FaceTarget, "S_SPID_ATK2"),  # S_SPID_ATK1
    ("SPID", 32774, 4, actions.A_SPosAttack, "S_SPID_ATK3"),  # S_SPID_ATK2
    ("SPID", 32775, 4, actions.A_SPosAttack, "S_SPID_ATK4"),  # S_SPID_ATK3
    ("SPID", 32775, 1, actions.A_SpidRefire, "S_SPID_ATK2"),  # S_SPID_ATK4
    ("SPID", 8, 3, None, "S_SPID_PAIN2"),  # S_SPID_PAIN
    ("SPID", 8, 3, actions.A_Pain, "S_SPID_RUN1"),  # S_SPID_PAIN2
    ("SPID", 9, 20, actions.A_Scream, "S_SPID_DIE2"),  # S_SPID_DIE1
    ("SPID", 10, 10, actions.A_Fall, "S_SPID_DIE3"),  # S_SPID_DIE2
    ("SPID", 11, 10, None, "S_SPID_DIE4"),  # S_SPID_DIE3
    ("SPID", 12, 10, None, "S_SPID_DIE5"),  # S_SPID_DIE4
    ("SPID", 13, 10, None, "S_SPID_DIE6"),  # S_SPID_DIE5
    ("SPID", 14, 10, None, "S_SPID_DIE7"),  # S_SPID_DIE6
    ("SPID", 15, 10, None, "S_SPID_DIE8"),  # S_SPID_DIE7
    ("SPID", 16, 10, None, "S_SPID_DIE9"),  # S_SPID_DIE8
    ("SPID", 17, 10, None, "S_SPID_DIE10"),  # S_SPID_DIE9
    ("SPID", 18, 30, None, "S_SPID_DIE11"),  # S_SPID_DIE10
    ("SPID", 18, -1, actions.A_BossDeath, "S_NULL"),  # S_SPID_DIE11
    ("BSPI", 0, 10, actions.A_Look, "S_BSPI_STND2"),  # S_BSPI_STND
    ("BSPI", 1, 10, actions.A_Look, "S_BSPI_STND"),  # S_BSPI_STND2
    ("BSPI", 0, 20, None, "S_BSPI_RUN1"),  # S_BSPI_SIGHT
    ("BSPI", 0, 3, actions.A_BabyMetal, "S_BSPI_RUN2"),  # S_BSPI_RUN1
    ("BSPI", 0, 3, actions.A_Chase, "S_BSPI_RUN3"),  # S_BSPI_RUN2
    ("BSPI", 1, 3, actions.A_Chase, "S_BSPI_RUN4"),  # S_BSPI_RUN3
    ("BSPI", 1, 3, actions.A_Chase, "S_BSPI_RUN5"),  # S_BSPI_RUN4
    ("BSPI", 2, 3, actions.A_Chase, "S_BSPI_RUN6"),  # S_BSPI_RUN5
    ("BSPI", 2, 3, actions.A_Chase, "S_BSPI_RUN7"),  # S_BSPI_RUN6
    ("BSPI", 3, 3, actions.A_BabyMetal, "S_BSPI_RUN8"),  # S_BSPI_RUN7
    ("BSPI", 3, 3, actions.A_Chase, "S_BSPI_RUN9"),  # S_BSPI_RUN8
    ("BSPI", 4, 3, actions.A_Chase, "S_BSPI_RUN10"),  # S_BSPI_RUN9
    ("BSPI", 4, 3, actions.A_Chase, "S_BSPI_RUN11"),  # S_BSPI_RUN10
    ("BSPI", 5, 3, actions.A_Chase, "S_BSPI_RUN12"),  # S_BSPI_RUN11
    ("BSPI", 5, 3, actions.A_Chase, "S_BSPI_RUN1"),  # S_BSPI_RUN12
    ("BSPI", 32768, 20, actions.A_FaceTarget, "S_BSPI_ATK2"),  # S_BSPI_ATK1
    ("BSPI", 32774, 4, actions.A_BspiAttack, "S_BSPI_ATK3"),  # S_BSPI_ATK2
    ("BSPI", 32775, 4, None, "S_BSPI_ATK4"),  # S_BSPI_ATK3
    ("BSPI", 32775, 1, actions.A_SpidRefire, "S_BSPI_ATK2"),  # S_BSPI_ATK4
    ("BSPI", 8, 3, None, "S_BSPI_PAIN2"),  # S_BSPI_PAIN
    ("BSPI", 8, 3, actions.A_Pain, "S_BSPI_RUN1"),  # S_BSPI_PAIN2
    ("BSPI", 9, 20, actions.A_Scream, "S_BSPI_DIE2"),  # S_BSPI_DIE1
    ("BSPI", 10, 7, actions.A_Fall, "S_BSPI_DIE3"),  # S_BSPI_DIE2
    ("BSPI", 11, 7, None, "S_BSPI_DIE4"),  # S_BSPI_DIE3
    ("BSPI", 12, 7, None, "S_BSPI_DIE5"),  # S_BSPI_DIE4
    ("BSPI", 13, 7, None, "S_BSPI_DIE6"),  # S_BSPI_DIE5
    ("BSPI", 14, 7, None, "S_BSPI_DIE7"),  # S_BSPI_DIE6
    ("BSPI", 15, -1, actions.A_BossDeath, "S_NULL"),  # S_BSPI_DIE7
    ("BSPI", 15, 5, None, "S_BSPI_RAISE2"),  # S_BSPI_RAISE1
    ("BSPI", 14, 5, None, "S_BSPI_RAISE3"),  # S_BSPI_RAISE2
    ("BSPI", 13, 5, None, "S_BSPI_RAISE4"),  # S_BSPI_RAISE3
    ("BSPI", 12, 5, None, "S_BSPI_RAISE5"),  # S_BSPI_RAISE4
    ("BSPI", 11, 5, None, "S_BSPI_RAISE6"),  # S_BSPI_RAISE5
    ("BSPI", 10, 5, None, "S_BSPI_RAISE7"),  # S_BSPI_RAISE6
    ("BSPI", 9, 5, None, "S_BSPI_RUN1"),  # S_BSPI_RAISE7
    ("APLS", 32768, 5, None, "S_ARACH_PLAZ2"),  # S_ARACH_PLAZ
    ("APLS", 32769, 5, None, "S_ARACH_PLAZ"),  # S_ARACH_PLAZ2
    ("APBX", 32768, 5, None, "S_ARACH_PLEX2"),  # S_ARACH_PLEX
    ("APBX", 32769, 5, None, "S_ARACH_PLEX3"),  # S_ARACH_PLEX2
    ("APBX", 32770, 5, None, "S_ARACH_PLEX4"),  # S_ARACH_PLEX3
    ("APBX", 32771, 5, None, "S_ARACH_PLEX5"),  # S_ARACH_PLEX4
    ("APBX", 32772, 5, None, "S_NULL"),  # S_ARACH_PLEX5
    ("CYBR", 0, 10, actions.A_Look, "S_CYBER_STND2"),  # S_CYBER_STND
    ("CYBR", 1, 10, actions.A_Look, "S_CYBER_STND"),  # S_CYBER_STND2
    ("CYBR", 0, 3, actions.A_Hoof, "S_CYBER_RUN2"),  # S_CYBER_RUN1
    ("CYBR", 0, 3, actions.A_Chase, "S_CYBER_RUN3"),  # S_CYBER_RUN2
    ("CYBR", 1, 3, actions.A_Chase, "S_CYBER_RUN4"),  # S_CYBER_RUN3
    ("CYBR", 1, 3, actions.A_Chase, "S_CYBER_RUN5"),  # S_CYBER_RUN4
    ("CYBR", 2, 3, actions.A_Chase, "S_CYBER_RUN6"),  # S_CYBER_RUN5
    ("CYBR", 2, 3, actions.A_Chase, "S_CYBER_RUN7"),  # S_CYBER_RUN6
    ("CYBR", 3, 3, actions.A_Metal, "S_CYBER_RUN8"),  # S_CYBER_RUN7
    ("CYBR", 3, 3, actions.A_Chase, "S_CYBER_RUN1"),  # S_CYBER_RUN8
    ("CYBR", 4, 6, actions.A_FaceTarget, "S_CYBER_ATK2"),  # S_CYBER_ATK1
    ("CYBR", 5, 12, actions.A_CyberAttack, "S_CYBER_ATK3"),  # S_CYBER_ATK2
    ("CYBR", 4, 12, actions.A_FaceTarget, "S_CYBER_ATK4"),  # S_CYBER_ATK3
    ("CYBR", 5, 12, actions.A_CyberAttack, "S_CYBER_ATK5"),  # S_CYBER_ATK4
    ("CYBR", 4, 12, actions.A_FaceTarget, "S_CYBER_ATK6"),  # S_CYBER_ATK5
    ("CYBR", 5, 12, actions.A_CyberAttack, "S_CYBER_RUN1"),  # S_CYBER_ATK6
    ("CYBR", 6, 10, actions.A_Pain, "S_CYBER_RUN1"),  # S_CYBER_PAIN
    ("CYBR", 7, 10, None, "S_CYBER_DIE2"),  # S_CYBER_DIE1
    ("CYBR", 8, 10, actions.A_Scream, "S_CYBER_DIE3"),  # S_CYBER_DIE2
    ("CYBR", 9, 10, None, "S_CYBER_DIE4"),  # S_CYBER_DIE3
    ("CYBR", 10, 10, None, "S_CYBER_DIE5"),  # S_CYBER_DIE4
    ("CYBR", 11, 10, None, "S_CYBER_DIE6"),  # S_CYBER_DIE5
    ("CYBR", 12, 10, actions.A_Fall, "S_CYBER_DIE7"),  # S_CYBER_DIE6
    ("CYBR", 13, 10, None, "S_CYBER_DIE8"),  # S_CYBER_DIE7
    ("CYBR", 14, 10, None, "S_CYBER_DIE9"),  # S_CYBER_DIE8
    ("CYBR", 15, 30, None, "S_CYBER_DIE10"),  # S_CYBER_DIE9
    ("CYBR", 15, -1, actions.A_BossDeath, "S_NULL"),  # S_CYBER_DIE10
    ("PAIN", 0, 10, actions.A_Look, "S_PAIN_STND"),  # S_PAIN_STND
    ("PAIN", 0, 3, actions.A_Chase, "S_PAIN_RUN2"),  # S_PAIN_RUN1
    ("PAIN", 0, 3, actions.A_Chase, "S_PAIN_RUN3"),  # S_PAIN_RUN2
    ("PAIN", 1, 3, actions.A_Chase, "S_PAIN_RUN4"),  # S_PAIN_RUN3
    ("PAIN", 1, 3, actions.A_Chase, "S_PAIN_RUN5"),  # S_PAIN_RUN4
    ("PAIN", 2, 3, actions.A_Chase, "S_PAIN_RUN6"),  # S_PAIN_RUN5
    ("PAIN", 2, 3, actions.A_Chase, "S_PAIN_RUN1"),  # S_PAIN_RUN6
    ("PAIN", 3, 5, actions.A_FaceTarget, "S_PAIN_ATK2"),  # S_PAIN_ATK1
    ("PAIN", 4, 5, actions.A_FaceTarget, "S_PAIN_ATK3"),  # S_PAIN_ATK2
    ("PAIN", 32773, 5, actions.A_FaceTarget, "S_PAIN_ATK4"),  # S_PAIN_ATK3
    ("PAIN", 32773, 0, actions.A_PainAttack, "S_PAIN_RUN1"),  # S_PAIN_ATK4
    ("PAIN", 6, 6, None, "S_PAIN_PAIN2"),  # S_PAIN_PAIN
    ("PAIN", 6, 6, actions.A_Pain, "S_PAIN_RUN1"),  # S_PAIN_PAIN2
    ("PAIN", 32775, 8, None, "S_PAIN_DIE2"),  # S_PAIN_DIE1
    ("PAIN", 32776, 8, actions.A_Scream, "S_PAIN_DIE3"),  # S_PAIN_DIE2
    ("PAIN", 32777, 8, None, "S_PAIN_DIE4"),  # S_PAIN_DIE3
    ("PAIN", 32778, 8, None, "S_PAIN_DIE5"),  # S_PAIN_DIE4
    ("PAIN", 32779, 8, actions.A_PainDie, "S_PAIN_DIE6"),  # S_PAIN_DIE5
    ("PAIN", 32780, 8, None, "S_NULL"),  # S_PAIN_DIE6
    ("PAIN", 12, 8, None, "S_PAIN_RAISE2"),  # S_PAIN_RAISE1
    ("PAIN", 11, 8, None, "S_PAIN_RAISE3"),  # S_PAIN_RAISE2
    ("PAIN", 10, 8, None, "S_PAIN_RAISE4"),  # S_PAIN_RAISE3
    ("PAIN", 9, 8, None, "S_PAIN_RAISE5"),  # S_PAIN_RAISE4
    ("PAIN", 8, 8, None, "S_PAIN_RAISE6"),  # S_PAIN_RAISE5
    ("PAIN", 7, 8, None, "S_PAIN_RUN1"),  # S_PAIN_RAISE6
    ("SSWV", 0, 10, actions.A_Look, "S_SSWV_STND2"),  # S_SSWV_STND
    ("SSWV", 1, 10, actions.A_Look, "S_SSWV_STND"),  # S_SSWV_STND2
    ("SSWV", 0, 3, actions.A_Chase, "S_SSWV_RUN2"),  # S_SSWV_RUN1
    ("SSWV", 0, 3, actions.A_Chase, "S_SSWV_RUN3"),  # S_SSWV_RUN2
    ("SSWV", 1, 3, actions.A_Chase, "S_SSWV_RUN4"),  # S_SSWV_RUN3
    ("SSWV", 1, 3, actions.A_Chase, "S_SSWV_RUN5"),  # S_SSWV_RUN4
    ("SSWV", 2, 3, actions.A_Chase, "S_SSWV_RUN6"),  # S_SSWV_RUN5
    ("SSWV", 2, 3, actions.A_Chase, "S_SSWV_RUN7"),  # S_SSWV_RUN6
    ("SSWV", 3, 3, actions.A_Chase, "S_SSWV_RUN8"),  # S_SSWV_RUN7
    ("SSWV", 3, 3, actions.A_Chase, "S_SSWV_RUN1"),  # S_SSWV_RUN8
    ("SSWV", 4, 10, actions.A_FaceTarget, "S_SSWV_ATK2"),  # S_SSWV_ATK1
    ("SSWV", 5, 10, actions.A_FaceTarget, "S_SSWV_ATK3"),  # S_SSWV_ATK2
    ("SSWV", 32774, 4, actions.A_CPosAttack, "S_SSWV_ATK4"),  # S_SSWV_ATK3
    ("SSWV", 5, 6, actions.A_FaceTarget, "S_SSWV_ATK5"),  # S_SSWV_ATK4
    ("SSWV", 32774, 4, actions.A_CPosAttack, "S_SSWV_ATK6"),  # S_SSWV_ATK5
    ("SSWV", 5, 1, actions.A_CPosRefire, "S_SSWV_ATK2"),  # S_SSWV_ATK6
    ("SSWV", 7, 3, None, "S_SSWV_PAIN2"),  # S_SSWV_PAIN
    ("SSWV", 7, 3, actions.A_Pain, "S_SSWV_RUN1"),  # S_SSWV_PAIN2
    ("SSWV", 8, 5, None, "S_SSWV_DIE2"),  # S_SSWV_DIE1
    ("SSWV", 9, 5, actions.A_Scream, "S_SSWV_DIE3"),  # S_SSWV_DIE2
    ("SSWV", 10, 5, actions.A_Fall, "S_SSWV_DIE4"),  # S_SSWV_DIE3
    ("SSWV", 11, 5, None, "S_SSWV_DIE5"),  # S_SSWV_DIE4
    ("SSWV", 12, -1, None, "S_NULL"),  # S_SSWV_DIE5
    ("SSWV", 13, 5, None, "S_SSWV_XDIE2"),  # S_SSWV_XDIE1
    ("SSWV", 14, 5, actions.A_XScream, "S_SSWV_XDIE3"),  # S_SSWV_XDIE2
    ("SSWV", 15, 5, actions.A_Fall, "S_SSWV_XDIE4"),  # S_SSWV_XDIE3
    ("SSWV", 16, 5, None, "S_SSWV_XDIE5"),  # S_SSWV_XDIE4
    ("SSWV", 17, 5, None, "S_SSWV_XDIE6"),  # S_SSWV_XDIE5
    ("SSWV", 18, 5, None, "S_SSWV_XDIE7"),  # S_SSWV_XDIE6
    ("SSWV", 19, 5, None, "S_SSWV_XDIE8"),  # S_SSWV_XDIE7
    ("SSWV", 20, 5, None, "S_SSWV_XDIE9"),  # S_SSWV_XDIE8
    ("SSWV", 21, -1, None, "S_NULL"),  # S_SSWV_XDIE9
    ("SSWV", 12, 5, None, "S_SSWV_RAISE2"),  # S_SSWV_RAISE1
    ("SSWV", 11, 5, None, "S_SSWV_RAISE3"),  # S_SSWV_RAISE2
    ("SSWV", 10, 5, None, "S_SSWV_RAISE4"),  # S_SSWV_RAISE3
    ("SSWV", 9, 5, None, "S_SSWV_RAISE5"),  # S_SSWV_RAISE4
    ("SSWV", 8, 5, None, "S_SSWV_RUN1"),  # S_SSWV_RAISE5
    ("KEEN", 0, -1, None, "S_KEENSTND"),  # S_KEENSTND
    ("KEEN", 0, 6, None, "S_COMMKEEN2"),  # S_COMMKEEN
    ("KEEN", 1, 6, None, "S_COMMKEEN3"),  # S_COMMKEEN2
    ("KEEN", 2, 6, actions.A_Scream, "S_COMMKEEN4"),  # S_COMMKEEN3
    ("KEEN", 3, 6, None, "S_COMMKEEN5"),  # S_COMMKEEN4
    ("KEEN", 4, 6, None, "S_COMMKEEN6"),  # S_COMMKEEN5
    ("KEEN", 5, 6, None, "S_COMMKEEN7"),  # S_COMMKEEN6
    ("KEEN", 6, 6, None, "S_COMMKEEN8"),  # S_COMMKEEN7
    ("KEEN", 7, 6, None, "S_COMMKEEN9"),  # S_COMMKEEN8
    ("KEEN", 8, 6, None, "S_COMMKEEN10"),  # S_COMMKEEN9
    ("KEEN", 9, 6, None, "S_COMMKEEN11"),  # S_COMMKEEN10
    ("KEEN", 10, 6, actions.A_KeenDie, "S_COMMKEEN12"),  # S_COMMKEEN11
    ("KEEN", 11, -1, None, "S_NULL"),  # S_COMMKEEN12
    ("KEEN", 12, 4, None, "S_KEENPAIN2"),  # S_KEENPAIN
    ("KEEN", 12, 8, actions.A_Pain, "S_KEENSTND"),  # S_KEENPAIN2
    ("BBRN", 0, -1, None, "S_NULL"),  # S_BRAIN
    ("BBRN", 1, 36, actions.A_BrainPain, "S_BRAIN"),  # S_BRAIN_PAIN
    ("BBRN", 0, 100, actions.A_BrainScream, "S_BRAIN_DIE2"),  # S_BRAIN_DIE1
    ("BBRN", 0, 10, None, "S_BRAIN_DIE3"),  # S_BRAIN_DIE2
    ("BBRN", 0, 10, None, "S_BRAIN_DIE4"),  # S_BRAIN_DIE3
    ("BBRN", 0, -1, actions.A_BrainDie, "S_NULL"),  # S_BRAIN_DIE4
    ("SSWV", 0, 10, actions.A_Look, "S_BRAINEYE"),  # S_BRAINEYE
    ("SSWV", 0, 181, actions.A_BrainAwake, "S_BRAINEYE1"),  # S_BRAINEYESEE
    ("SSWV", 0, 150, actions.A_BrainSpit, "S_BRAINEYE1"),  # S_BRAINEYE1
    ("BOSF", 32768, 3, actions.A_SpawnSound, "S_SPAWN2"),  # S_SPAWN1
    ("BOSF", 32769, 3, actions.A_SpawnFly, "S_SPAWN3"),  # S_SPAWN2
    ("BOSF", 32770, 3, actions.A_SpawnFly, "S_SPAWN4"),  # S_SPAWN3
    ("BOSF", 32771, 3, actions.A_SpawnFly, "S_SPAWN1"),  # S_SPAWN4
    ("FIRE", 32768, 4, actions.A_Fire, "S_SPAWNFIRE2"),  # S_SPAWNFIRE1
    ("FIRE", 32769, 4, actions.A_Fire, "S_SPAWNFIRE3"),  # S_SPAWNFIRE2
    ("FIRE", 32770, 4, actions.A_Fire, "S_SPAWNFIRE4"),  # S_SPAWNFIRE3
    ("FIRE", 32771, 4, actions.A_Fire, "S_SPAWNFIRE5"),  # S_SPAWNFIRE4
    ("FIRE", 32772, 4, actions.A_Fire, "S_SPAWNFIRE6"),  # S_SPAWNFIRE5
    ("FIRE", 32773, 4, actions.A_Fire, "S_SPAWNFIRE7"),  # S_SPAWNFIRE6
    ("FIRE", 32774, 4, actions.A_Fire, "S_SPAWNFIRE8"),  # S_SPAWNFIRE7
    ("FIRE", 32775, 4, actions.A_Fire, "S_NULL"),  # S_SPAWNFIRE8
    ("MISL", 32769, 10, None, "S_BRAINEXPLODE2"),  # S_BRAINEXPLODE1
    ("MISL", 32770, 10, None, "S_BRAINEXPLODE3"),  # S_BRAINEXPLODE2
    ("MISL", 32771, 10, actions.A_BrainExplode, "S_NULL"),  # S_BRAINEXPLODE3
    ("ARM1", 0, 6, None, "S_ARM1A"),  # S_ARM1
    ("ARM1", 32769, 7, None, "S_ARM1"),  # S_ARM1A
    ("ARM2", 0, 6, None, "S_ARM2A"),  # S_ARM2
    ("ARM2", 32769, 6, None, "S_ARM2"),  # S_ARM2A
    ("BAR1", 0, 6, None, "S_BAR2"),  # S_BAR1
    ("BAR1", 1, 6, None, "S_BAR1"),  # S_BAR2
    ("BEXP", 32768, 5, None, "S_BEXP2"),  # S_BEXP
    ("BEXP", 32769, 5, actions.A_Scream, "S_BEXP3"),  # S_BEXP2
    ("BEXP", 32770, 5, None, "S_BEXP4"),  # S_BEXP3
    ("BEXP", 32771, 10, actions.A_Explode, "S_BEXP5"),  # S_BEXP4
    ("BEXP", 32772, 10, None, "S_NULL"),  # S_BEXP5
    ("FCAN", 32768, 4, None, "S_BBAR2"),  # S_BBAR1
    ("FCAN", 32769, 4, None, "S_BBAR3"),  # S_BBAR2
    ("FCAN", 32770, 4, None, "S_BBAR1"),  # S_BBAR3
    ("BON1", 0, 6, None, "S_BON1A"),  # S_BON1
    ("BON1", 1, 6, None, "S_BON1B"),  # S_BON1A
    ("BON1", 2, 6, None, "S_BON1C"),  # S_BON1B
    ("BON1", 3, 6, None, "S_BON1D"),  # S_BON1C
    ("BON1", 2, 6, None, "S_BON1E"),  # S_BON1D
    ("BON1", 1, 6, None, "S_BON1"),  # S_BON1E
    ("BON2", 0, 6, None, "S_BON2A"),  # S_BON2
    ("BON2", 1, 6, None, "S_BON2B"),  # S_BON2A
    ("BON2", 2, 6, None, "S_BON2C"),  # S_BON2B
    ("BON2", 3, 6, None, "S_BON2D"),  # S_BON2C
    ("BON2", 2, 6, None, "S_BON2E"),  # S_BON2D
    ("BON2", 1, 6, None, "S_BON2"),  # S_BON2E
    ("BKEY", 0, 10, None, "S_BKEY2"),  # S_BKEY
    ("BKEY", 32769, 10, None, "S_BKEY"),  # S_BKEY2
    ("RKEY", 0, 10, None, "S_RKEY2"),  # S_RKEY
    ("RKEY", 32769, 10, None, "S_RKEY"),  # S_RKEY2
    ("YKEY", 0, 10, None, "S_YKEY2"),  # S_YKEY
    ("YKEY", 32769, 10, None, "S_YKEY"),  # S_YKEY2
    ("BSKU", 0, 10, None, "S_BSKULL2"),  # S_BSKULL
    ("BSKU", 32769, 10, None, "S_BSKULL"),  # S_BSKULL2
    ("RSKU", 0, 10, None, "S_RSKULL2"),  # S_RSKULL
    ("RSKU", 32769, 10, None, "S_RSKULL"),  # S_RSKULL2
    ("YSKU", 0, 10, None, "S_YSKULL2"),  # S_YSKULL
    ("YSKU", 32769, 10, None, "S_YSKULL"),  # S_YSKULL2
    ("STIM", 0, -1, None, "S_NULL"),  # S_STIM
    ("MEDI", 0, -1, None, "S_NULL"),  # S_MEDI
    ("SOUL", 32768, 6, None, "S_SOUL2"),  # S_SOUL
    ("SOUL", 32769, 6, None, "S_SOUL3"),  # S_SOUL2
    ("SOUL", 32770, 6, None, "S_SOUL4"),  # S_SOUL3
    ("SOUL", 32771, 6, None, "S_SOUL5"),  # S_SOUL4
    ("SOUL", 32770, 6, None, "S_SOUL6"),  # S_SOUL5
    ("SOUL", 32769, 6, None, "S_SOUL"),  # S_SOUL6
    ("PINV", 32768, 6, None, "S_PINV2"),  # S_PINV
    ("PINV", 32769, 6, None, "S_PINV3"),  # S_PINV2
    ("PINV", 32770, 6, None, "S_PINV4"),  # S_PINV3
    ("PINV", 32771, 6, None, "S_PINV"),  # S_PINV4
    ("PSTR", 32768, -1, None, "S_NULL"),  # S_PSTR
    ("PINS", 32768, 6, None, "S_PINS2"),  # S_PINS
    ("PINS", 32769, 6, None, "S_PINS3"),  # S_PINS2
    ("PINS", 32770, 6, None, "S_PINS4"),  # S_PINS3
    ("PINS", 32771, 6, None, "S_PINS"),  # S_PINS4
    ("MEGA", 32768, 6, None, "S_MEGA2"),  # S_MEGA
    ("MEGA", 32769, 6, None, "S_MEGA3"),  # S_MEGA2
    ("MEGA", 32770, 6, None, "S_MEGA4"),  # S_MEGA3
    ("MEGA", 32771, 6, None, "S_MEGA"),  # S_MEGA4
    ("SUIT", 32768, -1, None, "S_NULL"),  # S_SUIT
    ("PMAP", 32768, 6, None, "S_PMAP2"),  # S_PMAP
    ("PMAP", 32769, 6, None, "S_PMAP3"),  # S_PMAP2
    ("PMAP", 32770, 6, None, "S_PMAP4"),  # S_PMAP3
    ("PMAP", 32771, 6, None, "S_PMAP5"),  # S_PMAP4
    ("PMAP", 32770, 6, None, "S_PMAP6"),  # S_PMAP5
    ("PMAP", 32769, 6, None, "S_PMAP"),  # S_PMAP6
    ("PVIS", 32768, 6, None, "S_PVIS2"),  # S_PVIS
    ("PVIS", 1, 6, None, "S_PVIS"),  # S_PVIS2
    ("CLIP", 0, -1, None, "S_NULL"),  # S_CLIP
    ("AMMO", 0, -1, None, "S_NULL"),  # S_AMMO
    ("ROCK", 0, -1, None, "S_NULL"),  # S_ROCK
    ("BROK", 0, -1, None, "S_NULL"),  # S_BROK
    ("CELL", 0, -1, None, "S_NULL"),  # S_CELL
    ("CELP", 0, -1, None, "S_NULL"),  # S_CELP
    ("SHEL", 0, -1, None, "S_NULL"),  # S_SHEL
    ("SBOX", 0, -1, None, "S_NULL"),  # S_SBOX
    ("BPAK", 0, -1, None, "S_NULL"),  # S_BPAK
    ("BFUG", 0, -1, None, "S_NULL"),  # S_BFUG
    ("MGUN", 0, -1, None, "S_NULL"),  # S_MGUN
    ("CSAW", 0, -1, None, "S_NULL"),  # S_CSAW
    ("LAUN", 0, -1, None, "S_NULL"),  # S_LAUN
    ("PLAS", 0, -1, None, "S_NULL"),  # S_PLAS
    ("SHOT", 0, -1, None, "S_NULL"),  # S_SHOT
    ("SGN2", 0, -1, None, "S_NULL"),  # S_SHOT2
    ("COLU", 32768, -1, None, "S_NULL"),  # S_COLU
    ("SMT2", 0, -1, None, "S_NULL"),  # S_STALAG
    ("GOR1", 0, 10, None, "S_BLOODYTWITCH2"),  # S_BLOODYTWITCH
    ("GOR1", 1, 15, None, "S_BLOODYTWITCH3"),  # S_BLOODYTWITCH2
    ("GOR1", 2, 8, None, "S_BLOODYTWITCH4"),  # S_BLOODYTWITCH3
    ("GOR1", 1, 6, None, "S_BLOODYTWITCH"),  # S_BLOODYTWITCH4
    ("PLAY", 13, -1, None, "S_NULL"),  # S_DEADTORSO
    ("PLAY", 18, -1, None, "S_NULL"),  # S_DEADBOTTOM
    ("POL2", 0, -1, None, "S_NULL"),  # S_HEADSONSTICK
    ("POL5", 0, -1, None, "S_NULL"),  # S_GIBS
    ("POL4", 0, -1, None, "S_NULL"),  # S_HEADONASTICK
    ("POL3", 32768, 6, None, "S_HEADCANDLES2"),  # S_HEADCANDLES
    ("POL3", 32769, 6, None, "S_HEADCANDLES"),  # S_HEADCANDLES2
    ("POL1", 0, -1, None, "S_NULL"),  # S_DEADSTICK
    ("POL6", 0, 6, None, "S_LIVESTICK2"),  # S_LIVESTICK
    ("POL6", 1, 8, None, "S_LIVESTICK"),  # S_LIVESTICK2
    ("GOR2", 0, -1, None, "S_NULL"),  # S_MEAT2
    ("GOR3", 0, -1, None, "S_NULL"),  # S_MEAT3
    ("GOR4", 0, -1, None, "S_NULL"),  # S_MEAT4
    ("GOR5", 0, -1, None, "S_NULL"),  # S_MEAT5
    ("SMIT", 0, -1, None, "S_NULL"),  # S_STALAGTITE
    ("COL1", 0, -1, None, "S_NULL"),  # S_TALLGRNCOL
    ("COL2", 0, -1, None, "S_NULL"),  # S_SHRTGRNCOL
    ("COL3", 0, -1, None, "S_NULL"),  # S_TALLREDCOL
    ("COL4", 0, -1, None, "S_NULL"),  # S_SHRTREDCOL
    ("CAND", 32768, -1, None, "S_NULL"),  # S_CANDLESTIK
    ("CBRA", 32768, -1, None, "S_NULL"),  # S_CANDELABRA
    ("COL6", 0, -1, None, "S_NULL"),  # S_SKULLCOL
    ("TRE1", 0, -1, None, "S_NULL"),  # S_TORCHTREE
    ("TRE2", 0, -1, None, "S_NULL"),  # S_BIGTREE
    ("ELEC", 0, -1, None, "S_NULL"),  # S_TECHPILLAR
    ("CEYE", 32768, 6, None, "S_EVILEYE2"),  # S_EVILEYE
    ("CEYE", 32769, 6, None, "S_EVILEYE3"),  # S_EVILEYE2
    ("CEYE", 32770, 6, None, "S_EVILEYE4"),  # S_EVILEYE3
    ("CEYE", 32769, 6, None, "S_EVILEYE"),  # S_EVILEYE4
    ("FSKU", 32768, 6, None, "S_FLOATSKULL2"),  # S_FLOATSKULL
    ("FSKU", 32769, 6, None, "S_FLOATSKULL3"),  # S_FLOATSKULL2
    ("FSKU", 32770, 6, None, "S_FLOATSKULL"),  # S_FLOATSKULL3
    ("COL5", 0, 14, None, "S_HEARTCOL2"),  # S_HEARTCOL
    ("COL5", 1, 14, None, "S_HEARTCOL"),  # S_HEARTCOL2
    ("TBLU", 32768, 4, None, "S_BLUETORCH2"),  # S_BLUETORCH
    ("TBLU", 32769, 4, None, "S_BLUETORCH3"),  # S_BLUETORCH2
    ("TBLU", 32770, 4, None, "S_BLUETORCH4"),  # S_BLUETORCH3
    ("TBLU", 32771, 4, None, "S_BLUETORCH"),  # S_BLUETORCH4
    ("TGRN", 32768, 4, None, "S_GREENTORCH2"),  # S_GREENTORCH
    ("TGRN", 32769, 4, None, "S_GREENTORCH3"),  # S_GREENTORCH2
    ("TGRN", 32770, 4, None, "S_GREENTORCH4"),  # S_GREENTORCH3
    ("TGRN", 32771, 4, None, "S_GREENTORCH"),  # S_GREENTORCH4
    ("TRED", 32768, 4, None, "S_REDTORCH2"),  # S_REDTORCH
    ("TRED", 32769, 4, None, "S_REDTORCH3"),  # S_REDTORCH2
    ("TRED", 32770, 4, None, "S_REDTORCH4"),  # S_REDTORCH3
    ("TRED", 32771, 4, None, "S_REDTORCH"),  # S_REDTORCH4
    ("SMBT", 32768, 4, None, "S_BTORCHSHRT2"),  # S_BTORCHSHRT
    ("SMBT", 32769, 4, None, "S_BTORCHSHRT3"),  # S_BTORCHSHRT2
    ("SMBT", 32770, 4, None, "S_BTORCHSHRT4"),  # S_BTORCHSHRT3
    ("SMBT", 32771, 4, None, "S_BTORCHSHRT"),  # S_BTORCHSHRT4
    ("SMGT", 32768, 4, None, "S_GTORCHSHRT2"),  # S_GTORCHSHRT
    ("SMGT", 32769, 4, None, "S_GTORCHSHRT3"),  # S_GTORCHSHRT2
    ("SMGT", 32770, 4, None, "S_GTORCHSHRT4"),  # S_GTORCHSHRT3
    ("SMGT", 32771, 4, None, "S_GTORCHSHRT"),  # S_GTORCHSHRT4
    ("SMRT", 32768, 4, None, "S_RTORCHSHRT2"),  # S_RTORCHSHRT
    ("SMRT", 32769, 4, None, "S_RTORCHSHRT3"),  # S_RTORCHSHRT2
    ("SMRT", 32770, 4, None, "S_RTORCHSHRT4"),  # S_RTORCHSHRT3
    ("SMRT", 32771, 4, None, "S_RTORCHSHRT"),  # S_RTORCHSHRT4
    ("HDB1", 0, -1, None, "S_NULL"),  # S_HANGNOGUTS
    ("HDB2", 0, -1, None, "S_NULL"),  # S_HANGBNOBRAIN
    ("HDB3", 0, -1, None, "S_NULL"),  # S_HANGTLOOKDN
    ("HDB4", 0, -1, None, "S_NULL"),  # S_HANGTSKULL
    ("HDB5", 0, -1, None, "S_NULL"),  # S_HANGTLOOKUP
    ("HDB6", 0, -1, None, "S_NULL"),  # S_HANGTNOBRAIN
    ("POB1", 0, -1, None, "S_NULL"),  # S_COLONGIBS
    ("POB2", 0, -1, None, "S_NULL"),  # S_SMALLPOOL
    ("BRS1", 0, -1, None, "S_NULL"),  # S_BRAINSTEM
    ("TLMP", 32768, 4, None, "S_TECHLAMP2"),  # S_TECHLAMP
    ("TLMP", 32769, 4, None, "S_TECHLAMP3"),  # S_TECHLAMP2
    ("TLMP", 32770, 4, None, "S_TECHLAMP4"),  # S_TECHLAMP3
    ("TLMP", 32771, 4, None, "S_TECHLAMP"),  # S_TECHLAMP4
    ("TLP2", 32768, 4, None, "S_TECH2LAMP2"),  # S_TECH2LAMP
    ("TLP2", 32769, 4, None, "S_TECH2LAMP3"),  # S_TECH2LAMP2
    ("TLP2", 32770, 4, None, "S_TECH2LAMP4"),  # S_TECH2LAMP3
    ("TLP2", 32771, 4, None, "S_TECH2LAMP"),  # S_TECH2LAMP4
]

class State(object):
    def __init__(self, sprite, frame, tics, action=None):
        self.sprite = sprites.SPRITE_NAMES.index(sprite)
        self.frame = frame
        self.tics = tics
        self.action = action
        self.next_state = None

STATES = [State(*s[0:4]) for s in DEFAULT_STATES]

for index, (_, _, _, _, next_state_name) in enumerate(DEFAULT_STATES):
    next_state_index = STATE_NAMES.index(next_state_name)
    STATES[index].next_state = STATES[next_state_index]

