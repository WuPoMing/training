import pandas as pd
df1 = pd.read_csv("brics.csv", header=0, index_col=0)
print(df1['country'])
print('-----------------------------')
print(df1.capital)
print('-----------------------------')
print(df1[1:2])
print('-----------------------------')

