"""Script demonstrating use of string replacements.

This sets a couple of text strings in the game using the symbolic
names for strings.
"""

import deh9000

f = deh9000.DehackedFile()

# Set a level name in the automap:
f.strings.HUSTR_1 = "my boring level"
# Add some story text:
f.strings.C4TEXT = "at last that's all over with!"

f.save("boring.deh")

