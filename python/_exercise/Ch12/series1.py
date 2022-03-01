import pandas as pd
fruits = ["蘋果", "橘子", "梨子", "櫻桃"]
s1 = pd.Series(fruits)
print(type(s1))
print(s1)
print(s1.index)
print(s1.values)
print("-------------------------------------")
quantities = [15, 33, 45, 55]
s2 = pd.Series(quantities, index=fruits)
print(type(s2))
print(s2)
print(s2.index)
print(s2.values)
print("-------------------------------------")

