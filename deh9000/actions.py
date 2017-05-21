"""Doom's internal action functions.

Action functions, also known as "code pointers", are callback functions that
are associated with particular frames and invoked when a thing reaches that
particular frame.

  <https://doomwiki.org/wiki/DeHackEd#Code_pointers>
"""

class Action():
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name


A_Light0 = Action("A_Light0")
A_WeaponReady = Action("A_WeaponReady")
A_Lower = Action("A_Lower")
A_Raise = Action("A_Raise")
A_Punch = Action("A_Punch")
A_ReFire = Action("A_ReFire")
A_FirePistol = Action("A_FirePistol")
A_Light1 = Action("A_Light1")
A_FireShotgun = Action("A_FireShotgun")
A_Light2 = Action("A_Light2")
A_FireShotgun2 = Action("A_FireShotgun2")
A_CheckReload = Action("A_CheckReload")
A_OpenShotgun2 = Action("A_OpenShotgun2")
A_LoadShotgun2 = Action("A_LoadShotgun2")
A_CloseShotgun2 = Action("A_CloseShotgun2")
A_FireCGun = Action("A_FireCGun")
A_GunFlash = Action("A_GunFlash")
A_FireMissile = Action("A_FireMissile")
A_Saw = Action("A_Saw")
A_FirePlasma = Action("A_FirePlasma")
A_BFGsound = Action("A_BFGsound")
A_FireBFG = Action("A_FireBFG")
A_BFGSpray = Action("A_BFGSpray")
A_Explode = Action("A_Explode")
A_Pain = Action("A_Pain")
A_PlayerScream = Action("A_PlayerScream")
A_Fall = Action("A_Fall")
A_XScream = Action("A_XScream")
A_Look = Action("A_Look")
A_Chase = Action("A_Chase")
A_FaceTarget = Action("A_FaceTarget")
A_PosAttack = Action("A_PosAttack")
A_Scream = Action("A_Scream")
A_SPosAttack = Action("A_SPosAttack")
A_VileChase = Action("A_VileChase")
A_VileStart = Action("A_VileStart")
A_VileTarget = Action("A_VileTarget")
A_VileAttack = Action("A_VileAttack")
A_StartFire = Action("A_StartFire")
A_Fire = Action("A_Fire")
A_FireCrackle = Action("A_FireCrackle")
A_Tracer = Action("A_Tracer")
A_SkelWhoosh = Action("A_SkelWhoosh")
A_SkelFist = Action("A_SkelFist")
A_SkelMissile = Action("A_SkelMissile")
A_FatRaise = Action("A_FatRaise")
A_FatAttack1 = Action("A_FatAttack1")
A_FatAttack2 = Action("A_FatAttack2")
A_FatAttack3 = Action("A_FatAttack3")
A_BossDeath = Action("A_BossDeath")
A_CPosAttack = Action("A_CPosAttack")
A_CPosRefire = Action("A_CPosRefire")
A_TroopAttack = Action("A_TroopAttack")
A_SargAttack = Action("A_SargAttack")
A_HeadAttack = Action("A_HeadAttack")
A_BruisAttack = Action("A_BruisAttack")
A_SkullAttack = Action("A_SkullAttack")
A_Metal = Action("A_Metal")
A_SpidRefire = Action("A_SpidRefire")
A_BabyMetal = Action("A_BabyMetal")
A_BspiAttack = Action("A_BspiAttack")
A_Hoof = Action("A_Hoof")
A_CyberAttack = Action("A_CyberAttack")
A_PainAttack = Action("A_PainAttack")
A_PainDie = Action("A_PainDie")
A_KeenDie = Action("A_KeenDie")
A_BrainPain = Action("A_BrainPain")
A_BrainScream = Action("A_BrainScream")
A_BrainDie = Action("A_BrainDie")
A_BrainAwake = Action("A_BrainAwake")
A_BrainSpit = Action("A_BrainSpit")
A_SpawnSound = Action("A_SpawnSound")
A_SpawnFly = Action("A_SpawnFly")
A_BrainExplode = Action("A_BrainExplode")

