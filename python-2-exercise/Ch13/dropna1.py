import missdata
data = missdata.df
print(data)
print("----------------------------------------")
df_drop_any= data.dropna() 
print(df_drop_any)
print("----------------------------------------")
df_drop_all = data.dropna(how='all')
print(df_drop_all)
print("----------------------------------------")
