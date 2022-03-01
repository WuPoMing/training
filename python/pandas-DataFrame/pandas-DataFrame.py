import pandas as pd

# 資料索引
data=pd.DataFrame({
    "name":["Amy", "Bob", "Charles"],
    "salary":[30000, 50000, 40000]
}, index=["a", "b", "c"])
print(data)
print("====================")

# 觀察資料
print("資料數量", data.size)
print("資料形狀（欄、列）", data.shape)
print("資料索引", data.index)
print("====================")

# 取得列 (row) 的 Series 資料：根據順序、根據索引
print("取得第二列", data.iloc[2], sep="\n")
print("====================")
print("取得第 c 列", data.loc["c"], sep="\n")
print("====================")

# 取得欄 (column) 的 Series 資料：根據欄位名稱
print("取得 name 欄位", data["name"], sep="\n")
print("====================")
names=data["name"]      # 取得單維度的 Series 資料 
print("把 name 全部轉大寫", names.str.upper(), sep="\n")
print("====================")
salaries=data["salary"]
print("薪水的平均值", salaries.mean())
print("====================")

# 建立新的欄位
data["revenue"]=[500000, 400000, 300000]        # data[新欄位名稱]=列表
print(data)
print("====================")
data["rank"]=pd.Series([3, 6, 1], index=["a", "b", "c"])
print(data)
print("====================")
data["cp"]=data["revenue"]/data["salary"]
print(data)