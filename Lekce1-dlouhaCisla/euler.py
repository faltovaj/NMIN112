"""
Priblizny vypocet Eulerova cisla
e = SUM_{N}^{inf} 1/N!
"""
import math

# Pozadovana presnost
epsilon = 1e-20

# Inicializace: e = e0+e1
e = 2
# Hodnoty faktorialu a N pro 1
fact = 1
N = 1
while ((1/fact)>epsilon):
    N += 1
    fact *= N
    e += 1/fact

print(f"Hodnota e po {N}-krocich: {e}") 
print(f"Kontrola - e v math: {math.e}")
