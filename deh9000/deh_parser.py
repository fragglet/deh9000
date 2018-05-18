"""Main module for parsing dehacked files.

The main function in this module is called parse_dehacked_file(). This takes
as an argument a list objects which implement the following two methods:

header_regexp() - This is a function that, when called, will return a regexp.
The parser will read the dehacked file one line at a time, and it is expected
that each line it encounters will match one of the regexps returned by these
methods. It is expected that the regexp will use named capture groups.

parse_section(stream, **params) - If a line matches the regexp returned by
header_regexp(), this function is invoked, and passed an instance of
DehackedInputStream that allows more data to be read from the file using the
methods it implements. Furthermore, any values from named capture groups
matched by the header regexp are passed to the function as named parameters.
"""

from __future__ import print_function
import re
import sys

# A dehacked file must start with one of these lines:
HEADER_LINES = [
	"Patch File for DeHackEd v3.0",
	"Patch File for DeHackEd v2.3",
]

# Lines which match this regexp are comment lines and will be stripped out of
# the input stream.
COMMENT_LINE_RE = re.compile("\s*#")

class DehackedParseException(Exception):
	pass

class DehackedInputStream(object):
	def __init__(self, stream):
		self.stream = stream
		self.lineno = 0

	def read(self, nbytes):
		"""Read the specified number of bytes from the input."""
		result = ''
		while len(result) < nbytes:
			c = self.stream.read(1)
			# Strip out \r\n - support DOS text file format.
			if c == '\r':
				continue
			if c == '\n':
				self.lineno += 1
			result += c
		return result

	def readline(self):
		"""Read a line from input stream, stripping out comments."""
		while True:
			line = self.stream.readline()
			if line == "":
				break
			self.lineno += 1
			if not COMMENT_LINE_RE.match(line):
				break
		return line

	def exception(self, message):
		raise DehackedParseException("%s:%d: %s" % (
			self.stream.name,
			self.lineno,
			message,
		))

class TopLevelProperty(object):
	"""Helper class that is used to parse top-level "fields".

	This class implements the section protocol described above, but only
	parses a single line and uses the value to set a single property of an
	object.
	"""
	def __init__(self, deh_name, obj, propname, converter=None):
		self.deh_name = deh_name
		self.obj = obj
		self.propname = propname
		self.converter = converter or (lambda x: x)

	def header_regexp(self):
		return re.compile(r"\s*%s\s*=\s*(?P<value>.*\S)\s*$" % (
			self.deh_name), re.I)

	def parse_section(self, stream, value):
		setattr(self.obj, self.propname, self.converter(value))

def _read_header(stream):
	line = stream.readline()
	if line.strip() not in HEADER_LINES:
		stream.exception("dehacked file must start with the line "
		                 "%r" % HEADER_LINES[0])

def _parse_line(sections, stream, line):
	if line.strip() == "":
		return
	for regex, obj in sections:
		m = regex.match(line)
		if m:
			params = m.groupdict()
			obj.parse_section(stream, **params)
			break
	else:
		stream.exception("syntax not recognized: %r" % line)

def _parse_stream(sections, stream, strict_mode):
	_read_header(stream)
	warnings = []
	while True:
		line = stream.readline()
		if line == "":
			break
		try:
			_parse_line(sections, stream, line)
		except DehackedParseException as e:
			if strict_mode:
				raise
			warnings.append(e.message)

	if not strict_mode and warnings:
		print("Warnings loading dehacked file:", file=sys.stderr)
		for w in warnings:
			print(w, file=sys.stderr)

def parse_dehacked_file(filename, objects, strict_mode=False):
	"""Load a dehacked file from the given filename.

	'objects' is a list of objects which are expected to conform to the
	protocol described above.
	"""
	sections = [(o.header_regexp(), o) for o in objects]
	with open(filename, "r") as f:
		stream = DehackedInputStream(f)
		_parse_stream(sections, stream, strict_mode)

