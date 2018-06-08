"""Script demonstrating the use of string replacements.

This changes the status bar to always show the ouch face by replacing the
format strings used for the different faces to all point to it.
"""

import deh9000

f = deh9000.DehackedFile()

# Everyone loves the ouch face:
for face in ("STFST%d%d", "STFTR%d0", "STFTL%d0", "STFEVL%d", "STFKILL%d"):
	f.strings[face] = "STFOUCH%d"

f.save("ouchface.deh")

