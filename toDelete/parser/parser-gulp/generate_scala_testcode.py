#!/usr/bin/env python
# Copyright 2016-2018 Ask Hjorth Larsen, Fawzi Mohamed
# 
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

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
