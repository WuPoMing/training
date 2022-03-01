import pandas as pd
fruits = ["蘋果", "橘子", "梨子", "櫻桃"]
quantities = [15, 33, 45, 55]
s3 = pd.Series(quantities)
s3.index = fruits
print(s3)
print("---------") 
dict4 = {"蘋果":15, "橘子":33, "梨子":45, "櫻桃":55}
s4 = pd.Series(dict4)
print(type(s4))
print(s4)
print(s4.index)
print(s4.values)
print("---------")

