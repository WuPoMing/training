import pandas as pd
df = pd.read_csv('area.csv', header=0, index_col=0)
print(df.nlargest(3, 'population'))
print()
print(df.nsmallest(4, 'population'))
