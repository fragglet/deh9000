"""Script demonstrating use of the sprnames list.

This replaces the POSS sprite with SPOS, making all zombiemen look
like sergeants.
"""

import deh9000

f = deh9000.DehackedFile()

# Let's make zombiemen look like sergeants:
f.sprnames[deh9000.SPR_POSS] = "SPOS"

f.save("sargies.deh")

