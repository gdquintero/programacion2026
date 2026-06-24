import numpy as np

def compute_min(v,n):

	minimum = v[0]
	pos = 0

	for i in range(1,n):
		if v[i] < minimum:
			minimum = v[i]
			pos = i

	return minimum,pos

def selection(v,n):

	for i in range(n - 1):
		key,pos = compute_min(v[i:],n - i)
		v[i + 1:pos + 1 + i] = v[i:pos + i] 
		v[i] = key

	return v
		

v = np.array([5,-3,4,1,0,-5,5,7,2,1,4,0,3])
n = len(v)


print(selection(v,n))
