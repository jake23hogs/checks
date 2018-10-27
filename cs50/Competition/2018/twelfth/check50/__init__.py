from check50 import *


class Twelfth(Checks):

    @check()
    def exists(self):
        """Twelfth.java exists."""
        self.require("Twelfth.java")

    @check("exists")
    def compiles(self):
        """Twelfth.java compiles."""
        self.spawn("javac Twelfth.java").exit(0)

    @check("compiles")
    def test1(self):
        """Input of "happpy  happy"  yields output of 3"""
        self.spawn("java Twelfth").stdin("happpy").stdin("happy").stdout("3\n", "3\n").exit(0)

    @check("compiles")
    def test2(self):
        """Input of "boldldd  bold"  yields output of 5"""
        self.spawn("java Twelfth").stdin("boldldd").stdin("bold").stdout("5\n", "5\n").exit(0)