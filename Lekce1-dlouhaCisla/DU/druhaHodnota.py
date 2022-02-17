#cisla = [int(i) for i in input().split()]
#cisla = cisla[:-1]
#print(sorted(set(cisla))[-2])

radek = '4 5 1 4 5 3 -1'
cisla = []
for i in radek.split():
    if int(i) != -1:
        cisla.append(int(i))
print(cisla)


