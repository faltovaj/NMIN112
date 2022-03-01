""" 
Je dan seznam retezcu tvaru jmeno prijmeni
- Setridte je primarne podle prijmeni, sekundarne podle jmena
- Najdete osobu s nejdelsim prijmenim
"""

jmena = ['Pavel Novotny', 'Pavel Bures', 'Kamil Bures']
print(sorted(jmena, key=lambda x: (x.split()[1], x.split()[0])))
print(max(jmena, key=lambda x: len(x.split()[1])))
