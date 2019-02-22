from check50 import *

class Recursion5(Checks):

    @check()
    def exists(self):
        """Recursion5 exists"""
        self.require("Recursion5.java")

   @check("exists")
   def compiles(self):
        """Recursion5 compiles""" 
        self.spawn("javac Recursion5.java").exit(0)

    @check("compiles")
    def test1(self):
        """input of 3 correctly gives output of 0"""
        self.spawn("java Recursion5")..stdin("3").stdout("0\n", "0\n")
