#!/usr/bin/python3

"""
Oddeleni cisel a operatoru
- Prehlednejsi, lepe se vklada novy operator
"""

class Cislo:
	""" Reprezentace cisel """
	def __init__(self, x):
		self.x = x     

	def __str__(self):
		return f'{self.x}'

	def vycisli(self):
		return self.x

class Operace:
	""" Reprezentace operatoru: Ma vzdy 2 ukazatele """
	def __init__(self, levy, pravy):
		self.levy = levy
		self.pravy = pravy

	def __str__(self):
		return f'({str(self.levy)} {self.operand} {str(self.pravy)})'

	def vycisli(self):
		return self.vycisli_operator(self.levy.vycisli(), self.pravy.vycisli())	

class Soucet(Operace):
	operand = '+'
	def vycisli_operator(self, a, b):
		return a + b

class Rozdil(Operace):
	operand = '-'
	def vycisli_operator(self, a, b):
		return a - b

class Nasobek(Operace):
	operand = '*'
	def vycisli_operator(self, a, b):
		return a * b

class Podil(Operace):
	operand = '//'
	def vycisli_operator(self, a, b):
		return a // b

x = Soucet( Nasobek(Cislo(3), Cislo(4)), Rozdil(Cislo(5), Cislo(6)) )
print(x)
print(x.vycisli())
