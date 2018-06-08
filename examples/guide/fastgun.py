"""Script demonstrating use of the states table.

This changes the tics field for pistol states so that it fires
very quickly.
"""

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

