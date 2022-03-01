import pandas as pd
data1 = {'Name'   : pd.Series(['Tom', 'Jack', 'Stella', 'Ricky']),
         'Age'    : pd.Series([28,34,29,42]),
         'Gender' : pd.Series(['M', 'M', 'F', 'M'])}
df1 = pd.DataFrame(data1)
print(df1)
print('--------------------')
data2 = [pd.Series(['Tom', 28, 'M'],   index=('Name', 'Age', 'Gender')),
         pd.Series(['Jack', 34, 'M'],  index=('Name', 'Age', 'Gender')),
         pd.Series(['Stella', 29, 'F'],index=('Name', 'Age', 'Gender')),
         pd.Series(['Ricky', 42, 'M'], index=('Name', 'Age', 'Gender'))]
df2 = pd.DataFrame(data2)
print(df2)
print('--------------------')
