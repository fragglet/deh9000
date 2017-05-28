from actions import *
from ammo import *
from misc import *
from mobjs import *
from sounds import *
from sprites import *
from states import *
from weapons import *

from file import DehackedFile

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

