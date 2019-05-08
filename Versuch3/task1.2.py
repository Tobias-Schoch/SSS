import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('data/Mundharmonika/eins.csv', delimiter=',', unpack=True)
data = np.loadtxt('data/Mundharmonika/eins.csv', delimiter=',', unpack=True)

# Darstellung des Signals unserer Mundharmonikaaufnahme
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

fft = np.fft.fft(y)

# Darstellung des Signals unserer Mundharmonikaaufnahme
plt.plot(np.abs(fft))
plt.ylabel('Spannung in V')
plt.xlabel('Zeit t')
plt.grid(True)
plt.show()

qq = int(len(fft) / 2 + 1)

# Darstellung des Signals unserer Mundharmonikaaufnahme
plt.plot(np.abs(fft)[:qq])
plt.ylabel('Spannung in V')
plt.xlabel('Zeit t')
plt.grid(True)
plt.show()
