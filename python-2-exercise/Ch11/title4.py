import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2
plt.figure(num=3, figsize=(8, 5),)
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')
plt.xticks(np.arange(5),('Tom', 'Dick', 'Harry', 'Sally', 'Sue') )
plt.yticks([-2, -1.8, -1, 1.22, 3],['really bad', 'bad', 'normal', 'good', 'really good'])
plt.show()
