import pandas as pd
df = pd.read_csv('area.csv', header=0, index_col=0)
print(df)
print("---------------------")
print(df.pop('city'))
print("---------------------")
print(df)
print("---------------------")
del df['population']
print(df)
print("---------------------")

