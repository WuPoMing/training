import pandas as pd
ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo['City'].head(10))
print('------------------------')
ufo['Location'] = ufo.City + ', ' + ufo.State
print(ufo['Location'].head(10))
