import pandas as pd
df1 = pd.read_csv("brics.csv", header=0, index_col=0)
print(df1.loc['BR'])
print('-----------------------------')
print(df1.loc['CH'])
