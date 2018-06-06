
DEH 9000 is a different approach to creating
[Dehacked](https://doomwiki.org/wiki/DeHackEd) patches that is designed to
appeal to programmers. It takes the form of a Python library that can be
imported and used to write programs which output Dehacked patches.

## How to use the library

There are two "modes" of using DEH 9000, which depend on what you're doing:
"object mode" and "global mode".

### Object mode

In "object mode", DEH 9000 works like a standard Python library. To generate a
Dehacked file, create an instance of `deh9000.DehackedFile`; the file object
has various properties which can be modified to generate a patch. Here's an
example:
```python
import deh9000

f = deh9000.DehackedFile()

# Give all weapons infinite ammo.
for weapon in f.weaponinfo:
	weapon.ammo = deh9000.am_noammo

f.save("infinite.deh")
```
Object mode can be preferable if writing a program to generate many different
Dehacked files. Each instance of a `deh9000.DehackedFile` gets its own copy of
Doom's tables which can be independently modified without affecting other
instances.

### Globals mode

The DEH 9000 API is designed to emulate Doom's internal API - the tables, types
and field names are named the same as they are in the Doom source code.
Because of this, it can often be more convenient to use "globals mode",
especially if you're porting hacks from Doom's C source code. It's also useful
if you're writing a script to output a single Dehacked file, since it avoids
having to repeatedly write the `deh9000` import prefix.
Here's an example that is equivalent to the previous example:
```python
from deh9000 import *

# Give all weapons infinite ammo.
for weapon in weaponinfo:
	weapon.ammo = am_noammo

dehfile.save("infinite.deh")
```
Globals mode has the advantage of bringing all constants into the global
namespace. There is a single global copy of the tables that can be modified;
these belong to a singleton object that is named `dehfile`.

### Loading and saving Dehacked files

DEH 9000 supports both loading and saving Dehacked files. This allows Dehacked
files to be loaded into memory, modified and then saved again. For example to
modify an existing mod to make all the enemies tougher:
```python
import deh9000

f = deh9000.DehackedFile()
f.load("easy.deh")

# Make all the enemies tougher:
for mobj in f.mobjinfo:
	if mobj.flags & deh9000.MF_COUNTKILL:
		mobj.spawnhealth = int(mobj.spawnhealth * 1.3)

f.save("tougher.deh")
```
It's also possible to use this to merge multiple patches into one. Here's a
simple example of a program to merge many Dehacked patches into one:
```python
import deh9000, sys

f = deh9000.DehackedFile()

for filename in sys.argv[1:-1]:
        f.load(filename)

f.save(sys.argv[-1])
```

### Interactive mode

One of the nice things about Python is the dynamic nature of the language
means that it's easy to open up a Python interactive console at any time and
get some immediate results. To support this, DEH 9000 has "interactive mode"
which will quickly start up Chocolate Doom to test out changes typed on the
command line. It's recommended to use this in combination with "globals mode"
(described above).

For example, suppose you wanted to experiment with the mobj `mass` parameter
and see the effect of changing it:
```python
$ python
Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from deh9000 import *
>>> mobjinfo[MT_POSSESSED].mass = 10
>>> dehfile.interactive()
>>> mobjinfo[MT_POSSESSED].mass = 1
>>> dehfile.interactive()
```
Every time the `interactive()` method is called the game is killed and
restarted.

## Tables

The tables contain all of the data controlling Doom's objects and how they are
animated. Because of this they are some of the most important features of
DEH 9000. Each table mirrors an internal table from the Doom source code and
the same names are used as in the Doom source.

### mobjinfo

The `mobjinfo` table defines the basic properties of all of Doom's internal
objects. Each entry in `mobjinfo` is an object of type `mobjinfo_t`, and there
is a symbolic name for each entry that begins with `MT_...`. Here's an
example:

```python
import deh9000

f = deh9000.DehackedFile()

# Now the Cyberdemon will be a pushover.
f.mobjinfo[deh9000.MT_CYBORG].spawnhealth = 1

f.save("easycybr.deh")
```

The following properties are available on each `mobjinfo_t`:

| Field name | Dehacked name | Description | Index into |
| ---------- | ------------- | ----------- | ---------- |
| `doomednum` | `ID #` | Number used in levels to create an object of this type. | |
| `spawnstate` | `Initial frame` | Initial state the object starts in. | `states` |
| `spawnhealth` | `Hit points` | Number of health points the object starts with. | |
| `seestate` | `First moving frame` | State the monster jumps to when it sees an enemy. | `states` |
| `seesound` | `Alert sound` | Sound the monster waits when waking up. | `S_sfx` |
| `reactiontime` | `Reaction time` | Time a monster will wait before attacking. | |
| `attacksound` | `Attack sound` | Sound used for melee attacks. | `S_sfx` |
| `painstate` | `Injury frame` | State for monster pain animation. | `states` |
| `painchance` | `Pain chance` | Chance (out of 255) a monster will jump to `painstate` when hurt. | |
| `painsound` | `Pain sound` | Sound played by `A_Pain` action. | `S_sfx` |
| `meleestate` | `Close attack frame` | State for monster melee attack. | `states` |
| `missilestate` | `Far attack frame` | State for monster distance attack (includes hitscan attacks, despite the name). | `states` |
| `deathstate` | `Death frame` | State for normal monster death animation. | `states` |
| `xdeathstate` | `Exploding frame` | State for monster gib death animation. | `states` |
| `deathsound` | `Death sound` | Sound played by `A_Scream` action. | `S_sfx` |
| `speed` | `Speed` | How fast the monster moves. | |
| `radius` | `Width` | Size of the object. Bounding boxes are actually square despite the name. | |
| `height` | `Height` | Height of the object. | |
| `mass` | `Mass` | Used in thrust when calculating momentum from weapon impacts. | |
| `damage` | `Missile damage` | Amount of damage done by missile things. | |
| `activesound` | `Action sound` | Sound randomly played while monster is active. | `S_sfx` |
| `flags` | `Bits` | Control flags (these begin with `MF_...`). | |
| `raisestate` | `Respawn frame` | State for monster resurrect animation (Archvile resurrections) | `states` |

### states

The `states` table defines the individual frames of animation for all objects
and weapons. Each entry in `states` is an object of type `state_t`, and there
is a symbolic name for each entry that begins with `S_...`. Here's an
example:
```python
import deh9000

pistol_states = (
	deh9000.S_PISTOL1, deh9000.S_PISTOL2, deh9000.S_PISTOL3,
	deh9000.S_PISTOL4, deh9000.S_PISTOLFLASH,
)

f = deh9000.DehackedFile()

# Make the pistol fire really quickly.
for state_id in pistol_states:
	f.states[state_id].tics = 1

f.save("fastgun.deh")
```

The following properties are available on each `state_t`:

| Field name | Dehacked name | Description | Index into |
| ---------- | ------------- | ----------- | ---------- |
| `sprite` | `Sprite number` | Sprite to use for this state. | `sprnames` |
| `frame` | `Sprite subnumber` | Sprite frame number to use for this frame of animation. These map alphabetically; `A` = `0`, `B` = `1`, etc. For example, for `TROOC` this would be `2`, and `sprite` would be `SPR_TROO`. | |
| `tics` | `Duration` | Number of tics to show this state before jumping to `nextstate`. | |
| `nextstate` | `Next frame` | Next state to show. | `states` |
| `action` | | Internal action to invoke when this state is jumped to. These begin with `A_...`. | |
| `misc1` | `Unknown 1` | Extra parameter to action function. | |
| `misc2` | `Unknown 2` | Extra parameter to action function. | |

### weaponinfo

The `weaponinfo` table controls the properties of the player's weapons. Each
entry in `weaponinfo` is an object of type `weaponinfo_t`, and there
is a symbolic name for each entry that begins with `wp_...`. Here's an
example:
```python
import deh9000

f = deh9000.DehackedFile()

# Infinite missiles for the rocket launcher!
f.weaponinfo[deh9000.wp_missile].ammo = deh9000.am_noammo

f.save("rockets.deh")
```

The following properties are available on each `weaponinfo_t`:

| Field name | Dehacked name | Description | Index into |
| ---------- | ------------- | ----------- | ---------- |
| `ammo` | `Ammo type` | Ammo this weapon consumes (or `am_noammo` if it consumes no ammo, like the fist). | `ammodata` |
| `upstate` | `Deselect frame` | Animation frame to show when switching to this weapon. | `states` |
| `downstate` | `Select frame` | Animation frame to show when switching to this weapon. | `states` |
| `readystate` | `Bobbing frame` | Animation frame to show while holding the weapon. | `states` |
| `atkstate` | `Shooting frame` | Animation frame to show when the weapon fires. | `states` |
| `flashstate` | `Firing frame` | Extra animation sequence to overlay when weapon fires, for gun flash. | `states` |

### ammodata

The `ammodata` table controls parameters for each ammo type in the game. Each
entry in `ammodata` is an object of type `ammodata_t` and there is a symbolic
name for each entry that begins with `am_...`. Here's an example:
```python
import deh9000

f = deh9000.DehackedFile()

# Don't let the player carry too many rockets - it's unrealistic.
f.weaponinfo[deh9000.am_misl].maxammo = 10

f.save("10rocket.deh")
```

The `ammodata` table does not exist as such inside the Doom source code, but
exists in DEH 9000 as an abstraction for Dehacked's `Ammo` block type.

The following properties are available on each `ammodata_t`:

| Field name | Dehacked name | Description |
| ---------- | ------------- | ----------- |
| `clipammo` | `Per ammo` | Amount of ammo the player receives when picking up a "clip" of this ammo type. Each ammo type has two types of power-up that give some of that ammo: a "clip" type and a "box" type. The box gives 5x the clip type.  Ammo dropped by a monster (either in clip or weapon form) usually gives half a clip. |
| `maxammo` | `Max ammo` | Maximum amount of this ammo type that a player can hold. The backpack item doubles this. |

### sprnames

The `sprnames` table is a list of strings used for sprite names; there is a
limited number of sprite names which can be used in the game. Each entry in
`sprnames` has a symbolic name that begins `SPR_...`. Here's an example:
```python
import deh9000

f = deh9000.DehackedFile()

# Let's make zombiemen look like sergeants:
f.sprnames[deh9000.SPR_POSS] = "SPOS"

f.save("sargies.deh")
```

### S\_sfx

The `S_sfx` table is a table of the game's sound effects; each entry in
`S_sfx` is an object of type `sfxinfo_t`. It's not a very interesting table.

## Special objects

### strings

Other than tables, one very useful feature in Dehacked patches is the ability
to perform string replacements. Almost any text appearing in the game can be
replaced. A convenient way to do this is using the symbolic names for strings
which can be found by checking `strings.py` in the source code, or
`d_englsh.h` in the Doom source code. Here's an example:
```python
import deh9000

f = deh9000.DehackedFile()

# Set a level name in the automap:
f.strings.HUSTR_1 = "my boring level"
# Add some story text:
f.strings.C4TEXT = "at last that's all over with!"

f.save("boring.deh")
```
That said, Doom includes a lot of strings which do not have symbolic names.
Sometimes you may want to do arbitrary string replacements in order to do
fancy tricks. Here's an example:
```python
import deh9000

f = deh9000.DehackedFile()

# Everyone loves the ouch face:
for face in ("STFST%d%d", "STFTR%d0", "STFTL%d0", "STFEVL%d", "STFKILL%d"):
	f.strings[face] = "STFOUCH%d"

f.save("ouchface.deh")
```
In general you can use `strings` like a normal Python dictionary to set and
look up string replacements in the specified Dehacked file.

### miscdata

Dehacked supports a rather random selection of miscellaneous parameters which
can be tweaked in patches using the `miscdata` object. Here's an example:
```python
import deh9000

f = deh9000.DehackedFile()

# In our WAD, we start from almost nothing:
f.miscdata.initial_health = 10
f.miscdata.initial_bullets = 3

f.save("hardlife.deh")
```

`miscdata` has the following properties:

| Field name | Dehacked name | Description |
| ---------- | ------------- | ----------- |
| `initial_health` | `Initial Health` | Initial health a player has when starting anew. |
| `initial_bullets` | `Initial Bullets` | Number of bullets the player has when starting anew. |
| `max_health` | `Max Health` | Maximum health that can be reached using medikits alone. |
| `max_armor` | `Max Armor` | Maximum armor which can be reached by picking up armor helmets. |
| `green_armor_class` | `Green Armor Class` | Armor class that is given when picking up the green armor or an armor helmet. DOS dehacked only modifies the behavior of the green armor shirt, the armor class set by armor helmets is not affected. |
| `blue_armor_class` | `Blue Armor Class` | Armor class that is given when picking up the blue armor or a megasphere. DOS dehacked only modifies the MegaArmor behavior and not the MegaSphere, which always gives armor type 2. |
| `max_soulsphere` | `Max Soulsphere` | Maximum health which can be reached by picking up the soulsphere. |
| `soulsphere_health` | `Soulsphere Health` | Amount of health bonus that picking up a soulsphere gives. |
| `megasphere_health` | `Megasphere Health` | What health is set to after picking up a megasphere. |
| `god_mode_health` | `God Mode Health` | What the health value is set to when cheating using the IDDQD god mode cheat. |
| `idfa_armor` | `IDFA Armor` | What the armor is set to when using the IDFA cheat. |
| `idfa_armor_class` | `IDFA Armor Class` | What the armor class is set to when using the IDFA cheat. |
| `idkfa_armor` | `IDKFA Armor` | What the armor is set to when using the IDKFA cheat. |
| `idkfa_armor_class` | `IDKFA Armor Class` | What the armor class is set to when using IDKFA. |
| `bfg_cells_per_shot` | `BFG Cells/Shot` | The number of CELLs firing the BFG uses up. |
| `species_infighting` | `Species Infighting` | Controls whether monsters can harm other monsters of the same species. For example, whether an imp fireball will damage other imps. The value of this is weird - '202' means off, while '221' means on. |

## Advanced features

### Finding free states

One of the big limitations of vanilla Dehacked is the limited number of states
available to work with in the `states` table. This restricts the ability to
add new monsters and animations, since any new states must come at the expense
of sacrificing something else.

DEH 9000 includes a helpful API that can help to identify which states are not
referenced from anywhere and are therefore free to use. It starts from the
`mobjinfo` and `weaponinfo` tables and walks all referenced states to find out
which are used and which are not used: if you're familiar with how a
mark-and-sweep garbage collector operates, it works in a similar way.

To use it, call `DehackedFile.free_states()`. Here's a short demo of an
interactive session:
```python
Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from deh9000 import *
>>> dehfile.free_states()
{S_DEADBOTTOM, S_STALAG, S_DEADTORSO, S_DSNR1, S_DSNR2}
>>>
```
Vanilla Doom has these five free states available before anything else is
done: they're left over from the development process and were never included
in the game. Suppose now you decide that in order to get more states, you'll
sacrifice the Wolfenstein SS guard from Doom II's secret levels. To do this,
call `clear()` on the object corresponding to the guard:
```python
>>> mobjinfo[MT_WOLFSS].clear()
>>> dehfile.free_states()
{S_STALAG, S_DSNR1, S_DSNR2, S_SSWV_STND, S_SSWV_STND2, S_SSWV_RUN1,
S_SSWV_RUN2, S_SSWV_RUN3, S_SSWV_RUN4, S_SSWV_RUN5, S_SSWV_RUN6, S_SSWV_RUN7,
S_SSWV_RUN8, S_SSWV_ATK1, S_SSWV_ATK2, S_SSWV_ATK3, S_SSWV_ATK4, S_SSWV_ATK5,
S_SSWV_ATK6, S_SSWV_PAIN, S_SSWV_PAIN2, S_SSWV_DIE1, S_SSWV_DIE2, S_SSWV_DIE3,
S_SSWV_DIE4, S_SSWV_DIE5, S_SSWV_XDIE1, S_SSWV_XDIE2, S_SSWV_XDIE3,
S_SSWV_XDIE4, S_SSWV_XDIE5, S_SSWV_XDIE6, S_SSWV_XDIE7, S_SSWV_XDIE8,
S_SSWV_XDIE9, S_SSWV_RAISE1, S_SSWV_RAISE2, S_SSWV_RAISE3, S_SSWV_RAISE4,
S_SSWV_RAISE5, S_DEADTORSO, S_DEADBOTTOM}
```
All of the guard's animation states are now free to reuse for other purposes,
along with the original five states previously mentioned. This gives a lot of
flexibility since it's now possible to programmatically reassign them, and
experiment with sacrificing different pieces of the game to get the right
balance.

### Finding free sprites

As with `free_states()` a similar API exists for reclaiming sprites. These are
another thing that is often in short supply.
```python
>>> from deh9000 import *
>>> dehfile.free_sprites()
{SPR_SMT2}
```
Unlike with `free_states()`, Doom only has a single unreferenced sprite in its
tables. Suppose we try the same trick of clearing the Wolfenstein SS guard:
```python
>>> mobjinfo[MT_WOLFSS].clear()
>>> dehfile.free_sprites()
{SPR_SMT2}
```
Surprisingly, this doesn't work. That's because the Boss Brain's "eye" thing
from MAP30 reuses the SS guard's sprite name. Changing its three states to use
a different sprite fixes the issue, and now `SPR_SSWV` is available:
```python
>>> states[S_BRAINEYE].sprite = SPR_TROO
>>> states[S_BRAINEYESEE].sprite = SPR_TROO
>>> states[S_BRAINEYE1].sprite = SPR_TROO
>>> dehfile.free_sprites()
{SPR_SSWV, SPR_SMT2}
```

### Automatic reclaim
### DECORATE-style parser

