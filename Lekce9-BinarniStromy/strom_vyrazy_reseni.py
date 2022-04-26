#!/usr/bin/python3

"""
Ukazka reseni
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

	def vypis_postfix(self):
		print(self.x, end = ' ')

	def hloubka1(self, hl):
		"""
		Hloubku dodefinujeme i pro cisla (popis u Operaci)
		"""
		return hl

	def hloubka2(self):
		"""
		Hloubku dodefinujeme i pro cisla (popis u Operaci)
		"""
		return 0

class Operace:
	""" Reprezentace operatoru: Ma vzdy 2 ukazatele """
	def __init__(self, levy, pravy):
		self.levy = levy
		self.pravy = pravy

	def __str__(self):
		return f'({str(self.levy)} {self.operand} {str(self.pravy)})'

	def vycisli(self):
		return self.vycisli_operator(self.levy.vycisli(), self.pravy.vycisli())

	def vypis_postfix(self):
		self.levy.vypis_postfix()
		self.pravy.vypis_postfix()
		print(self.operand, end = ' ')
	
	def hloubka1(self, hl):
		"""
		Pocita hloubku stromu
		Pomocny parametr hl - pri kazdem rekurzivnim volani se zvetsi o 1
		"""
		print('hl', hl, 'levy', self.levy, 'pravy ', self.pravy)
		hl_l = self.levy.hloubka1(hl + 1)
		hl_p = self.pravy.hloubka1(hl + 1)
		print('hl', hl_l, hl_p)
		return max(hl_l, hl_p)

	def hloubka2(self):
		"""
		Pocita hloubku stromu, bez pomocneho parametru
		Vraci pocet vrstev pod aktualni vrstvou
		"""
		#print('levy', self.levy, 'pravy ', self.pravy)
		hl_l = self.levy.hloubka2() + 1
		hl_p = self.pravy.hloubka2() + 1
		#print('hl', hl_l, hl_p)
		return max(hl_l, hl_p)

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
	operand = '/'
	def vycisli_operator(self, a, b):
		return a // b

class Umocneni(Operace):
        operand = "**"
        def vycisli_operator(self, a, b):
                return a**b

#slovnik operaci
slovnik_op = {'+' : Soucet, '-' : Rozdil, '*' : Nasobek, '//' : Podil}
def strom(postfix):
	"""
	Vyhodnoceni postfixoveho vyrazu
	Parametr postfix je retezec
	Hodnoty ukladame do zasobniku, pri nacteni operatoru vezmeme dve posledni ulozene hodnoty, 
	vysledek ulozime do zasobniku
	Vyhodnoceni vyrazu vypise, vraci hloubku stromu
	"""
	hl = 0
	zasobnik = []
	vyraz_postfix = postfix.split()
	for i in vyraz_postfix:
		if i.isdigit():
			zasobnik.append(int(i))
		else:
			l = zasobnik.pop()
			p = zasobnik.pop()
			op = slovnik_op[i]
			t = op(Cislo(p), Cislo(l))
			print(t.levy, t.pravy)
			hl += 1
			zasobnik.append(t.vycisli())
	print(f'Vysledek: {t.vycisli()}')
	return hl

x = Soucet( Nasobek(Podil(Cislo(4), Cislo(2)), Cislo(4)), Rozdil(Cislo(5), Cislo(6)) )
print(f'Vyraz {x}')
print(f'Vysledek: {x.vycisli()}')
print(f'Hloubka stromu (1. moznost): {x.hloubka1(0)}')
print(f'Hloubka stromu (2. moznost): {x.hloubka2()}')

print('Vyraz prevedeny na postfix:')
x.vypis_postfix()
print()

vyraz_postfix = '3 4 * 5 6 - +'
print(f'Postfixovy vyraz: {vyraz_postfix}')
r = strom(vyraz_postfix)
