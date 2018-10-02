from check50 import *

class First(Checks):

    @check()
    def exists(self):
        """Fourth exists"""
        self.require("Fourth.java")

    @check("exists")
    def compiles(self):
        """Fourth compiles""" 
        self.spawn("javac Fourth.java").exit(0)

    @check("compiles")
    def test1(self):
        """input of ab+CA--d* correctly gives output of (((a+b)-(C-A))*d)\n(a+b-(C-A))*d"""
        self.spawn("java Fourth").stdin("ab+CA--d*").stdout("(((a+b)-(C-A))*d)\n(a+b-(C-A))*d\n", "(((a+b)-(C-A))*d)\n(a+b-(C-A))*d\n")
