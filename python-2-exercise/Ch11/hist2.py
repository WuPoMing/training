import matplotlib.pyplot as plt
values = [82, 76, 24, 40, 67, 62, 75, 78, 71, 32, 98, 89, 78, 67, 72, 82, 87, 66, 56, 52]
plt.hist(values, bins=5, range=(0,100), histtype='bar', align='mid', color='c', edgecolor='black')
plt.title('Histogram of score')
plt.show()
