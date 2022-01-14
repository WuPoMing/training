import missdata
data = missdata.df
print(data)
print("---------------")
print (data.fillna(method='ffill'))
print("---------------")
print (data.fillna(method='pad'))
print("---------------")
print (data.fillna(method='bfill'))
print("---------------")
print (data.fillna(method='backfill'))
print("---------------")

