import matplotlib.pyplot as plt
city = ['Delhi', 'Beijing', 'Washington', 'Tokyo', 'Moscow']
Happiness_Index = [60, 40, 70, 65, 85]
plt.bar(city, Happiness_Index, color='blue', edgecolor='black', width=0.25)
plt.xlabel('City', fontsize=16)
plt.ylabel('Index', fontsize=16)
plt.title('Barchart ', fontsize=20)
plt.show()
