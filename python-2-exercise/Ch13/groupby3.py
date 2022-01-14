import pandas as pd
fortune1000 = pd.read_csv("Fortune1000.csv",index_col="Rank")
gb_sector = fortune1000.groupby('Sector')
print(gb_sector.agg({'Revenue':'mean','Profits':'mean','Employees':'sum'}))
