import re

from check50 import *


class Distance(Checks):

    @check()
    def exists(self):
        """Distance exists"""
        self.require("Distance.java")

    @check("exists")
    def compiles(self):
        """distance compiles"""
        self.spawn("java Distance").exit(0)

    @check("compiles")
    def distance1(self):
        """inputs of x1 = 3, y1 = -2, x2 = -1, y2 = 5 yields Distance = 8.1"""
        self.spawn("java Distance").stdin("3").stdin("-2").stdin("-1").stdin("5").stdout("Distance = 8.1\n", "Distance = 8.1\n").exit(0)
    
    @check("compiles")
    def distance1(self):
        """inputs of x1 = 4, y1 = -1, x2 = -5, y2 = 3 yields Distance = 8.1"""
        self.spawn("java Distance").stdin("4").stdin("-1").stdin("-5").stdin("3").stdout("Distance = 8.1\n", "Distance = 8.1\n").exit(0)
        
    @check("compiles")
    def test_reject_negative(self):
        """rejects a negative input like -.1"""
        self.spawn("java Distance").stdin("-1").reject()

    @check("compiles")
    def test_reject_foo(self):
        """rejects a non-numeric input of "foo" """
        self.spawn("java Distance").stdin("foo").reject()

    @check("compiles")
    def test_reject_empty(self):
        """rejects a non-numeric input of "" """
        self.spawn("java Distance").stdin("").reject()



