'''
Napiste generator, ktery dostane dva seznamy 
a bude generovat jejich kartezsky soucin.
'''
def gen_kartezsky(x, y):
	for i in x:
		for j in y:
			yield(i, j)

for i in gen_kartezsky([1, 2], [11, 22]):
	print(i)