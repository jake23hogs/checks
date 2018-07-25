import re

from check50 import *


class MarioLess(Checks):

    @check()
    def exists(self):
        """MarioLess exists"""
        self.require("MarioLess.java")
        self.add("1.txt", "2.txt", "23.txt")

    @check("exists")
    def compiles(self):
        """MarioLess compiles"""
        self.spawn("javac MarioLess.java").exit(0)

    @check("compiles")
    def test041(self):
        """input of 0.41 yields output of 4"""
        self.spawn("java MarioLess").stdin("0.41").stdout(coins(4), "4\n").exit(0)

    @check("compiles")
    def test001(self):
        """input of 0.01 yields output of 1"""
        self.spawn("java MarioLess").stdin("0.01").stdout(coins(1), "1\n").exit(0)

    @check("compiles")
    def test015(self):
        """input of 0.15 yields output of 2"""
        self.spawn("java MarioLess").stdin("0.15").stdout(coins(2), "2\n").exit(0)

    @check("compiles")
    def test160(self):
        """input of 1.6 yields output of 7"""
        self.spawn("java MarioLess").stdin("1.6").stdout(coins(7), "7\n").exit(0)

    @check("compiles")
    def test230(self):
        """input of 23 yields output of 92"""
        self.spawn("java MarioLess").stdin("23").stdout(coins(92), "92\n").exit(0)

    @check("compiles")
    def test_reject_negative(self):
        """rejects a negative input like -.1"""
        self.spawn("java MarioLess").stdin("-1").reject()

    @check("compiles")
    def test_reject_empty(self):
        """rejects a non-numeric input of "" """
        self.spawn("java MarioLess").stdin("").reject()

