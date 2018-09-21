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
