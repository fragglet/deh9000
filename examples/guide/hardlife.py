"""Script demonstrating the use of miscdata.

This changes a couple of miscdata properties so that the player starts with
very little health and ammo.
"""

import deh9000

f = deh9000.DehackedFile()

# In our WAD, we start from almost nothing:
f.miscdata.initial_health = 10
f.miscdata.initial_bullets = 3

f.save("hardlife.deh")

