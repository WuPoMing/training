import matplotlib.pyplot as plt
height1 = [100.7, 195.6, 94.3, 127.1, 111.7, 159.7, 135, 149.9, 124.3, 112.9, 176.7, 110.2, 123.9, 161.9, 107.8]
weight1 = [57, 58.2, 58.6, 59.6, 59.8, 60.2, 60.5, 60.6, 60.7, 61.3, 61.3, 61.4, 61.8, 61.9, 62.3]
height2 = [151.8, 156.3, 136.1, 124.2, 156.3, 130, 181.2, 255.9, 163.1, 123.1, 119.5, 179.9, 114.8, 174.1, 108.8]
weight2 = [62.9, 63, 63.1, 63.2, 63.3, 63.4, 63.4, 63.4, 63.5, 63.6, 63.7, 64.1, 64.3, 64.3, 64.7]
height3 = [166.8, 172.9, 193.8, 137.4, 162.4, 137.1, 169.1, 237.1, 189.1, 179.3, 174.8, 213.3, 198, 191.1, 220.6]
weight3 = [69.2, 69.2, 69.4, 69.7, 70, 70.3, 70.8, 71, 71.1, 71.7, 71.9, 72.4, 73, 73.1, 76.2]
height = height1+height2+height3
weight = weight1+weight2+weight3
color_array = ['b'] * 15 + ['g'] * 15 + ['r'] * 15
plt.scatter(height, weight, marker='*', c=color_array)
plt.xlabel('height', fontsize=16)
plt.ylabel('weight', fontsize=16)
plt.title('grouped scatter plot - height vs weight', fontsize=20)
plt.show( )
