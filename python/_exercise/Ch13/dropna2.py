import missdata
import numpy as np
data = missdata.df
data['location'] = np.nan
print(data)
print("----------------------------------------")
df_drop_col= data.dropna(axis=1, how='all') 
print(df_drop_col)
print("----------------------------------------")
df_drop_thresh = data.dropna(thresh=6)
print(df_drop_thresh)
print("----------------------------------------")
df_drop_thresh2 = data.dropna(thresh=5)
print(df_drop_thresh2)
print("----------------------------------------")
