from check50 import *


class Vigenere(Checks):

    @check()
    def exists(self):
        """Vigenere.java exists."""
        self.require("Vigenere.java")

    @check("exists")
    def compiles(self):
        """Vigenere.java compiles."""
        self.spawn("javac Vigenere.java").exit(0)

    @check("compiles")
    def aa(self):
        """encrypts "a" as "a" using "a" as keyword"""
        self.spawn("java Vigenere a").stdin("a").stdout("ciphertext:\s*a\n", "ciphertext: a\n").exit(0)

    @check("compiles")
    def bazbarfoo_caqgon(self):
        """encrypts "barfoo" as "caqgon" using "baz" as keyword"""
        self.spawn("java Vigenere baz").stdin("barfoo").stdout("ciphertext:\s*caqgon\n", "ciphertext: caqgon\n").exit(0)

    @check("compiles")
    def mixedBaZBARFOO(self):
        """encrypts "BaRFoo" as "CaQGon" using "BaZ" as keyword"""
        self.spawn("java Vigenere BaZ").stdin("BaRFoo").stdout("ciphertext:\s*CaQGon\n", "ciphertext: CaQGon\n").exit(0)

    @check("compiles")
    def allcapsBAZBARFOO(self):
        """encrypts "BARFOO" as "CAQGON" using "BAZ" as keyword"""
        self.spawn("java Vigenere BAZ").stdin("BARFOO").stdout("ciphertext:\s*CAQGON\n", "ciphertext: CAQGON\n").exit(0)

    @check("compiles")
    def bazworld(self):
        """encrypts "world!$?" as "xoqmd!$?" using "baz" as keyword"""
        self.spawn("java Vigenere baz").stdin("world!$?").stdout("ciphertext:\s*xoqmd!\$\?\n", "ciphertext: xoqmd!$?\n").exit(0)

    @check("compiles")
    def withspaces(self):
        """encrypts "Hello, World!" as "Iekmo, Vprke!" using "baz" as keyword"""
        self.spawn("java Vigenere baz").stdin("Hello, World!").stdout("ciphertext:\s*Iekmo, Vprke!\n", "ciphertext: Iekmo, Vprke!\n").exit(0)
    
    @check("compiles")
    def noarg(self):
        """handles lack of argv[1]"""
        self.spawn("java Vigenere").exit(1)

    @check("compiles")
    def toomanyargs(self):
        """handles argc > 2"""
        self.spawn("java Vigenere 1 2 3").exit(1)

    @check("compiles")
    def reject(self):
        """rejects "Hax0r2" as keyword"""
        self.spawn("java Vigenere Hax0r2").exit(1)
