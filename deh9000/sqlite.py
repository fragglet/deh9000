"""Interface module that exposes a DehackedFile as SQLite tables.

This uses the SQLite "virtual table" functionality to make the tables
associated with a given DehackedFile object accessible via SQL. The table
contents can be queried and modified via SQL.

Based on the apsw (Another Python SQLite Wrapper) library; also included
is a subclass of the apsw.Shell class that implements DEH9000-related
subcommands to load and save Dehacked files.
"""

import apsw
import sys

from deh9000 import c

TABLES = [
	"ammodata",
	"miscdata",
	"mobjinfo",
	"states",
	# TODO "strings",
	"S_sfx",
	"weaponinfo",
]

class Cursor(object):
	"""Implements the apsw.VTCursor interface.

	This allows values to be read from out of a c.StructArray into
	SQLite.
	"""

	def __init__(self, struct_array, columns):
		self.struct_array = struct_array
		self.columns = columns
		self.position = 0

	def Close(self):
		pass

	def Column(self, number):
		if number == -1:
			return self.position
		colname = self.columns[number]
		return getattr(self.struct_array[self.position], colname)

	def Eof(self):
		return self.position >= len(self.struct_array)

	def Filter(self, indexnum, indexname, constraintargs):
		pass

	def Next(self):
		self.position += 1

	def Rowid(self):
		return self.position


class Table(object):
	"""Implementation of the apsw.VTTable interface.

	This wraps a c.StructArray object as a virtual table that can be
	queried and modified.
	"""

	def __init__(self, struct_array):
		self.struct_array = struct_array
		self.columns = type(struct_array[0]).field_names()

	def BestIndex(self, constraints, orderbys):
		pass

	def Open(self):
		return Cursor(self.struct_array, self.columns)

	def Disconnect(self):
		pass

	Destroy = Disconnect

	def UpdateChangeRow(self, rowid, newrowid, fields):
		s = self.struct_array[rowid]
		for field_id, column in enumerate(self.columns):
			value = fields[field_id]
			setattr(s, column, value)

	def UpdateDeleteRow(self, rowid):
		raise NotImplementedError()

	def UpdateInsertRow(self, rowid, fields):
		raise NotImplementedError()


class Module(object):
	"""Implementation of the apsw.VTModule interface.

	This implements the module invoked by SQLite when virtual tables are
	instantiated.
	"""

	def __init__(self, dehfile):
		self.dehfile = dehfile

	def Create(self, connection, modulename,
	           databasename, tablename, *args):
		if len(args) > 0:
			raise ValueError("no arguments permitted")
		if tablename not in TABLES:
			raise ValueError("valid tables: %s" % (
				"; ".join(TABLES)))
		array = getattr(self.dehfile, tablename)
		if isinstance(array, c.Struct):
			array = c.StructArray(type(array), [array])
		table = Table(array)
		struct_type = type(array[0])
		create_sql = "CREATE TABLE %s (%s);" % (
			tablename, ", ".join(struct_type.field_names()),
		)
		return create_sql, table

	Connect = Create


class Shell(apsw.Shell):
	"""Extension of apsw.Shell with commands to read/write .deh files."""

	def __init__(self, dehfile, *args, **kwargs):
		self.dehfile = dehfile
		super().__init__(*args, **kwargs)

	def command_dehload(self, cmd):
		"""dehload FILE: Load Dehacked patch from FILE."""
		self.dehfile.load(cmd[0])

	def command_dehsave(self, cmd):
		"""dehsave FILE: Write Dehacked patch to FILE."""
		self.dehfile.save(cmd[0])

	def command_doom(self, cmd):
		"""doom ARGS: Start an interactive session to test changes."""
		self.dehfile.interactive(cmd)


def MakeTables(dehfile, connection=None):
	"""Create Dehacked virtual tables on the given SQLite connection.

	Args:
	  dehfile: instance of deh9000.dehfile to query.
	  connection: instance of apsw.Connection; if None then an in-memory
	      connection is created.
	Returns:
	  instance of apsw.Connection on which the tables were created.
	"""
	if not connection:
		connection = apsw.Connection(":memory:")
	mod = Module(f)
	connection.createmodule("deh9000", mod)
	cursor = connection.cursor()
	for table in TABLES:
		cursor.execute("CREATE VIRTUAL TABLE %s USING deh9000()" % (
			table))
	return connection


if __name__ == "__main__":
	import file
	f = file.DehackedFile()
	for filename in sys.argv[1:]:
		f.load(filename)
	shell = Shell(f, db=MakeTables(f))
	shell.cmdloop()

