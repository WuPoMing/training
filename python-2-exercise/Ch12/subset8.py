import pandas as pd
ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo)
print('--------------------------------')
print(ufo.head(10))
print('--------------------------------')
print(ufo[['City','State','Time']].tail())
print('--------------------------------')
print(ufo.loc[:, ['City','State','Time']].sample(6))
print('--------------------------------')
print(ufo.ix[10:500:10, ['City','State','Time']].sample(frac=0.1))

