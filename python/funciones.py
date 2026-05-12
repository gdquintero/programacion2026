import numpy as np

# Definiendo funciones en piton

def saluda(nombre="Fulano de Tal"):
    print(f"Hola de nuevo, {nombre}")

def f(x):
    return x**2 + 2*x - 1

def cuadrado_cubo(x):
    return x**2, x**3

def polinomio_estatico(c0,c1,c2,c3,c4,x):
    return c0 + (c1 * x) + (c2 * x**2) + (c3 * x**3) + (c4 * x**4)

def polinomio_dinamico(coef,x):

    n = len(coef)

    aux = np.zeros(n)

    for i in range(n):
        aux[i] = x**i

    return np.dot(coef,aux)
    

# saluda("David")
# saluda()

numero = 2
cuadrado, cubo = cuadrado_cubo(numero)

print(f"El cuadrado de {numero} es {cuadrado} y su cubo es {cubo}")

print(f"El polinomio evaluado en {numero} es {polinomio_estatico(1,1,1,1,1,numero)}")

coef = np.array(
    [1,1,1,1,1,1,1,1,1,1,1]
)

print(polinomio_dinamico(coef,numero))