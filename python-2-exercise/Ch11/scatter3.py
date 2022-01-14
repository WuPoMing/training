import matplotlib.pyplot as plt
import numpy as np
countries = ['Brazil', 'Madagascar', 'S. Korea', 'United States', 'Ethiopia', 'Pakistan', 'China', 'Belize']
birth_rate = [16.4, 33.5, 9.5, 14.2, 38.6, 30.2, 13.5, 23.0]
life_expectancy = [73.7, 64.3, 81.3, 78.8, 63.0, 66.4, 75.2, 73.7]
GDP = np.array([4800, 240, 16700, 37700, 230, 670, 2640, 3490])
colours = range(len(countries))
plt.scatter(birth_rate, life_expectancy, c=colours, s=GDP/10)
plt.xlabel('Birth rate per 1000 population')
plt.ylabel('Life expectancy at birth (years)')
plt.show( )
