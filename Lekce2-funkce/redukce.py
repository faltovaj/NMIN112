"""
Funkce na redukci
- Napište funkci red(s,f), která dostane seznam s a funkci f(x,y) a spočítá s[0] f s[1] f s[2] f ... f s[-1]. Zápisem x f y myslíme zavolání f(x,y), celý výraz se vyhodnocuje zleva doprava.
- Zapište pomocí redukce součet prvků seznamu
- Zapište pomocí redukce nalezení maxima seznamu
- Zapište pomocí redukce nalezení prvního nenulového prvku (není-li, vraťte 0)
"""
def red(seznam, fce):
	x = seznam[0]
	for i in range(1, len(seznam)):
		x = fce(x, seznam[i])
		#print(x)
	return x

seznam = [1, 2, 3, 4, 5]
print(red(seznam, max))
print(red(seznam, lambda x, y: x + y))
