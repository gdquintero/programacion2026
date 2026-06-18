import numpy as np

# Ejercicio 1
def pow_rec(a,n):
	if a == 0 and n == 0:
		error = "El resultado es indeterminado"
		return error
	if a != 0:
		if n == 0:
			return 1
		elif n % 2 == 0:
			return pow_rec(a,n/2) * pow_rec(a,n/2)
		else:
			return a * pow_rec(a,n-1)

# Ejercicio 2
def mul_rec(a,b):
	if b == 0:
		return 0
	elif b % 2 == 0:
		return a * a * b / 2
	else:
		return a + a * (b - 1)

# Ejercicio 3
def horner(p,x0):
	
	if len(p) == 1:
		return p[-1]
	else:
		return p[0] + x0 * horner(p[1:],x0)

# Ejercicio 4
def mcd_rec(a,b):
	if b == 0:
		return a
	else:
		return mcd_rec(b,a%b)

# Ejercicio 5
def biseccion(f, a, b, tol):
	c = 0.5 * (a + b)

	if f(c) == 0 or (b - a) < tol:
		return c
	elif f(a) * f(c) < 0:
		return biseccion(f,a,c,tol)
	else:
		return biseccion(f,b,c,tol)


# Tests

# Ejercicio 1

print("Test ejercicio 1")
print(pow_rec(0,0))
print(pow_rec(2,5))

# Ejercicio 2
print("\nTest ejercicio 2")
print(mul_rec(-2,-3))

# Ejercicio 3
print("\nTest ejercicio 3")
p = np.array([1,2,-3,4])
x0 = 2
print(horner(p,x0))

# Ejercicio 4
print("\nTest ejercicio 4")
print(mcd_rec(45,30))

# Ejercicio 5
print("\nTest ejercicio 5")
f = lambda x: (x-1)**2 - 2
print(biseccion(f,1,3,1e-4))

