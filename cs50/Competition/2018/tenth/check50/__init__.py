from check50 import *


class Tenth(Checks):

    @check()
    def exists(self):
        """Tenth.java exists."""
        self.require("Tenth.java")

    @check("exists")
    def compiles(self):
        """Tenth.java compiles."""
        self.spawn("javac Tenth.java").exit(0)

    @check("compiles")
    def test1(self):
        """Outputs 2707   PRIME"""
        self.spawn("java Tenth").stdin("1047 4170 2513 2424 2866 4394 2707 4947 22 5405 745 2638 8550 2910 3218 3546 2859 a").stdout("2707   PRIME\n", "2707   PRIME\n").exit(0)

    @check("compiles")
    def test2(self):
        """Outputs 8550   NOT PRIME"""
        self.spawn("java Tenth").stdin("1047 4170 2513 2424 2866 4394 270 4947 22 5405 745 2638 8550 2910 3218 5036 2859 a").stdout("8550   NOT PRIME\n", "8550   NOT PRIME\n").exit(0)
