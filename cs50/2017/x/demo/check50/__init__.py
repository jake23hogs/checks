from check50 import *

class Hello(Checks):

    @check()
    def exists(self):
        """Demo exists"""
        self.require("Hello.java")

   @check("exists")
   def compiles(self):
        """Hello compiles""" 
        self.spawn("javac Hello.java").exit(0)

    @check("compiles")
    def test(self):
        """displays Hello, World! correctly"""
        self.spawn("java Hello").stdout("Hello, World!\n", "Hello, World!\n")

    