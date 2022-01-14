import matplotlib.pyplot as plt
import numpy as np
city = ['Delhi', 'Beijing', 'Washington', 'Tokyo', 'Moscow']
Gender = ['Male', 'Female']
pos = np.arange(len(city))
bar_width = 0.4
Index_Male = [60, 40, 70, 65, 85]
Index_Female = [30, 60, 70, 55, 75]
plt.xticks(pos, city)
plt.xlabel('City', fontsize=16)
plt.ylabel('Happiness_Index', fontsize=16)
plt.title('Group Barchart - ', fontsize=18)
plt.bar(pos-bar_width/2, Index_Male, bar_width, color='blue', edgecolor='black')
plt.bar(pos+bar_width/2, Index_Female, bar_width, color='pink', edgecolor='black')
plt.legend(Gender, loc=2)
plt.show( )
