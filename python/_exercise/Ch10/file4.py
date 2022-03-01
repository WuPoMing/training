import numpy as np
arr = np.genfromtxt('data3.csv', delimiter=',', dtype='int', skip_header=1, encoding='utf-8')
print(arr)
print(arr.shape)
print(np.size(arr, axis=0))
print(np.size(arr, axis=1))
print(arr[0,0])
print(arr[1,2])
print(arr[2,3])
