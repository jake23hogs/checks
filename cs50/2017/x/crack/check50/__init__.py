from check50 import *


class Crack(Checks):
        
    @check()
    def compiles(self):
        """Crack.java compiles"""
        self.spawn("javac Crack.java Crypt.java B64.java CharEncoding.java Charsets.java MessageDigestAlgorithms.java Sha2Crypt.java UnixCrypt.java").exit(0)
    
    @check("compiles")
    def test1(self):
        """Correctly cracks maria:509nVI8B9VfuA"""
        self.spawn("java Crack 509nVI8B9VfuA").stdout("TF\n", "TF\n").exit(0)

    @check("compiles")
    def test2(self):
        """Correctly cracks brian:50mjprEcqC/ts"""
        self.spawn("java Crack 50mjprEcqC/ts").stdout("CA\n", "CA\n).exit(0)
