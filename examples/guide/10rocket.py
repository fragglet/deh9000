"""Script demonstrating use of the ammodata table.

This changes the maximum number of rockets that a player can carry.
"""

import deh9000

f = deh9000.DehackedFile()

# Don't let the player carry too many rockets - it's unrealistic.
f.ammodata[deh9000.am_misl].maxammo = 10

f.save("10rocket.deh")

