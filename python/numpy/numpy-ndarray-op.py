import os
os.system("clear")

# 載入 numpy 套件
import numpy as np

# 逐元運算(elementwise)
data1 = np.array([3,5,6])
data2 = np.array([5,3,7])
result = data1+data2
result = data1*data2
result = data1>data2 # 是否大於
result = data1==data2 # 是否等於

# 矩陣運算(matrix)
data1 = np.array([ #1x2
    [1, 3]
])
data2 = np.array([ # 2x3
    [2, -1, 3],
    [-2, 4, 1]
])
result = data1@data2 #result = data1.dot(data2) # 1x3 # 內積
result = np.outer(data1, data2) # 2x6 # 外積

# 統計運算(statistics)
data = np.array([ # 2x3
    [2, 1, 2],
    [3, 4, 5]
])
result = data.sum() # 總和
result = data.sum(axis=0) # 針對欄(column)做總和(針對第一個維度做總和)
result = data.sum(axis=1) # 針對列(row)做總和(針對第二個維度做總和)
result = data.max() # 最大值
result = data.min() # 最小值
result = data.mean() # 平均數
result = data.std() # 標準差
result = data.cumsum(axis=0) # 針對欄(column)做逐值累加(針對第一個維度做逐值累加)

print(result)