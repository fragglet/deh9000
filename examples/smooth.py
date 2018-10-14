"""Dehacked generator for smooth weapons.

This is based on perkristian's original smooth weapons mod. Previous
implementations of this mod have targeted advanced ports like EDGE or ZDoom
which remove the limits on the number of animation frames / states. This
demonstrates how such a mod can be ported to dehacked using DEH9000.
"""
from __future__ import print_function

from deh9000 import *

# We need some additional states; acquire these now.
dehfile.reclaim_states(73)
dehfile.reclaim_sprites(8)

# Rebuild weapons from scratch.
weaponinfo[wp_fist].clear()
weaponinfo[wp_fist].ammo = am_noammo
weaponinfo[wp_fist].update(states.parse("""
        Ready:
                PUNG A 1 A_WeaponReady
                Loop
        Deselect:
                PUNG A 1 A_Lower
                Loop
        Select:
                PUNG A 1 A_Raise
                Loop
        Fire:
                PKFS LBCD 1
                PKFS E 2 A_Punch
                PKFS FGHI 2
                PKFS JKL 1
                PUNG A 5 A_ReFire
                Goto Ready
"""))

weaponinfo[wp_pistol].clear()
weaponinfo[wp_pistol].ammo = am_clip
weaponinfo[wp_pistol].update(states.parse("""
        Ready:
                PKPI A 1 A_WeaponReady
                Loop
        Deselect:
                PKPI A 1 A_Lower
                Loop
        Select:
                PKPI A 1 A_Raise
                Loop
        Fire:
                PKPI A 4
                PKPI B 2 A_FirePistol
                PKPI CEDB 2
                PKPI A 5 A_ReFire
                Goto Ready
        Flash:
                PKPF A 3 Bright A_Light1
                PKPF B 2 Bright
                Goto S_LIGHTDONE
"""))

weaponinfo[wp_shotgun].clear()
weaponinfo[wp_shotgun].ammo = am_shell
weaponinfo[wp_shotgun].update(states.parse("""
        Ready:
                SHTG A 1 A_WeaponReady
                Loop
        Deselect:
                SHTG A 1 A_Lower
                Loop
        Select:
                SHTG A 1 A_Raise
                Loop
        Fire:
                PKSG A 3
                PKSG A 5 A_FireShotgun
                PKSG B 2
                PKSG C 1
                PKSG D 2
                PKSG E 3
                PKSG F 4
                PKSG G 1
                PKSG H 3
                PKSG GFEDCB 2
                PKSG A 1
                PKSG A 7 A_ReFire
                Goto Ready
        Flash:
                SHTF B 3 Bright A_Light2
                SHTF A 2 Bright A_Light1
                Goto S_LIGHTDONE
"""))

weaponinfo[wp_supershotgun].clear()
weaponinfo[wp_supershotgun].ammo = am_shell
weaponinfo[wp_supershotgun].update(states.parse("""
        Ready:
                PKS2 A 1 A_WeaponReady
                Loop
        Deselect:
                PKS2 A 1 A_Lower
                Loop
        Select:
                PKS2 A 1 A_Raise
                Loop
        Fire:
                PKS2 A 3
                PKS2 A 6 A_FireShotgun2
                PKS2 A 3
                PKS2 B 2
                PKS2 C 3
                PKS2 D 4 A_CheckReload
                PKS2 E 4
                PKS2 F 2 A_OpenShotgun2
                PKS2 GHIJ 2
                PKS2 K 3
                PKS2 L 2 A_LoadShotgun2
                PKS2 M 3
                PKS2 NOPQ 2
                PKS2 R 3 A_CloseShotgun2
                PKS2 S 3
                PKS2 T 5 A_ReFire
                Goto Ready
        Flash:
                PKS2 V 3 Bright A_Light2
                PKS2 U 2 Bright A_Light1
                Goto S_LIGHTDONE
"""))

weaponinfo[wp_chaingun].clear()
weaponinfo[wp_chaingun].ammo = am_clip
weaponinfo[wp_chaingun].update(states.parse("""
        Ready:
                CHGG A 1 A_WeaponReady
                Loop
        Deselect:
                CHGG A 1 A_Lower
                Loop
        Select:
                CHGG A 1 A_Raise
                Loop
        Fire:
	Pin(S_CHAIN1):
                PKCG A 1 A_FireCGun
                PKCG BCD 1
	Pin(S_CHAIN2):
                PKCG A 1 A_FireCGun
                PKCG BCD 1
                PKCG B 0 A_ReFire
                Goto Ready
        Flash:
	Pin(S_CHAINFLASH1):
                PKCF A 2 Bright A_Light1
                PKCF D 1 Bright
                NULL A 2
                Goto S_LIGHTDONE
	Pin(S_CHAINFLASH2):
                PKCF C 2 Bright A_Light2
                PKCF B 1 Bright
                NULL A 2
                Goto S_LIGHTDONE

"""))

weaponinfo[wp_plasma].clear()
weaponinfo[wp_plasma].ammo = am_cell
weaponinfo[wp_plasma].update(states.parse("""
        Ready:
                PLSG A 1 A_WeaponReady
                Loop
        Deselect:
                PLSG A 1 A_Lower
                Loop
        Select:
                PLSG A 1 A_Raise
                Loop
        Fire:
                PLSF C 1 Bright A_FirePlasma
                PLSF D 2 Bright
                PKPL C 1 A_ReFire
                PKPL E 1
                PLSG B 15
                PKPL DCB 1
                Goto Ready
        Flash:
	Pin(S_PLASMAFLASH1):
                NULL A 4 A_Light1
                Goto S_LIGHTDONE
	Pin(S_PLASMAFLASH2):
                NULL A 4 A_Light1
                Goto S_LIGHTDONE
"""))

weaponinfo[wp_chainsaw].clear()
weaponinfo[wp_chainsaw].ammo = am_noammo
weaponinfo[wp_chainsaw].update(states.parse("""
        Deselect:
                SAWG C 1 A_Lower
                Loop
        Select:
                SAWG C 1 A_Raise
                Loop
        Ready:
	Pin(S_SAW):
                SAWG C 1 A_WeaponReady
                SAWG CDD 1
	Pin(S_SAWB):
                SAWG E 1 A_WeaponReady
                SAWG EFF 1
                Loop
        Fire:
                SAWG A 2 A_Saw
                SAWG B 2
                SAWG A 2 A_Saw
                SAWG B 2
                SAWG B 0 A_ReFire
                Goto Ready
"""))

weaponinfo[wp_missile].clear()
weaponinfo[wp_missile].ammo = am_misl
weaponinfo[wp_missile].update(states.parse("""
        Ready:
                MISG A 1 A_WeaponReady
                Loop
        Deselect:
                MISG A 1 A_Lower
                Loop
        Select:
                MISG A 1 A_Raise
                Loop
        Fire:
                PKRL A 2
                PKRL A 4 A_GunFlash
                PKRL B 2
                PKRL D 3 A_FireMissile
                PKRL C 3
                PKRL BE 2
                PKRL FG 1
                PKRL A 0 A_ReFire
                Goto Ready
        Flash:
                PKRF A 3 Bright A_Light1
                PKRF B 2 Bright
                PKRF C 2 Bright A_Light2
                PKRF DE 3 Bright
                Goto S_LIGHTDONE
"""))

weaponinfo[wp_bfg].clear()
weaponinfo[wp_bfg].ammo = am_cell
weaponinfo[wp_bfg].update(states.parse("""
        Ready:
                BFGG A 1 A_WeaponReady
                Loop
        Deselect:
                BFGG A 1 A_Lower
                Loop
        Select:
                BFGG A 1 A_Raise
                Loop
        Fire:
                BFGG A 20 A_BFGsound
                BFGG A 10 A_GunFlash
                BFGG A 10 A_FireBFG
                BFGG A 20 A_ReFire
                goto Ready
        Flash:
                BFGW A 3 bright
                BFGX GE 2 bright A_Light1
                BFGX DCBA 1 bright A_Light2
                BFGY AB 1 bright
                BFGY C 1 bright A_Light0
                Goto S_LIGHTDONE
"""))

dehfile.save("smooth.deh")

# Any left over?
state_ids = dehfile.free_states()
if state_ids:
	print("Still have %d states remaining" % len(state_ids))

