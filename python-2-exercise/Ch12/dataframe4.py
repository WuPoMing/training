import numpy as np
import pandas as pd
data = np.array([['Tom', 28, 'M'], ['Jack', 34, 'M'], ['Stella', 29, 'F'], ['Ricky', 42, 'M']])
df1 = pd.DataFrame(data)
print(df1)
print('--------------------')
df2 = pd.DataFrame(data, index=range(1,5), columns=('Name', 'Age', 'Gender'))
print(df2)
print('--------------------')
