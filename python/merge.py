import numpy as np
import matplotlib.pyplot as plt
import time

def merge(A, p, q, r):
    # Copiar la mitad izquierda A[p..q] en un arreglo temporal L
    L = A[p:q+1].copy()
    # Copiar la mitad derecha A[q+1..r] en un arreglo temporal R
    R = A[q+1:r+1].copy()
    
    i = 0   # índice para recorrer L, empieza en el primer elemento
    j = 0   # índice para recorrer R, empieza en el primer elemento
    k = p   # índice para rellenar A, empieza en la posición p
    
    # Mientras queden elementos en AMBOS arreglos L y R
    while i < len(L) and j < len(R):
        # Si el elemento actual de L es menor o igual al de R
        if L[i] <= R[j]:
            A[k] = L[i]  # copiar elemento de L en A
            i += 1       # avanzar en L
        else:
            A[k] = R[j]  # copiar elemento de R en A
            j += 1       # avanzar en R
        k += 1           # avanzar en A (siguiente posición a rellenar)
    
    # Si quedaron elementos en L (R se agotó primero), copiarlos
    while i < len(L):
        A[k] = L[i]  # copiar elemento restante de L en A
        i += 1       # avanzar en L
        k += 1       # avanzar en A
    
    # Si quedaron elementos en R (L se agotó primero), copiarlos
    while j < len(R):
        A[k] = R[j]  # copiar elemento restante de R en A
        j += 1       # avanzar en R
        k += 1       # avanzar en A


def merge_sort(A, p, r):
    # Caso base: si el subarreglo tiene 1 solo elemento, ya está ordenado
    if p < r:
        # Calcular el punto medio para dividir el subarreglo en dos mitades
        q = (p + r) // 2
        # Conquistar: ordenar recursivamente la mitad izquierda A[p..q]
        merge_sort(A, p, q)
        # Conquistar: ordenar recursivamente la mitad derecha A[q+1..r]
        merge_sort(A, q+1, r)
        # Combinar: mezclar las dos mitades ya ordenadas
        merge(A, p, q, r)


sizes = np.linspace(500,5000,100,dtype=int)
tn = np.zeros(len(sizes))
i = 0
ordered = False

for n in sizes:
    print(i)

    if ordered: x = np.linspace(1,n,n,dtype=int) 
    else: x = np.linspace(n,1,n,dtype=int)

    start = time.time()
    np.sort(x)
    finish = time.time()
    tn[i] = finish - start
    i += 1

plt.plot(sizes,tn,"or")
plt.show()