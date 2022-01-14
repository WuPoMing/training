import pandas as pd
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
url = 'http://bit.ly/movieusers'
users = pd.read_table(url, sep='|', header=None, names=user_cols, index_col='user_id')
print(users)
print(users.zip_code.duplicated()) 
print("---------------")
dup_count=users.zip_code.duplicated().sum() 
print(dup_count)
print("---------------")
zips=users.zip_code.unique()
print(len(zips))
print("---------------")


