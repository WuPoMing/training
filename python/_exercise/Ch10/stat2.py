import numpy as np
a = np.array([[0, 30,45],[60,75,90]])
print(a)
print("---------------")
b=np.min(a)
print(b)
print("---------------")
c=np.min(a,axis=0)
print(c)
print("---------------")
d=np.min(a,axis=1)
print(d)
print("---------------")