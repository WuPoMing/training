import os
os.system("clear")
'''
Iterable 資料型態:字串、列表、集合、字典

for 迴圈:
for 變數名稱 in 可疊代資料:
'''
dic = {"a":3, "test":5}
for key in dic:
    print(key)
    print(dic[key])

# 內建函式
'''
max(可疊代資料)
sorted(可疊代資料)
'''
result = max([10, 2, 30, 1])
print(result)
result = max("xaz")
print(result)
result = max({10, 200, 30, 1})
print(result)
result = max({"x":3, "a":4})
print(result)
result = sorted("asdfgh")
print(result)
result = sorted({10, 2, 100, -5})
print(result)