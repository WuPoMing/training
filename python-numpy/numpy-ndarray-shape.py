import os
os.system("clear")

# 載入 numpy 套件
import numpy as np

# 多維陣列維度/形狀操作
# 觀察資料形狀
data = np.ones(10)
data = np.array([
    [3, 1, 5],
    [1, 2, 3]
])
print(data.shape)
print()

# 資料轉置
data = np.array([
    [2, 4, 1],
    [1, 5, 0]
])
print(data.shape) # (2, 3)
print(data.T.shape) # (3, 2)
print()

# 扁平化資料
data = np.array([
    [
        [2,1,3],[1,2,3]
    ],
    [
        [0,2,1],[8,9,10]
    ]
]) # (2, 2, 3)
newdata = data.ravel()
print(newdata)
print(newdata.shape)
print()

# 重塑資料形狀
data = np.array([
    [
        [2,1,3],[1,2,3]
    ],
    [
        [0,2,1],[8,9,10]
    ]
]) # 2x2x3=12
newdata = data.reshape(3, 4) # 3x4
print(newdata)
print()

data = np.zeros(18).reshape(3,2,3)
print(data)
print()

data = np.arange(9).reshape(3,3)
print(data)
print(data.T)