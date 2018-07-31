from check50 import *

class Divisible1(Checks):

    @check()
    def exists(self):
        """Demo exists"""
        self.require("Divisible1.java")

   @check("exists")
   def compiles(self):
        """Divisible1 compiles""" 
        self.spawn("javac Divisible1.java").exit(0)

    @check("compiles")
    def test1(self):
        """input of 10 5 correctly gives output of DIVISIBLE"""
        self.spawn("java Divisible1").stdin("10").stdin("5").stdout("DIVISIBLE\n", "DIVISIBLE\n")

    @check("compiles")
    def test2(self):
        """input of 10 3 correctly gives output of NOT DIVISIBLE"""
        self.spawn("java Divisible1").stdin("10").stdin("3").stdout("NOT DIVISIBLE\n", "NOT DIVISIBLE\n")
