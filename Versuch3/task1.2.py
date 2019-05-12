import matplotlib.pyplot as plt
import numpy as np

# Einlesen der .csv Datei
x, y = np.loadtxt('data/eins.csv', delimiter=',', unpack=True)

# Darstellung des Signals unserer Mundharmonikaaufnahme
plt.plot(x * 1000, y * 1000, 'b')
plt.ylabel('Spannung in mV')
plt.xlabel('Zeit in ms')
plt.grid(True)
plt.savefig('data/img/mundharmonika.png')
plt.show()