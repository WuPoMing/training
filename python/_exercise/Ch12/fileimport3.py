import pandas as pd
df1 = pd.read_csv("area.csv")  
print(df1)
print('--------------------------')
df2 = pd.read_csv('area.csv', header=0, index_col=0)
print(df2)
print('--------------------------')
