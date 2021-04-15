import numpy as np
a = np.arange(81).reshape((9, 9))

b = a.ravel()
c = a.reshape((3,27))
print(b)
print(c)
#mamy takie możliwości ponieważ tablica posiada 81 wartości i kaźdy nowy kształt także musi posiadać 81 wartości


