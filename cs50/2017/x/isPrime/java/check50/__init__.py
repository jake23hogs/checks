import re

import os.path,subprocess
from subprocess import STDOUT,PIPE

def compile_java(java_file):
    subprocess.check_call(['javac', java_file])

def execute_java(java_file, stdin):
    java_class,ext = os.path.splitext(java_file)
    cmd = ['java', java_class]
    proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout,stderr = proc.communicate(stdin)
    #print ('This was "' + stdout + '"')




from check50 import *


class isPrime(Checks):

    @check()
    def exists(self):
        """isPrime exists"""
        self.require("isPrime.java")

   @check("exists")
   def compiles(self):
       """isPrime compiles"""
        self.spawn("compile_java('isPrime.java')").exit(0)

    @check("exists")
    def test2(self):
        """input of 2 yields output of true"""
        self.spawn("execute_java('isPrime.java', '2')").stdout("true\n", "true\n").exit(0)

    @check("exists")
    def test_reject_negative(self):
        """rejects a negative input like -1"""
        self.spawn("java isPrime").stdin("-1").reject()
