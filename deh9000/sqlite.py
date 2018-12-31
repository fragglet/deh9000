"""Interface module that exposes a DehackedFile as SQLite tables.

This uses the SQLite "virtual table" functionality to make the tables
associated with a given DehackedFile object accessible via SQL. The table
contents can be queried and modified via SQL.

Based on the apsw (Another Python SQLite Wrapper) library; also included
is a subclass of the apsw.Shell class that implements DEH9000-related
subcommands to load and save Dehacked files.
"""

from __future__ import absolute_import
from __future__ import print_function

import apsw
import sys
import unittest

from deh9000 import actions
from deh9000 import c
from deh9000.file import DehackedFile
from deh9000.states import state_t, S_PISTOL

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
		result = getattr(self.struct_array[self.position], colname)
		# We represent action pointers by their string name:
		if isinstance(result, actions.Action):
			result = result.name
		return result

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

	def _convert_from_sql_value(self, field, value):
		if field == state_t.action:
			if value == None:
				return None
			if not hasattr(actions, value):
				raise NameError("Unknown action pointer %r" % (
					value))
			return getattr(actions, value)

		return value

	def UpdateChangeRow(self, rowid, newrowid, fields):
		s = self.struct_array[rowid]
		for field_id, column in enumerate(self.columns):
			value = fields[field_id]
			field = getattr(type(s), column)
			value = self._convert_from_sql_value(field, value)
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
	mod = Module(dehfile)
	connection.createmodule("deh9000", mod)
	cursor = connection.cursor()
	for table in TABLES:
		cursor.execute("CREATE VIRTUAL TABLE %s USING deh9000()" % (
			table))
	return connection


class TestSqlite(unittest.TestCase):

	def setUp(self):
		self.dehfile = DehackedFile()
		self.conn = MakeTables(self.dehfile)

	def expected_table_rows(self, table_name):
		if table_name == "miscdata":
			return 1
		arr = getattr(self.dehfile, table_name)
		return len(arr)

	def test_query_all_tables(self):
		for t in TABLES:
			cursor = self.conn.cursor()
			rowcount = 0
			for row in cursor.execute("SELECT * FROM %s" % t):
				rowcount += 1
			self.assertEqual(rowcount, self.expected_table_rows(t))

	def test_update_query(self):
		cursor = self.conn.cursor()
		query = "SELECT tics FROM states WHERE rowid=%d" % S_PISTOL
		self.assertEqual(self.dehfile.states[S_PISTOL].tics, 1)
		for row in cursor.execute(query):
			self.assertEqual(row[0], 1)
		cursor.execute("""
			UPDATE states SET tics=tics*2
			WHERE rowid=%d
		""" % S_PISTOL)
		self.assertEqual(self.dehfile.states[S_PISTOL].tics, 2)
		for row in cursor.execute(query):
			self.assertEqual(row[0], 2)

	def test_action_pointer_conversion(self):
		cursor = self.conn.cursor()
		query = "SELECT action FROM states WHERE rowid=%d" % S_PISTOL
		self.assertEqual(self.dehfile.states[S_PISTOL].action,
		                 actions.A_WeaponReady)
		for row in cursor.execute(query):
			self.assertEqual(row[0], "A_WeaponReady")

		cursor.execute("""
			UPDATE states SET action='A_SkelFist'
			WHERE rowid=%d
		""" % S_PISTOL)
		self.assertEqual(self.dehfile.states[S_PISTOL].action,
		                 actions.A_SkelFist)
		for row in cursor.execute(query):
			self.assertEqual(row[0], "A_SkelFist")

		cursor.execute("""
			UPDATE states SET action=NULL
			WHERE rowid=%d
		""" % S_PISTOL)
		self.assertEqual(self.dehfile.states[S_PISTOL].action, None)
		for row in cursor.execute(query):
			self.assertEqual(row[0], None)


if __name__ == "__main__":
	unittest.main()

