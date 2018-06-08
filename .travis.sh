#!/bin/bash
# Shell script to run tests.

set -eu

IGNORE_FILES="
	examples/guide/merge.py
"

success=true

for src in deh9000/*.py examples/*.py examples/guide/*.py; do
	if echo "$IGNORE_FILES" | grep -qw "$src"; then
		continue
	fi
	if ! python "$src"; then
		echo "FAILED: $src"
		success=false
	fi
done

if ! $success; then
	echo "Some files failed to execute."
	exit 1
fi

