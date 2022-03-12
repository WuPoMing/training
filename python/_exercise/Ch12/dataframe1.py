import pandas as pd
data = {'Name':['Tom', 'Jack', 'Stella', 'Ricky'],'Age':[28,34,29,42],'Gender':['M','M','F','M']}
df1 = pd.DataFrame(data)
print(df1)
print('--------------------')
df2 = pd.DataFrame(data, index=['emp1','emp2','emp3','emp4'])
print(df2)
print('--------------------')
df3 = pd.DataFrame(data, index=range(1,5), columns=(['Name','Gender']))
print(df3)
print('--------------------')
df4 = pd.DataFrame(data, index=range(1,5), columns=(['Name','Age']))
print(df4)
print('--------------------')