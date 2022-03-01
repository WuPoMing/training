import matplotlib.pyplot as plt
city = ['Delhi', 'Beijing', 'Washington', 'Tokyo', 'Moscow']
Happiness_Index = [60, 40, 70, 65, 85]
plt.barh(city, Happiness_Index, color='blue', edgecolor='black')
plt.xlabel('Index', fontsize=16)
plt.ylabel('City', fontsize=16)
plt.title('Barchart - 2', fontsize=20)
plt.show( )
