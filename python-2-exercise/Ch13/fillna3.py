import missdata
data = missdata.df
median=data["testdata"].median( )
print("median of testdata column:",median)
print("---------------")
data["testdata"].fillna(median,inplace=True)
print(data)
print("---------------")
