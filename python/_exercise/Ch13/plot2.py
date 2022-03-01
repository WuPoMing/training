import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
fortune1000 = pd.read_csv("Fortune1000.csv",index_col="Rank")
fortune1000.dropna()
columns = ['Revenue', 'Profits', 'Employees']
gb_sector_num = fortune1000.groupby('Sector')[columns].mean()
gb_sector_num.plot(subplots=True)
plt.xticks(np.arange(len(gb_sector_num.index)), gb_sector_num.index, rotation='vertical')
plt.show()
