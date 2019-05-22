from scipy import signal

import matplotlib.pyplot as plt
import numpy as np

# Einlesen der .csv Datei
data = np.load('data/test.npy')
window = np.zeros((881, 513))
z = 511

for y in range(0, 878):
    z = z - 256
    for x in range(0, 512):
        z = z + 1
        window[y, x] = data[z]

gaussianwindow = signal.windows.gaussian(512, std=4)

# Darstellung des Amplitudenspektrums
plt.plot(gaussianwindow)
plt.grid()
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude in V')
plt.savefig('data/img/testamp.png')
plt.show()
