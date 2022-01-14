import pandas as pd
data = [{'Name':'Tom', 'Age': 28, 'Gender':'M'},
        {'Name':'Jack', 'Age': 34, 'Gender':'M'},
        {'Name':'Stella', 'Age': 29, 'Gender':'F'},
        {'Name':'Ricky', 'Age': 42, 'Gender':'M'}]
df1 = pd.DataFrame(data)
print (df1)
print('--------------------')
df2 = pd.DataFrame(data, index=['emp1','emp2','emp3','emp4'], columns=['Name','Age','Gender'])
print (df2)
print('--------------------')
df3 = pd.DataFrame(data, index=range(1,5), columns=['Name','Gender'])
print (df3)
print('--------------------')
df4 = pd.DataFrame(data, index=range(1,5), columns=['Name','age'])
print (df4)
print('--------------------')
