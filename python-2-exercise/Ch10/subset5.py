import numpy as np
arr = np.array([3, -2, -1, 5, 7, -3])
print(arr)
print('-----------------')
print(arr[::-1])
print('-----------------')
print(arr[1:6:2])
print('-----------------')
print(arr>0)
print(arr[arr>0])