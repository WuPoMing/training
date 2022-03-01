import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)
print( )
b = np.resize(a, (3,2))
print(b)
print(b.shape)
print( )
a[0,1]=100
print(a)
print(b)
