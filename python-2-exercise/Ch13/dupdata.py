import pandas as pd
raw_data = {'first_name': ['Jason', 'Jason', 'Jason','Tina', 'Jake', 'Amy'],
            'last_name': ['Miller', 'Miller', 'Miller','Ali', 'Python', 'Pcschool'],
            'age': [42, 42, 42, 36, 24, 42],
            'preTestScore': [4, 4, 4, 31, 2, 3],
            'postTestScore': [25, 25, 25, 57, 62, 70],
            'testdata':[3,3,3,3,3,3]}
df = pd.DataFrame(raw_data)

#print(df)
