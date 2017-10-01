import unittest

import madlib


class MadlibTests(unittest.TestCase):

    def testEmptyString(self):
        seq = madlib.parse("")
        self.assertEquals(madlib.expand(seq), "")

    def testSimpleString(self):
        seq = madlib.parse("hello")
        self.assertEquals(madlib.expand(seq), "hello")

    def testEmptyAlternative(self):
        seq = madlib.parse("{}")
        self.assertEquals(madlib.expand(seq), "")

    def testSimpleAlternate(self):
        seq = madlib.parse("{x}")
        self.assertEquals(madlib.expand(seq), "x")

    def testSimpleStringWithEmptyAlternate(self):
        seq = madlib.parse("ab{}cd")
        self.assertEquals(madlib.expand(seq), "abcd")

    def testTrivialAlternate(self):
        seq = madlib.parse("a{x}b")
        self.assertEquals(madlib.expand(seq), "axb")

    def testAlternateOfEmpty(self):
        seq = madlib.parse("foo{|}bar")
        self.assertEquals(madlib.expand(seq), "foobar")

    def testAlternateMarkerOutsideOfAlternate(self):
        seq = madlib.parse("foo|bar")
        self.assertEquals(madlib.expand(seq), "foo|bar")

    def testAlternate(self):
        seq = madlib.parse("a{x|x}b")
        self.assertEquals(madlib.expand(seq), "axb")

    def testNestedSimpleAlternate(self):
        seq = madlib.parse("a{x{y}z}b")
        self.assertEquals(madlib.expand(seq), "axyzb")

    def testNestedAlternates(self):
        seq = madlib.parse("a{x{y|y}z{q}")
        self.assertEquals(madlib.expand(seq), "axyzq")

    def testCrazyScenario1(self):
        seq = madlib.parse("{{a|b}|{|grot}}foo")
        chooser = lambda p: p[0]
        self.assertEquals(madlib.expand(seq, chooser=chooser), "afoo")

    def testCrazyScenario2(self):
        seq = madlib.parse("{{a|{|{x|}b}}foo")
        chooser = lambda p: p[-1]
        self.assertEquals(madlib.expand(seq, chooser=chooser), "bfoo")

    def testAlternateLeftOpen(self):
        """TODO: this should fail to parse"""
        seq = madlib.parse("x{y|")
        chooser = lambda p: p[-1]
        self.assertEquals(madlib.expand(seq, chooser=chooser), "xy")

if __name__ == '__main__':
    unittest.main()

