import numpy as np
a = np.array([[2,3],[4,5]])
b=np.arange(4).reshape((2,2))
c=a*b
print(c)
print("---------------")
d=np.dot(a,b)
print(d)
print("---------------")
e=np.inner(a,b)
print(e)
print("---------------")
