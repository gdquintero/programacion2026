import numpy as np

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

v = np.array([5,4,3,2,1])

print(bubble(v))