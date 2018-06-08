"""Example of how to use load() and save() to merge patches."""

import deh9000, sys

assert len(sys.argv) >= 4, (
	"Usage: merge file.deh [file.deh...] merged.deh")

f = deh9000.DehackedFile()

for filename in sys.argv[1:-1]:
        f.load(filename)

f.save(sys.argv[-1])

