import re

from check50 import *


class isPrime(Checks):

    @check()
    def exists(self):
        """isPrime exists"""
        self.require("isPrime.c")

    @check("exists")
    def compiles(self):
        """isPrime compiles"""
        self.spawn("clang -std=c11 -ggdb3 -o isPrime isPrime.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test2(self):
        """input of 2 yields output of true"""
        self.spawn("./isPrime").stdin("2").stdout("true\n", "true\n").exit(0)

    @check("compiles")
    def test_reject_negative(self):
        """rejects a negative input like -.1"""
        self.spawn("./isPrime").stdin("-1").reject()

