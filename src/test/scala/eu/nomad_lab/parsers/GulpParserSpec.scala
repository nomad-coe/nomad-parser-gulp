package eu.nomad_lab.parsers

import eu.nomad_lab.{ parsers, DefaultPythonInterpreter }
import org.scalacheck.Properties
import org.specs2.mutable.Specification
import org.{ json4s => jn }

object GulpParserSpec extends Specification {
  "GulpParserTest" >> {
    "test example1.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example1.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example1.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example10.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example10.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example10.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example11.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example11.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example11.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example12.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example12.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example12.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example13.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example13.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example13.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example14.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example14.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example14.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example15.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example15.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example15.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example16.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example16.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example16.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example17.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example17.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example17.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example18.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example18.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example18.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example19.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example19.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example19.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example2.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example2.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example2.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example20.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example20.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example20.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example21.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example21.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example21.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example22.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example22.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example22.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example23.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example23.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example23.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example25.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example25.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example25.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example26.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example26.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example26.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example27.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example27.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example27.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example28.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example28.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example28.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example29.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example29.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example29.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example3.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example3.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example3.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example30.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example30.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example30.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example31.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example31.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example31.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example32.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example32.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example32.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example33.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example33.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example33.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example34.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example34.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example34.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example35.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example35.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example35.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example36.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example36.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example36.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example37.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example37.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example37.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example38.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example38.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example38.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example39.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example39.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example39.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example4.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example4.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example4.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example40.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example40.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example40.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example41.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example41.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example41.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example42.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example42.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example42.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example43.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example43.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example43.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example44.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example44.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example44.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example45.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example45.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example45.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example46.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example46.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example46.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example47.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example47.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example47.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example48.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example48.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example48.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example49.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example49.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example49.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example5.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example5.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example5.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example50.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example50.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example50.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example51.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example51.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example51.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example52.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example52.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example52.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example53.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example53.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example53.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example54.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example54.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example54.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example6.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example6.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example6.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example7a.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example7a.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example7a.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example7b.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example7b.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example7b.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example8.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example8.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example8.got", "json") must_== ParseResult.ParseSuccess
      }
    }
    "test example9.got " >> {
      "test with json-events" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example9.got", "json-events") must_== ParseResult.ParseSuccess
      }
      "test with json" >> {
        ParserRun.parse(GulpParser, "parsers/gulp/test/examples/outputs/example9.got", "json") must_== ParseResult.ParseSuccess
      }
    }
  }
}
