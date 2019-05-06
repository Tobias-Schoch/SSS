import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('data/großerLautsprecher/100.csv', delimiter=',', unpack=True)
x1, y1 = np.loadtxt('data/großerLautsprecher/100_2.csv', delimiter=',', unpack=True)

plt.plot(x, y)
plt.plot(x1, y1)
plt.grid(True)
plt.ylabel('logarithmierter Durchschnitt der Spannung in V')
plt.xlabel('logarithmierter Abstand in cm')
plt.show()


