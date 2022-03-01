import matplotlib.pyplot as plt
x_labels = ['小', '中', '大']
x = range(len(x_labels))
y = [-3, 0, 3]
plt.scatter(x, y)
plt.title('中文標題')
plt.xticks(x,x_labels)
plt.tick_params(axis='x', which='major', labelsize=8)
plt.show()
