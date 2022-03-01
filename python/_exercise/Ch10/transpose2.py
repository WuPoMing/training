import numpy as np
a = np.array([[1, 2, 3], [13, 6, 9], [12, 24, 36]])
print(a)
print("---------------")
for row in a:
    print(row)
print("---------------")
for column in a.T:
    print(column)
print("---------------")
