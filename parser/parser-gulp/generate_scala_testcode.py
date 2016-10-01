#!/usr/bin/env python
from __future__ import print_function
import os
from glob import glob

scala_imports = """package eu.nomad_lab.parsers

import eu.nomad_lab.{ parsers, DefaultPythonInterpreter }
import org.scalacheck.Properties
import org.specs2.mutable.Specification
import org.{ json4s => jn }

"""

test_template = """\
    "test %(name)s " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/%(name)s", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/%(name)s", "json") must_== ParseResult.ParseSuccess
      }
    }"""

fd = open('out.scala', 'w')

fd.write(scala_imports)

print('object GulpParserSpec extends Specification {', file=fd)
print('  "GulpParserTest" >> {', file=fd)

fnames = glob('test/outputs/example*.got')
fnames.sort()
for fname in fnames:
    fname = os.path.basename(fname)
    print(test_template % dict(name=fname), file=fd)

print('  }', file=fd)
print('}', file=fd)
