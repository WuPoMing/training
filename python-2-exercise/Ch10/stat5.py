import numpy as np
a = np.array([1,2,3,4])
wts = np.array([4,3,2,1])
b=np.average(a)
print(b)
print( )
c=np.average(a, weights=wts)
print(c)
print( )
d=np.average(a, weights=wts, returned = True)
print(d)
print( )
