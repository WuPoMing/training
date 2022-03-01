import dupdata
data = dupdata.df
print(data)
print("---------------")
print(data.duplicated(subset=['preTestScore','postTestScore'],keep=False))
print("---------------")
print(data.duplicated(subset=['preTestScore','postTestScore']))
print("---------------")
