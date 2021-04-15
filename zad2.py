import numpy as np

a = np.array([np.arange(3), np.arange(3), np.arange(3)])
print(a)
b = np.arange(16).reshape((4, 4))
print(b)
print(a.min(axis=0), b.min(axis=0))
print(a.min(axis=1), b.min(axis=1))

