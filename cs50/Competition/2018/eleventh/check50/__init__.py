from check50 import *


class Eleventh(Checks):

    @check()
    def exists(self):
        """Eleventh.java exists."""
        self.require("Eleventh.java")

    @check("exists")
    def compiles(self):
        """Eleventh.java compiles."""
        self.spawn("javac Eleventh.java").exit(0)

    @check("compiles")
    def test1(self):
        """Input of "pay up pal! apples are pretty lucky."  yields output of True"""
        self.spawn("java Eleventh").stdin("pay up pal!").stdin("apples are pretty lucky.").stdout("True\n", "True\n").exit(0)

    @check("compiles")
    def test2(self):
        """Input of "if you call the cops... a song of ice and fire: a novel" yields output of True"""
        self.spawn("java Eleventh").stdin("if you call the cops...").stdin("a song of ice and fire: a novel").stdout("False\n", "False\n").exit(0)