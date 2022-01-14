import pandas as pd
df1 = pd.read_csv("brics.csv", header=0, index_col=0)
print(df1['capital'].loc['CH'])
print('-----------------------------')
print(df1.loc['CH']['capital'])
print('-----------------------------')
print(df1.loc['CH', 'capital'])
