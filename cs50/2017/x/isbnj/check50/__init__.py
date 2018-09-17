from check50 import *


class Credit(Checks):
    
    @check()
    def exists(self):
        """Credit.java exists."""
        self.require("Credit.java")
    
    @check("exists")
    def compiles(self):
        """Credit.java compiles."""
        self.spawn("javac Credit.java").exit(0)
    
    @check("compiles")
    def test1(self):
        """identifies 378282246310005 as AMEX"""
        self.spawn("java Credit").stdin("378282246310005").stdout("^AMEX\n", "AMEX\n").exit(0)
    
    @check("compiles")
    def test2(self):
        """identifies 371449635398431 as AMEX"""
        self.spawn("java Credit").stdin("371449635398431").stdout("^AMEX\n", "AMEX\n").exit(0)
    
    @check("compiles")
    def test3(self):
        """identifies 5555555555554444 as MASTERCARD"""
        self.spawn("java Credit").stdin("5555555555554444").stdout("^MASTERCARD\n", "MASTERCARD\n").exit(0)
    
    @check("compiles")
    def test4(self):
        """identifies 5105105105105100 as MASTERCARD"""
        self.spawn("java Credit").stdin("5105105105105100").stdout("^MASTERCARD\n", "MASTERCARD\n").exit(0)
    
    @check("compiles")
    def test5(self):
        """identifies 4111111111111111 as VISA"""
        self.spawn("java Credit").stdin("4111111111111111").stdout("^VISA\n", "VISA\n").exit(0)
    
    @check("compiles")
    def test6(self):
        """identifies 4012888888881881 as VISA"""
        self.spawn("java Credit").stdin("4012888888881881").stdout("^VISA\n", "VISA\n").exit(0)
    
    @check("compiles")
    def test7(self):
        """identifies 1234567890 as INVALID"""
        self.spawn("java Credit").stdin("1234567890").stdout("^INVALID\n", "INVALID\n").exit(0)
    
    @check("compiles")
    def test8(self):
        """identifies 5105105105135100 as INVALID"""
        self.spawn("java Credit").stdin("5105105105135100").stdout("^INVALID\n", "INVALID\n").exit(0)
    
    @check("compiles")
    def test9(self):
        """identifies 4111111111111114 as INVALID"""
        self.spawn("java Credit").stdin("4111111111111114").stdout("^INVALID\n", "INVALID\n").exit(0)
    
    @check("compiles")
    def test10(self):
        """identifies 378282246310006 as INVALID"""
        self.spawn("java Credit").stdin("378282246310006").stdout("^INVALID\n", "INVALID\n").exit(0)
    
    
    @check("compiles")
    def test_reject_empty(self):
        """rejects a non-numeric input of "" """
        self.spawn("java Credit").stdin("").reject()
