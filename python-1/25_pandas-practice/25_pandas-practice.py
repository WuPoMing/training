# 載入 pandas 模組
import pandas as pd

# 建立 Series
data=pd.Series([20, 10, 15])

# 基本 Series 操作
print(data)
print("====================")
print("Max:", data.max())
print("====================")
print("Median:", data.median())
print("====================")

data=data*2
print(data)
print("====================")

data=data==20
print(data)
print("====================")

# 建立 DataFrame
data=pd.DataFrame({
    "name":["Amy", "John", "Bob"],
    "salary":[30000, 50000, 40000]
})

# 基本 DataFrame 操作
print(data)
print("====================")
print(data["name"])     # 取得特定的欄位
print("====================")
print(data.iloc[0])     # 印出第一列