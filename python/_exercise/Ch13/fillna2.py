import missdata
data = missdata.df
mean=data["testdata"].mean( )
print("mean of testdata column:",mean)
print("---------------")
fill_mean=data["testdata"].fillna(mean)
print(fill_mean)
print("---------------")
print(data)
print("---------------")
data["testdata"].fillna(mean,inplace=True)
print(data)
print("---------------")
