import numpy as np
x = np.array([[1, 2, 3], [13, 6, 9], [12, 24, 36]])
print(x)
print("---------------")
print(x.flatten( ))
print("---------------")
print(x.flatten(order='F'))
print("---------------")
