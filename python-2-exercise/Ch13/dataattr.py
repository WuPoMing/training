import pandas as pd
df1 = pd.read_csv("brics.csv", header=0, index_col=0)
print(df1)
print('--------------------------')
print("ndim", df1.ndim)
print("shape", df1.shape)
print("size", df1.size)
print("index", df1.index)
print("columns", df1.columns)
print('--------------------------')
print("info():")
print(df1.info())
print("count():")
print(df1.count())
print("describe():")
print(df1.describe())
print('--------------------------')
print("sum():")
print(df1.sum())
print("population mean():", df1['population'].mean())
print("area median():", df1.area.median())
print("population min():", df1['population'].min())
print("population max():", df1['population'].max())
print("std():")
print(df1.std())