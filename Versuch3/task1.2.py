import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('data/Mundharmonika/eins.csv', delimiter=',', unpack=True)
data = np.loadtxt('data/Mundharmonika/eins.csv', delimiter=',', unpack=True)

# Darstellung der Logarithmierung von der avg Spannung und dem Abstand
plt.plot(x, y, 'b')
plt.ylabel('Spannung in V')
plt.xlabel('Zeit t')
plt.grid(True)
plt.show()

# Grundperiode:     1,586 ms
# Grundfrequenz:    630,52 Hz
# Signaldauer:      10 ms
# Abtastintervall:  4 μs
# Signallänge:      2500
# Abtastfrequenz:   4 MH

