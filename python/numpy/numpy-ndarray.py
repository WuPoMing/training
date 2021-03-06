import os
os.system("clear")

# 載入 numpy 套件
import numpy as np

# 建立一維陣列
data = np.array([3, 4, 5, 6])
data = np.empty(4) # 創造一個有四個資料的一維陣列，資料未指定
data = np.zeros(3)
data = np.ones(3)
data = np.arange(9)

# 建立二維陣列
data = np.array([ # 創造一個 3x3 的二維陣列
    [2, 3, 2],
    [1, 5, 2],
    [4, 2, 1]
])
data = np.empty([3,3]) # 創造一個 3x3 的二維陣列，資料未指定
data = np.ones([2,3])

# 建立三維陣列
data = np.array([ # 根據列表創造一個 2x2x2 的三維陣列
    [
        [1,3],[2,5]
    ],
    [
        [2,4],[1,1]
    ]
])
data = np.zeros([3,1,3]) # 創造一個 3x1x3 的三維陣列，資料都是 0

# 建立高維陣列
data = np.array([ # 創造一個 1x1x2x3 的四維陣列
    [
        [
            [
                [0,3,5]
            ],
            [
                [3,4,5]
            ]
        ]
    ]
])
data = np.ones([2,1,1,2]) # 創造一個 2x1x1x2 的四維陣列，資料都是 1

print(data)