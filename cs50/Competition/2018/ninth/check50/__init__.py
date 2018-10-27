from check50 import *


class Ninth(Checks):

    @check()
    def exists(self):
        """Ninth.java exists."""
        self.require("Ninth.java")

    @check("exists")
    def compiles(self):
        """Ninth.java compiles."""
        self.spawn("javac Ninth.java").exit(0)

    @check("compiles")
    def test1(self):
        """Outputs 300 for the max number"""
        self.spawn("java Ninth").stdin("56 300 89 299 254 7 85 98 71 111 221 a").stdout("300\n", "300\n").exit(0)

    @check("compiles")
    def test2(self):
        """Outputs 721 for the max number"""
        self.spawn("java Ninth").stdin("566 325 721 9 0099 654 720 685 38 71 111 221 a").stdout("721\n", "721\n").exit(0)
        
    @check("compiles")
    def test3(self):
        """Outputs 15489 for the max number"""
        self.spawn("java Ninth").stdin("15489 3255 7521 1 012199 06654 7020 685 38 71 111 221 a").stdout("15489\n", "15489\n").exit(0)
