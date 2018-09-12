from check50 import *

class Prime(Checks):
    
    @check()
    def exists(self):
        """Prime exists"""
        self.require("Prime.java")

    @check("exists")
    def compiles(self):
        """Prime compiles""" 
        self.spawn("javac Prime.java").exit(0)

    @check("compiles")
    def test5(self):
        """input of 5 yields output of true"""
        self.spawn("java Prime").stdin("5").stdout("true\n", "true\n")

    @check("compiles")
    def test3(self):
        """rejects an input of 3"""
        self.spawn("java Prime").stdin("3").reject()

    @check("compiles")
    def test8(self):
        """input of 8 yields output of false"""
        self.spawn("java Prime").stdin("8").stdout("false\n", "false\n")

    @check("compiles")
    def test197(self):
        """input of 197 yields output of true"""
        self.spawn("java Prime").stdin("197").stdout("true\n", "true\n")

    @check("compiles")
    def test_reject_negative(self):
        """rejects a negative input like -1"""
        self.spawn("java Prime").stdin("-1").reject()
