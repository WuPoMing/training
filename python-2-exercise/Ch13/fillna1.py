import missdata
data = missdata.df
fill_zero = data.fillna(0)  

print(fill_zero)
print("---------------")
print(data)
