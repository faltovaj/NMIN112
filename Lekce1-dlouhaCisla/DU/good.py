def good(cisl):
    N = cisl
    while N > 0:
        cifra = N%10
        if cifra == 0:
            return False
        if cisl%cifra != 0:
            return False
        N //= 10
    return True

cislo = int(input())

pocet = 0
for i in range(1,cislo+1):
    if good(i):
        pocet += 1
print(pocet)
