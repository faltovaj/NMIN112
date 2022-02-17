"""
Scitani dlouhych cisel
Postup: 
1/ Cisla ze vstupu (string) nacteme do 
seznamu od nejmensiho radu (pro snazsi praci)
2/ Provedeme scitani po cislicich
3/ Vysledek vypiseme (prevratime, vypiseme jako string)
"""""
def secti(a, b):
    # Funkce na scitani dvou dlouhych cisel
    # POZOR: vstup a, b jsou seznamy s cislicemi zacinajici od nejnizsiho radu!!!
    # Seznam pro zapsani vysledku (seznam od nejnizsiho radu)
    vysledek = []
    # Prenos
    prenos = 0
    # Na prvnim miste chceme delsi cislo
    if len(a) < len(b):
        a, b = b, a
    for i in range(len(a)):
        # Pokud je druhe cislo kratsi, tak budeme pricitat 0 (vetev else)
        if i < len(b):
            bb = b[i]
        else:
            bb = 0
        soucet = bb + a[i] + prenos
        vysledek.append(soucet%10)
        prenos = soucet//10    
    if prenos > 0:
        vysledek.append(prenos)
    return vysledek

def prevratCislo(cislo):
    # pomocna funkce: prevrati retezec/pole
    return [int(i) for i in reversed(cislo)]

# Nacteme si dve dlouha cisla ze vstupu
cislo1 = input("Zadej prvni cislo: ")
cislo2 = input("Zadej druhe cislo: ")

# Secteme cisla (vstup: cisla zapsana v seznamu od nejnizsiho radu)
soucetReversed = secti(prevratCislo(cislo1), prevratCislo(cislo2))
# Vypiseme cislo
[print(i, end='') for i in prevratCislo(soucetReversed)]
print()
