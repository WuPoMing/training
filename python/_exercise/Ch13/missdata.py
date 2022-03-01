import pandas as pd
import numpy as np
raw_data = {'first_name': ['Jason', np.nan, 'Tina', 'Jake', 'Amy'],
            'last_name': ['Miller', np.nan, 'Ali', 'Milner', 'Cooze'], 
            'age': [42, np.nan, 36, 24, 73], 
            'sex': ['m', np.nan, 'f', 'm', 'f'], 
            'preTestScore': [4, np.nan, np.nan, 2, 3],
            'postTestScore': [25, np.nan, np.nan, 62, 70],
            'testdata': [14, np.nan, 2, 22, 33]}

df = pd.DataFrame(raw_data)
#print(df)
