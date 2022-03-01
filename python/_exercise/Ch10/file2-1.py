import numpy as np
arr = np.loadtxt('data2.csv',skiprows=1, delimiter=',')
print(arr)
v1, v2 = np.loadtxt('data2.csv',skiprows=1,unpack=True, delimiter=',')
print("Value1=",v1)
print("Value2=",v2)
