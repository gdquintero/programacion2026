import numpy as np

def producto_matricial(A,B,m,n,p):
    res = np.zeros((m,p))

    for i in range(m):
        for j in range(p):
            res[i,j] = np.dot(A[i,:],B[:,j])

    return res

A = np.array([
    [1,2],
    [1,1],
    [2,1]
])

B = np.array([
    [2,3,1],
    [1,1,2]
])

C = producto_matricial(A,B,3,2,3)

print(C)
