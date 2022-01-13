# 集合的運算
s1={3,4,5}
s2={4,5,6,7}
print(3 not in s1)

s3=s1&s2 # 交集：取兩集合重疊的資料
s4=s1|s2 # 聯集：取兩集合所有資料，但不重複
s5=s1-s2 # 差集：從s1中減去與s2重疊部分
s6=s1^s2 # 反交集：取兩集合不重疊的資料
print(s3,s4,s5,s6)

s = set("Hello") # 把字串中的字母拆解成集合：set(字串)
print(s)
print("H" in s)
print("A" in s)

# 字典的運算：key-value 配對
dic = {"apple":"蘋果", "bug":"蟲蟲"}
print(dic["apple"])

dic["apple"] = "小蘋果"
print(dic["apple"])

dic = {"apple":"蘋果", "bug":"蟲蟲"} # 判斷 key 是否存在
print("apple" in dic)
print("test" in dic)
print("test" not in dic)

print(dic)
del dic["apple"] # 刪除字典中的鍵配對(key-value pair)
print(dic)

dic = {x:x*2 for x in [3, 4, 5]} # 從列表的資料產生字典
print(dic)