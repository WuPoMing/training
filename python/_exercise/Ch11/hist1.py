import matplotlib.pyplot as plt
values = [82, 76, 24, 40, 67, 62, 75, 78, 71, 32, 98, 89, 78, 67, 72, 82, 87, 66, 56, 52]
plt.hist(values, 5, histtype='bar', align='mid', color='c', label='Test score Data', edgecolor='black')
#plt.hist(values, 5, histtype='step', align='mid', color='g', label='Test Score Data')
plt.legend(loc=2)
plt.title('Histogram of score')
plt.show()
