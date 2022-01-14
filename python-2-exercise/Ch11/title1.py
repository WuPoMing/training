import matplotlib.pyplot as plt
days = range(1, 32, 3)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1, 28.6, 25.8, 30.2]
plt.plot(days, celsius)
plt.xlabel("Day")
plt.ylabel("Celsius")
plt.title("Temperature Record")
plt.show( )
