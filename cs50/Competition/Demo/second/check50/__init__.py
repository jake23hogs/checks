from check50 import *


class Divisible2(Checks):

    @check()
    def exists(self):
        """Demo exists"""
        self.require("Divisible2.java")

    @check("exists")
    def compiles(self):
        """Divisible2 compiles""" 
        self.spawn("javac Divisible2.java").exit(0)

    @check("compiles")
    def test1(self):
        """input of 3 correctly gives output of PRIME"""
        self.spawn("java Divisible2").stdin("3").stdout("PRIME\n", "PRIME\n")

    @check("compiles")
    def test2(self):
        """input of 12 correctly gives output of 2^2 * 3"""
        self.spawn("java Divisible2").stdin("12").stdout("2^2 * 3\n", "2^2 * 3\n")
    
    @check("compiles")
    def test3(self):
        """input of 32 correctly gives output of 2^5"""
        self.spawn("java Divisible2").stdin("32").stdout("2^5\n", "2^5\n")

    @check("compiles")
    def test4(self):
        """input of 17 correctly gives output of PRIME"""
        self.spawn("java Divisible2").stdin("17").stdout("PRIME\n", "PRIME\n")
