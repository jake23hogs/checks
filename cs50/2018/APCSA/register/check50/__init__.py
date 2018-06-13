import re

from check50 import *


class Register(Checks):

    @check()
    def exists(self):
        """register exists"""
        self.require("register.c")

    @check("exists")
    def compiles(self):
        """register compiles"""
        self.spawn("clang -std=c11 -ggdb3 -o register register.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test2495(self):
        """input of 24.95 yields outputs of 24.95, 1.80887, 26.7589"""
        self.spawn("./register").stdin("24.95").stdout(24.95, "24.95\n").stdout(1.80887, "1.80887\n").stdout(26.7589, "26.7589\n").exit(0)

   
    @check("compiles")
    def test_reject_negative(self):
        """rejects a negative input like -.1"""
        self.spawn("./register").stdin("-1").reject()

    @check("compiles")
    def test_reject_foo(self):
        """rejects a non-numeric input of "foo" """
        self.spawn("./register").stdin("foo").reject()

    @check("compiles")
    def test_reject_empty(self):
        """rejects a non-numeric input of "" """
        self.spawn("./register").stdin("").reject()



