import pandas as pd
df = pd.read_csv('area.csv', header=0, index_col=0)
print(df)
print("---------------------")
print(df.ix['third', 'city'])
print("---------------------")
print(df.ix[2, 2])
print("---------------------")
print(df.ix[['sixth','eigth','tenth'], 'name'])
print("---------------------")
print(df.ix[[5,7,9], 0])
print("---------------------")
print(df.ix['fifth':'ninth', "name":"city"])
print("---------------------")
print(df.ix[4:9, 0:3])
print("---------------------")
print(df.ix[5:9, "name":"city"])
print("---------------------")
print(df.ix["first", 0:2])
print("---------------------")

