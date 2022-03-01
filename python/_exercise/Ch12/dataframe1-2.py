import pandas as pd
names = ['Tom', 'Jack', 'Stella', 'Ricky']
ages=[28,34,29,42]
genders=['M', 'M', 'F', 'M']
emp_dict = { "Name": names, "Age": ages, "Gender": genders }
df1 = pd.DataFrame(emp_dict)
print (df1)
print('--------------------')
df2 = pd.DataFrame(emp_dict, index=range(1,5), columns=(['Name','Gender']))
print(df2)
print('--------------------')
df3 = pd.DataFrame(emp_dict, index=range(1,5), columns=(['Name','age']))
print(df3)
print('--------------------')


