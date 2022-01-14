import dupdata
data = dupdata.df
print(data)
print("---------------")
print(data.duplicated( ))
print("---------------")
print(data.duplicated('age'))
print("---------------")
print(data.duplicated('testdata'))
print("---------------")
