from check50 import *


class LibraryTester(Checks):

    #@check()
    #def exists(self):
    #    """LibraryTester.java, Book.java, and Patron.java exists"""
	#self.require("LibraryTester.java, Book.java, Patron.java")
	#self.require("Book.java")
	#self.require("Patron.java")
	
    @check()
    def compiles(self):
        """LibraryTester.java compiles"""
        self.spawn("javac LibraryTester.java Book.java Patron.java").exit(0)

    @check("compiles")
    def test1(self):
        """Correctly Outputs true\ntrue\ntrue\nfalse\n
	Patron's name:  Ken Lambert\nTitle:  Cider House Rules\nAuthor: John Irving\n
	Title:  The Perfect Storm\nAuthor: Sebastian Junger\nTitle:  The Illiad\nAuthor: Homer\n
	true\nfalse\ntrue\nPatron's name:  Ken Lambert\nTitle:  The Perfect Storm\n
	Author: Sebastian Junger\n\nTitle:  The Illiad\nAuthor: Homer"""
        self.spawn("java LibraryTester").stdout("true\ntrue\ntrue\nfalse\n"
	+ "Patron's name:  Ken Lambert\nTitle: Cider House Rules\nAuthor: John Irving\n\n"
	+ "Title: The Perfect Storm\nAuthor: Sebastian Junger\n\nTitle: The Illiad\nAuthor: Homer\n\n"
	+ "true\nfalse\ntrue\nPatron's name:  Ken Lambert\nTitle: The Perfect Storm\n"
	+ "Author: Sebastian Junger\n\nTitle: The Illiad\nAuthor: Homer\n", "true\ntrue\ntrue\nfalse\n"
	+ "Patron's name:  Ken Lambert\nTitle: Cider House Rules\nAuthor: John Irving\n\n"
	+ "Title: The Perfect Storm\nAuthor: Sebastian Junger\n\nTitle: The Illiad\nAuthor: Homer\n\n"
	+ "true\nfalse\ntrue\nPatron's name:  Ken Lambert\nTitle: The Perfect Storm\n"
	+ "Author: Sebastian Junger\n\nTitle: The Illiad\nAuthor: Homer\n").exit(0)

    
