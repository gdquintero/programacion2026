import numpy as np
import scipy as sc

def lu_sparse(a,b,c,n):
    l = np.zeros(n)
    u = np.zeros(n)

    u[0] = b[0]

    for i in range(1,n):
        l[i] = a[i] / u[i-1]
        u[i] = b[i] - l[i] * c[i-1]

    return l,u

def packing(n):
    a = np.zeros(n)
    b = 2 * np.ones(n)
    c = np.zeros(n)

    a[-1] = (2*n - 1) / (2*n)

    for i in range(1,n-1):
        a[i] = (2*i - 1) / (4*i)

    c[:-1] = 1 - a[:-1]

    return a,b,c

n = 4

a,b,c = packing(n)
l,u = lu_sparse(a,b,c,n)


A = np.zeros((n,n))

for i in range(n):
    A[i,i] = b[i]

    if i != n-1:
        A[i+1,i] = a[i+1]
        A[i,i+1] = c[i]
    

P,L,U = sc.linalg.lu(A)


print(c)
print()
print(U)

print()
