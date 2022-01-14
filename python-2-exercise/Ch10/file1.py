import numpy as np
arr1 = np.random.randint(1, 10, [2,3])
print(arr1)
np.save('myArray', arr1)
print('----------')
arr2 = np.load('myArray.npy')
print(arr2)
print('----------')
