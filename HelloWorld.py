#!/usr/bin/python

class Hello:
	
	def __init__(self, fname, lname):
		self.first = fname
		self.last = lname

	def __str__(self):
		return(self.first + " " + self.last)

hello = Hello("Hello", "World")
print(hello)
