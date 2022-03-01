import matplotlib.pyplot as plt
x = [1,2,3,4,5]
ch=[91, 95, 88, 100, 97]
en=[75, 90, 62, 80, 92]
plt.plot(x, ch, "r-o", x, en, "g--^")
plt.grid(which='major', axis='y') 
plt.show( )
