"""
Hratky s maticemi: knihovna numpy
"""
import numpy as np

r = int(input("Zadejte pocet radku matice "))
s = int(input("Zadejte pocet sloupcu matice "))
X = int(input("Zadejte cislo "))

# 1. Vyrobte matici tvaru R×S vyplněnou číslem X.
a1 = np.ones(( r, s), dtype = int) * X
print(a1)

# 2. Vyrobte matici tvaru R×S, která bude mít v i-tém řádku samá čísla i.
t = np.arange(1, r+1)
a2 = np.ones((r, s)).T
v = (a2 * t).T
print(v)

# 3. Spočítejte determinant 10 matic 10×10 vyplněných náhodnými čísly mezi -1 a 1
nmatic = 10
p = np.ones((10*nmatic, 10))*(-1)
a3 = np.random.random((10*nmatic, 10))*2 + p
#print(a3)
for i in range(nmatic):
    print(i*10, 10*(i+1)-1)
    print(f"Matice c. {i}: determinant je {np.linalg.det(a3[i*10:(i+1)*10,])}")
