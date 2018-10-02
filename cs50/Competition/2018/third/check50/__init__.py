from check50 import *

class Third(Checks):

    @check()
    def exists(self):
        """Third exists"""
        self.require("Third.java")

   @check("exists")
   def compiles(self):
        """Third compiles""" 
        self.spawn("javac Third.java").exit(0)

    @check("compiles")
    def test1(self):
        """input of 10 5 + 2 3 - - 2 * correctly gives output of 32"""
        self.spawn("java Third").stdin("10 5 + 2 3 - - 2 *").stdout("32\n", "32\n")
