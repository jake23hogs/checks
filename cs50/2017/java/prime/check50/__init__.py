import re

from check50 import *

class prime(Checks):

    @check()
    def exists(self):
        """Prime exists"""
        self.require("Prime.java")

   @check("exists")
   def compiles(self):
       """Prime compiles""" 
       self.spawn("javac Prime.java").exit(0)

    @check("compiles")
    def test2(self):
        """input of 2 yields output of true"""
        self.spawn("java Prime").stdin("2").stdout("true\n", "true\n")

    @check("compiles")
    def test_reject_negative(self):
        """rejects a negative input like -1"""
        self.spawn("java Prime").stdin("-1").reject()