"""Script demonstrating use of the mobjinfo table.

This is a simple example that makes the Cyberdemon easy to kill.
"""

import deh9000

f = deh9000.DehackedFile()

# Now the Cyberdemon will be a pushover.
f.mobjinfo[deh9000.MT_CYBORG].spawnhealth = 1

f.save("easycybr.deh")

