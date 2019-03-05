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

    
