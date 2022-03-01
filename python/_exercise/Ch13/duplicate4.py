import dupdata
data = dupdata.df
print(data)
print("---------------")
print(data.drop_duplicates( )) 
print("---------------")
print(data.drop_duplicates(keep='last')) 
print("---------------")
print(data.drop_duplicates(keep=False))
