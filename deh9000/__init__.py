from __future__ import absolute_import

from deh9000.actions import *
from deh9000.ammo import *
from deh9000.misc import *
from deh9000.mobjs import *
from deh9000.sounds import *
from deh9000.sprites import *
from deh9000.states import *
from deh9000.weapons import *

from deh9000.file import DehackedFile

# For convenience, we create one global instance of a dehacked file.
# This allows users to "from deh9000 import *" and refer to all the
# tables directly by name.
dehfile = DehackedFile()
ammodata = dehfile.ammodata
miscdata = dehfile.miscdata
mobjinfo = dehfile.mobjinfo
S_sfx = dehfile.S_sfx
states = dehfile.states
sprnames = dehfile.sprnames
strings = dehfile.strings
weaponinfo = dehfile.weaponinfo

