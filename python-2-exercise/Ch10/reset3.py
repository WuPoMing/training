import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = np.resize(a, (3,3))
print(b)
print(b.shape)
print( )
c = np.resize(a, (2,2))
print(c)
print(c.shape)
