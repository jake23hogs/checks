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
        """input of 1 correctly gives output of 1"""
        self.spawn("java Recursion5").stdin("1").stdout("1\n", "1\n")
    
    @check("compiles")
    def test2(self):
        """input of 2 correctly gives output of 1/n1 1/n"""
        self.spawn("java Recursion5").stdin("2").stdout(" 1\n1 1\n", "1\n1 1\n")
        
    @check("compiles")
    def test3(self):
        """input of 3 correctly gives output of 1/n1 1/n1 2 1\n"""
        self.spawn("java Recursion5").stdin("3").stdout("  1  \n 1 1 \n1 2 1\n", "  1  \n 1 1 \n1 2 1\n")
