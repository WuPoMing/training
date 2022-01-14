import matplotlib.pyplot as plt
height1 = [156.3, 100.7, 114.8, 156.3, 237.1, 123.9, 151.8, 164.7, 105.4, 136.1, 175.2, 137.4, 164.2, 151, 124.3]
weight1 = [63.3, 57, 64.3, 63, 71, 61.8, 62.9, 65.6, 64.8, 63.1, 68.3, 69.7, 65.4, 66.3, 60.7]
plt.scatter(height1, weight1, c='b', marker='o')
plt.xlabel('height', fontsize=16)
plt.ylabel('weight', fontsize=16)
plt.title('scatter plot - height vs weight', fontsize=20)
plt.show( )
