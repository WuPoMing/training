import pandas as pd
df1 = pd.read_csv("brics2.csv")
print(df1)
print('--------------------------')
cols=['code','country','population','area','capital']
df2 = pd.read_csv("brics2.csv", header=None, names=cols)
print(df2)
print('--------------------------')
cols2=['country','population','area','capital']
df3 = pd.read_csv("brics2.csv", names=cols2, index_col=0)
print(df3)
print('--------------------------')
