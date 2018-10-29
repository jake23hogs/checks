from check50 import *


# Coming soon...
class Crack(Checks):

    @check()
    def exists(self):
        """Crack.java exists."""
        self.require("Tenth.java")
    
    @check("exists")
    def compiles(self):
        """Crack.java compiles."""
        self.spawn("javac Crack.java").exit(0)
    
    @check("compiles")
    def test1(self):
        """Correctly cracks malan:50CcfIk1QrPr6"""
        self.spawn("java Crack 50CcfIk1QrPr6").stdout("maybe\n", "maybe\n).exit(0)

    @check("compiles")
    def test2(self):
        """Correctly cracks brian:50mjprEcqC/ts"""
        self.spawn("java Crack 50mjprEcqC/ts").stdout("CA\n", "CA\n).exit(0)
