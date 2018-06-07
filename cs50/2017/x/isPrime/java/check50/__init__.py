import re

from check50 import *


class isPrime(Checks):

    @check()
    def exists(self):
        """isPrime exists"""
        self.require("isPrime.java")

   @check("exists")
   def compiles(self):
       """isPrime compiles"""
        self.spawn("javac isPrime.java").exit(0)

    @check("exists")
    def test2(self):
        """input of 2 yields output of true"""
        self.spawn("java isPrime").stdin("2").stdout("true\n", "true\n").exit(0)

    @check("exists")
    def test_reject_negative(self):
        """rejects a negative input like -1"""
        self.spawn("java isPrime").stdin("-1").reject()
