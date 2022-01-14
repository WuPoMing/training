import matplotlib.pyplot as plt
city = ['Delhi', 'Beijing', 'Washington', 'Tokyo', 'Moscow']
Gender = ['Male', 'Female']
Happiness_Index_Male = [60, 40, 70, 65, 85]
Happiness_Index_Female = [30, 60, 70, 55, 75]
plt.xlabel('City', fontsize=16)
plt.ylabel('Happiness_Index', fontsize=16)
plt.title('Stacked Barchart ', fontsize=18)
plt.bar(city, Happiness_Index_Male, color='blue', edgecolor='black')
plt.bar(city, Happiness_Index_Female, color='pink', edgecolor='black', bottom=Happiness_Index_Male)
#plt.legend(Gender,loc=2)
plt.show( )
