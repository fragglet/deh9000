
DEH9000 is a different approach to creating
[Dehacked](https://doomwiki.org/wiki/DeHackEd) patches that is designed to
appeal to programmers. It takes the form of a Python library that can be
imported and used to write programs which output Dehacked patches.

## How to use the library

There are two "modes" of using DEH9000, which depend on what you're doing:
"object mode" and "global mode".

### Object mode

In "object mode", DEH9000 works like a standard Python library. To generate a
Dehacked file, create an instance of `deh9000.DehackedFile`; the file object
has various properties which can be modified to generate a patch. Here's an
example:
```
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

The DEH9000 API is designed to emulate Doom's internal API - the tables, types
and field names are named the same as they are in the Doom source code.
Because of this, it can often be more convenient to use "globals mode",
especially if you're porting hacks from Doom's C source code. It's also useful
if you're writing a script to output a single Dehacked file, since it avoids
having to repeatedly write the `deh9000` import prefix.
Here's an example that is equivalent to the previous example:
```
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
### Interactive mode

## Tables

The tables contain all of the data controlling Doom's objects and how they are
animated. Because of this they are some of the most important features of
DEH9000. Each table mirrors an internal table from the Doom source code and
the same names are used as in the Doom source.

### mobjinfo

The `mobjinfo` table defines the basic properties of all of Doom's internal
objects. Each entry in `mobjinfo` is an object of type `mobjinfo_t`, and there
is a symbolic name for each entry that begins with `MT_...`. Here's an
example:

```
import deh9000

f = deh9000.DehackedFile()

# Now the Cyberdemon will be a pushover.
f.mobjinfo[deh9000.MT_CYBORG].spawnhealth = 1

f.save("easycybr.deh")
```

The following properties are available on each `mobjinfo_t`:

* `doomednum`: Number used in levels to create an object of this type.
* `spawnhealth`: Number of health points the object starts with.
* `reactiontime`: Time a monster will wait before attacking.
* `painchance`: Chance (out of 255) a monster will jump to `painstate` when
  hurt.
* `speed`: How fast the monster moves.
* `radius`: Size of the object. Bounding boxes are actually square despite the
  name.
* `height`: Height of the object.
* `mass`: Used in thrust when calculating momentum from weapon impacts.
* `damage`: Amount of damage done by missile things.
* `flags`: Control flags (these begin with `MF_...`).

The following are indexes into the `states` table:

* `spawnstate`: Initial state the object starts in.
* `seestate`: State the monster jumps to when it sees an enemy.
* `painstate`: State for monster pain animation.
* `meleestate`: State for monster melee attack.
* `missilestate`: State for monster distance attack (includes tracer attacks,
  despite the name).
* `deathstate`: State for normal monster death animation.
* `xdeathstate`: State for monster gib death animation.
* `raisestate`: State for monster resurrect animation (Archvile resurrections)

The following are indexes into the `sfxinfo` table:

* `seesound`: Sound the monster waits when waking up.
* `attacksound`: Sound used for melee attacks.
* `painsound`: Sound played by `A_Pain` action.
* `deathsound`: Sound played by `A_Scream` action.
* `activesound`: Sound randomly played while monster is active.

### states

The `states` table defines the individual frames of animation for all objects
and weapons. Each entry in `states` is an object of type `state_t`, and there
is a symbolic name for each entry that begins with `S_...`. Here's an
example:
```
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

* `sprite`: Index of entry in `sprnames[]` of the sprite to use for this state.
* `frame`: Sprite frame number to use for this frame of animation. These map
  alphabetically; `A` = `0`, `B` = `1`, etc. For example, for `TROOC` this
  would be `2`, and `sprite` would be `SPR_TROO`.
* `tics`: Number of tics to show this state before jumping to `nextstate`.
* `nextstate`: Index into `states[]` of the next state to show.
* `action`: Internal action to invoke when this state is jumped to. These
  begin with `A_...`.
* `misc1`: Extra parameter to action function.
* `misc2`: Extra parameter to action function.

### weaponinfo
### ammodata
### sprnames
### S\_sfx

## Special objects:

### strings
### miscdata

## Advanced features

### Finding free states and sprites
### Automatic reclaim
### DECORATE-style parser

