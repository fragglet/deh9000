"""Dehacked generator for smooth weapons.

This is based on perkristian's original smooth weapons mod. Previous
implementations of this mod have targeted advanced ports like EDGE or ZDoom
which remove the limits on the number of animation frames / states. This
demonstrates how such a mod can be ported to dehacked using DEH9000.
"""
from __future__ import print_function

from deh9000 import *

# Clear all weapons we're replacing first, so we can reclaim their states.
weaponinfo[wp_fist].clear()
weaponinfo[wp_pistol].clear()
weaponinfo[wp_shotgun].clear()
weaponinfo[wp_supershotgun].clear()
weaponinfo[wp_plasma].clear()
weaponinfo[wp_chainsaw].clear()
state_ids = dehfile.reclaim_states(110)
state_ids.remove(S_SAW)

# Acquire new sprite names we need.
new_sprites = ("PKFS", "PUNG", "PKPI", "PKPF", "PKSG", "SHTG", "SHTF",
               "SHT2", "PKS2", "PKPL", "PLSF", "TNT1", "PLSG", "SAWG")

sprite_ids = list(dehfile.reclaim_sprites(len(new_sprites)))
for i, name in enumerate(new_sprites):
	sprite_id = sprite_ids[i]
	sprnames[sprite_id] = name

# Rebuild weapons from scratch.

weaponinfo[wp_fist].update(states.parse(state_ids, """
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

weaponinfo[wp_pistol].update(states.parse(state_ids, """
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
                Goto S_LIGHTDONE
"""))

weaponinfo[wp_shotgun].update(states.parse(state_ids, """
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

weaponinfo[wp_supershotgun].update(states.parse(state_ids, """
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
                PKS2 A 3 A_CheckReload
                PKS2 B 2
                PKS2 C 3
                PKS2 D 4
                PKS2 E 4
                PKS2 F 2 A_OpenShotgun2
                PKS2 GHIJ 2
                PKS2 K 3
                PKS2 L 2 A_LoadShotgun2
                PKS2 M 3
                PKS2 NOPQ 2
                PKS2 R 3 A_CloseShotgun2
                PKS2 S 3
                PKS2 T 1 A_ReFire
                Goto Ready
        Flash:
                SHT2 J 3 Bright A_Light2
                SHT2 I 2 Bright A_Light1
                Goto S_LIGHTDONE
"""))

weaponinfo[wp_plasma].update(states.parse(state_ids, """
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
                TNT1 A 0 A_ReFire
                PLSF E 1 Bright
                PLSF F 1 Bright
                PLSF E 1 Bright
                PKPL B 1
                PKPL DEF 1
                PKPL G 6
                PKPL FEDC 2
                PKPL BA 1
                Goto Ready
      #  Hold:
      #          PLSF E 1 Bright A_FirePlasma
      #          PLSF F 1 Bright
      #          PLSF E 1 Bright
      #          PLSF C 1 Bright A_FirePlasma
      #          PLSF D 2 Bright
      #          PLSF D 0 Bright A_ReFire
      #          Goto Fire+3
        Flash:
                TNT1 A 1 A_Light1
                Goto S_LIGHTDONE
"""))

state_ids.add(S_SAW)

weaponinfo[wp_chainsaw].update(states.parse(state_ids, """
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

dehfile.save("smooth.deh")

if state_ids:
	print("Still have %d states remaining" % len(state_ids))

