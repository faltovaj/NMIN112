#!/usr/bin/python3

"""
Reseni s pouzitim jedne tridy pro vrcholy.
Vrchol muze byt cislo i operator
Mene prehledne
"""

class Vrchol:
	""" Vrchol binarniho stromu """
	def __init__(self, x, levy=None, pravy=None):
		self.x = x       # Operator nebo cislo
		self.levy = levy
		self.pravy = pravy

	def __str__(self):
		if type(self.x) is int:
			return(str(self.x))
		else:
			return f'({str(self.levy)} {self.x} {str(self.pravy)})'

	def vypis_inorder(self, patro=0):
		if self.levy != None:
			self.levy.vypis_inorder(patro+1)
		print(f'{patro}. patro {self.x}')
		if self.pravy != None:
			self.pravy.vypis_inorder(patro+1)

	def vycisli(self):
		if type(self.x) is int:
			return self.x
		else:
			l = self.levy.vycisli()
			p = self.pravy.vycisli()
			if self.x == '+':
				return l + p
			if self.x == '-':
				return l - p
			if self.x == '*':
				return l * p
			if self.x == '/':
				return l // p

x = Vrchol('+', Vrchol('*', Vrchol(3), Vrchol(4)), Vrchol('-', Vrchol(5), Vrchol(6)))
print(x)
#x.vypis_inorder()
print(x.vycisli())
