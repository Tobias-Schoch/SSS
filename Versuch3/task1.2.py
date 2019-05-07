import matplotlib.pyplot as plt
import numpy as np

# Grundperiode:     10ms
# Grundfrequenz:    100Hz
# Signaldauer:      25ms
# Abtastintervall:  10μs
# Signallänge:      2500
# Abtastfrequenz:   1MH

period = 10
frequence = 100
singaltime = 25
keyintervall = 10
singallength = 2500
keyfrequence = 1

x, y = np.loadtxt('data/großerLautsprecher/100.csv', delimiter=',', unpack=True)

plt.plot(x, y)
plt.grid(True)
plt.figure()
plt.ylabel('Spannung in V')
plt.xlabel('Zeit t')
plt.show()



