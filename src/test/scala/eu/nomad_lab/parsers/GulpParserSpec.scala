package eu.nomad_lab.parsers

import eu.nomad_lab.{ parsers, DefaultPythonInterpreter }
import org.scalacheck.Properties
import org.specs2.mutable.Specification
import org.{ json4s => jn }

object GulpParserSpec extends Specification {
  "GulpParserTest" >> {
    "test example1 " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example1.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example1.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example2 " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example2.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example2.got", "json") must_== ParseResult.ParseSuccess
      }
    }
  }
}
