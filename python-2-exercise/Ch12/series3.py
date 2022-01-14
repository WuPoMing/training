import pandas as pd
quantities = [15, 33, 45, 55]
s5 = pd.Series(quantities)
print(s5.count( ))
print(s5.median( ))
print(s5.mean( ))
print(s5.min( ))
print(s5.max( ))
print("---------")
print(s5.describe( ))
print(s5.var( ))
print(s5.std ( ))
print("---------")
print(s5.apply(lambda x:x**2))

