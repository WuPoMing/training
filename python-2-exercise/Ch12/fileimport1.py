import pandas as pd
df1 = pd.read_csv("brics.csv")
print(df1)
print('--------------------------')
df2 = pd.read_csv("brics.csv",header=0, index_col=0)
print(df2)
print('--------------------------')
