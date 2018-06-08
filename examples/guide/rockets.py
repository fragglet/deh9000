"""Script demonstrating use of the weaponinfo table.

This modifies the rocket launcher to change the ammo it uses to the
am_noammo type, so that there are no limits on the number of rockets
which can be fired.
"""

import deh9000

f = deh9000.DehackedFile()

# Infinite missiles for the rocket launcher!
f.weaponinfo[deh9000.wp_missile].ammo = deh9000.am_noammo

f.save("rockets.deh")

