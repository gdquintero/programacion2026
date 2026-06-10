import numpy as np
import matplotlib.pyplot as plt
import time

def insertion_sort(x):
    n = len(x)

    for i in range(1,n):
        key = x[i]
        j = i - 1

        while key < x[j] and j >= 0:
            x[j + 1] = x[j]
            j -= 1

        x[j + 1] = key

    return x

sizes = np.linspace(500,5000,100,dtype=int)
tn = np.zeros(len(sizes))
i = 0
ordered = False

for n in sizes:
    print(i)

    if ordered: x = np.linspace(1,n,n,dtype=int) 
    else: x = np.linspace(n,1,n,dtype=int)

    start = time.time()
    insertion_sort(x)
    finish = time.time()
    tn[i] = finish - start
    i += 1

plt.plot(sizes,tn,"or")
plt.show()