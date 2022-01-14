import matplotlib.pyplot as plt
values = [60, 80, 90, 55, 10, 30]
colors = ['b', 'g', 'r', 'c', 'm', 'y']
labels = ['US', 'UK', 'India', 'Germany', 'Australia', 'South Korea']
plt.title('Population Density Index')
plt.pie(values, colors=colors, labels=labels, autopct='%.0f%%')
plt.axis('equal')
plt.show( )

