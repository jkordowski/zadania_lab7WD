import numpy as np

macierz1 = np.arange(6).reshape((2, 3))
a = np.sin(macierz1)
print(a)

macierz2 = np.arange(6).reshape((2, 3))
b = np.cos(macierz2)
print(b)

c = a + b
print(c)