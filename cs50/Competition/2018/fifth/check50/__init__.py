from check50 import *

class Fifth(Checks):

    @check()
    def exists(self):
        """Fifth exists"""
        self.require("Fifth.java")

    @check("exists")
    def compiles(self):
        """Fifth compiles""" 
        self.spawn("javac Fifth.java").exit(0)

    @check("compiles")
    def test1(self):
        """input of 2\n3 correctly gives output of 00\n01\n10\n11\n000\n001\n010\n011\n100\n101\n110\n111\n"""
        self.spawn("java Fifth").stdin("2 3").stdout("00\n01\n10\n11\n000\n001\n010\n011\n100\n101\n110\n111\n", "00\n01\n10\n11\n000\n001\n010\n011\n100\n101\n110\n111\n")

    @check("compiles")
    def test2(self):
        """input of 2\n2 correctly gives output of 00\n01\n10\n11\n"""
        self.spawn("java Fifth").stdin("2 2").stdout("00\n01\n10\n11\n", "00\n01\n10\n11\n")
