# 儲存檔案
file=open("13_data.txt", mode="w", encoding="UTF-8") # 開啟
file.write("測試中文\nSecond File") # 操作
file.close() # 關閉

with open("13_data.txt", mode="w", encoding="utf-8") as file:
    file.write("5\n3\n9")

# 讀取檔案
# 把檔案中的數字資料, 一行一行讀取出來, 並計算總和
sum=0
with open("13_data.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        sum+=int(line)
print(sum)

# 使用 .json 格式讀取、覆寫檔案
import json
with open("13_config.json", mode="r") as file:
    data=json.load(file)
print(data) # data 是一個字典資料
print("name:", data["name"])
print("version:", data["version"])
data["name"]="New Name" # 修改變數中的資料

# 把最新的資料覆寫回檔案中
with open("13_config.json", mode="w") as file:
    data=json.dump(data, file)