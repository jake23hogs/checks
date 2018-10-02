from check50 import *

class Sixth(Checks):

    @check()
    def exists(self):
        """Sixth exists"""
        self.require("Sixth.java")

    @check("exists")
    def compiles(self):
        """Sixth compiles""" 
        self.spawn("javac Sixth.java").exit(0)

    @check("compiles")
    def test1(self):
        """input of 011 correctly gives output of INVALID"""
        self.spawn("java Sixth").stdin("011").stdout("INVALID\n", "INVALID\n")

    @check("compiles")
    def test1(self):
        """input of 1111 correctly gives output of YES"""
        self.spawn("java Sixth").stdin("1111").stdout("YES\n", "YES\n")
        
    @check("compiles")
    def test1(self):
        """input of 1010 correctly gives output of NO"""
        self.spawn("java Sixth").stdin("1010").stdout("NO\n", "NO\n")
