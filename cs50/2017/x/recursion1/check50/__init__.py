from check50 import *

class Recursion1(Checks):

    @check()
    def exists(self):
        """Recursion1 exists"""
        self.require("Recursion1.java")

   @check("exists")
   def compiles(self):
        """Recursion1 compiles""" 
        self.spawn("javac Recursion1.java").exit(0)

    @check("compiles")
    def test1(self):
        """input of 3 correctly gives output of 3! = 6"""
        self.spawn("java Recursion1").stdin("3").stdout("3! = 6\n", "3! = 6\n")
    
    @check("compiles")
    def test2(self):
        """input of 5 correctly gives output of 5! = 120"""
        self.spawn("java Recursion1").stdin("5").stdout("5! = 120\n", "5! = 120\n")
