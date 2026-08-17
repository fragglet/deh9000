"""This module has function to start an interactive session.

This is convenient for experimenting with dehacked stuff from the Python
console. Table values can be changed interactively and dehfile.interactive()
can be called to start a source port to test the changes out. Successive calls
to the method will terminate and restart the source port with new values.
"""

import atexit
import os
import shlex
import subprocess
import tempfile

# TODO: Add the ability to configure these.

# Name of a source port to invoke.
EXE = "chocolate-doom"

# "Standard" command line arguments that are always passed.
ARGS = ["-window", "-nofullscreen", "-nograbmouse"]

running_process = None
temp_filename = None
atexit_registered = False
saved_args = ()
saved_level = (1, 1)

def _stop_process():
	global running_process
	if running_process is not None:
		running_process.send_signal(1)
		running_process.wait()
		running_process = None

def _write_patch_file(dehfile):
	global temp_filename
	if temp_filename is not None:
		os.unlink(temp_filename)
		temp_filename = None
	# This isn't a secure use of temp files, but oh well.
	temp_filename = tempfile.mktemp(suffix=".deh")
	dehfile.save(temp_filename)
	return temp_filename

def start_interactive(dehfile, args=None, level=None):
	global running_process, atexit_registered, saved_args, saved_level

	# Arguments can be provided as a list or just as a string. If a string
	# then use shlex to parse into a list.
	if isinstance(args, str):
		args = shlex.split(args)

	# Remember arguments so that if we are invoked again we restart with
	# the same arguments.
	if level is not None:
		saved_level = level
	if args is not None:
		saved_args = args

	# Terminate process with SIGHUP if it is already running:
	_stop_process()

	# Register a callback so we remember to shut down the process.
	# But we only do this once.
	if not atexit_registered:
		atexit.register(_stop_process)
		atexit_registered = True

	full_args = [EXE, "-deh", _write_patch_file(dehfile)]
	full_args.extend(saved_args)
	full_args.extend(ARGS)
	full_args.append("-warp")
	if isinstance(saved_level, tuple):
		full_args.extend([str(saved_level[0]), str(saved_level[1])])
	else:
		full_args.extend([str(saved_level)])

	running_process = subprocess.Popen(full_args, stdout=subprocess.PIPE)
	running_process.stdout.close()

