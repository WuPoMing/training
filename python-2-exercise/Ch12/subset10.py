import pandas as pd
df1 = pd.read_csv("brics.csv", header=0, index_col=0)
max_area = df1['area'].max()
print(df1[df1['area']==max_area])
print()

import numpy as np
df2 = pd.read_csv('area.csv', header=0, index_col=0)
min_pop = np.min(df2['population'])
print(df2[df2['population']==min_pop])
