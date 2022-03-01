import pandas as pd
fortune1000 = pd.read_csv("Fortune1000.csv",index_col="Rank")
gb_sec_ind = fortune1000.groupby(['Sector', 'Industry'])
print(gb_sec_ind .size())
print('-----------------------')
print(gb_sec_ind.count())
print('-----------------------')
print(gb_sec_ind.Company.count())
print('-----------------------')
print(gb_sec_ind.Employees.count())
print('-----------------------')

