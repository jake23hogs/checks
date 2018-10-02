from check50 import *

class First(Checks):

    @check()
    def exists(self):
        """Demo exists"""
        self.require("First.java")

    @check("exists")
    def compiles(self):
        """First compiles""" 
        self.spawn("javac First.java").exit(0)

    @check("compiles")
    def test1(self):
        """input of 1 3 correctly gives output of 0"""
        self.spawn("java First")..stdin("1 3 ").stdout("0\n", "0\n")

    @check("compiles")
    def test2(self):
        """input of 5 3 correctly gives output of 0"""
        self.spawn("java First").stdin("5 3").stdout("1\n", "1\n")
