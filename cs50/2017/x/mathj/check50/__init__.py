import re

from check50 import *


class MathQuiz(Checks):

    @check()
    def exists(self):
        """MathQuiz exists"""
        self.require("MathQuiz.java")

    @check("exists")
    def compiles(self):
        """MathQuiz compiles"""
        self.spawn("javac MathQuiz.java").exit(0)

    @check("compiles")
    def test_reject_empty(self):
        """rejects a non-numeric input of "" """
        self.spawn("java MathQuiz").stdin("").reject()
