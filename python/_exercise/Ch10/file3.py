import numpy as np
arr1 = np.genfromtxt('data2.csv', delimiter=',', skip_header =1)
print(arr1)
np.savetxt('data2a.csv', arr1, delimiter=',')
arr2 = np.genfromtxt('data2.csv', delimiter=',', skip_header =1, filling_values= 0.0)
print(arr2)
np.savetxt('data2b.csv', arr2, delimiter=',',fmt='%.2f')

