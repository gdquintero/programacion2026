import numpy as np
import time

def bubble(v):
	n = len(v)

	for i in range(n - 1):
		swaps = False

		for j in range(n - 1 - i):
			if v[j] > v[j + 1]:
				v[j], v[j + 1] = v[j + 1], v[j]
				swaps = True

		if not swaps:
			break
	return v

n = 20000
v = np.linspace(n,1,n)

star = time.time()
bubble(v)
finish = time.time()

print("Tiempo: ", finish - star)