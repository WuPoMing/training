import numpy as np
l = [[1, 2, 3],
     [2, 3, 4]]
a = np.array(l)
print(a)
print("number of dim:", a.ndim)
print("shape:", a.shape)
print("len():", len(a))
print("len(a[0]):", len(a[0]))
print("size:", a.size)
print("dtype:", a.dtype)
print("itemsize:", a.itemsize)
print("nbytes:", a.nbytes)

