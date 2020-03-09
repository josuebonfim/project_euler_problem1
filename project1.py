import numpy as np

n = 999

lista = []

for i in range(n):
	if((((i + 1) % 3) == 0) or ((((i + 1) % 5) == 0))):
		lista.append(i + 1)

lista = np.array(lista)

print(lista.sum())
