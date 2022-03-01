import pandas as pd
import numpy as np
dates=pd.date_range('20180516',periods=6)
df=pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['a','b','c','d'])
print(df)
print("------------")
print(df['b'])
print("------------")
print(df.d)
print("------------")
print(df[0:3])
print("------------")
print(df['20180516':'20180518'])
print("------------")
