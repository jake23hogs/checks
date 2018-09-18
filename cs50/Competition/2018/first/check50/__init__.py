from check50 import *


class First(Checks):

    @check()
    def exists(self):
        """First.java exists"""
        self.require("First.java")

    @check("exists")
    def compiles(self):
        """First compiles""" 
        self.spawn("javac First.java").exit(0)

    @check("compiles")
    def test1(self):
        """input of AABB correctly gives output of ACCEPTED!"""
        self.spawn("java First").stdin("AABB").stdout("ACCEPTED!\n", "ACCEPTED!\n")

    @check("compiles")
    def test2(self):
        """input of BA correctly gives output of REJECTED!"""
        self.spawn("java First").stdin("BA").stdout("REJECTED!\n", "REJECTED!\n")
