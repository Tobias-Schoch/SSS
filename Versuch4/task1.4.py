from scipy import signal

import matplotlib.pyplot as plt
import numpy as np

# Einlesen der .csv Datei
data = np.load('data/test.npy')
window = np.zeros((881, 513))
z = 511
gaussianwindow = signal.windows.gaussian(512, std=4)
for y in range(0, 878):
    z = z - 256
    for x in range(0, 512):
        z = z + 1
        window[y, x] = np.mean(np.abs(np.fft.fft(data[z]*gaussianwindow)))


# Darstellung des Amplitudenspektrums
plt.plot(window)
plt.grid()
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude in V')
plt.savefig('data/img/14_1.png')
plt.xlim(0, 880)
plt.show()
window2 = np.zeros((879, 512))
window3 = np.zeros((879, 512))
window4 = np.zeros((879, 512))
window5 = np.zeros((879, 512))

for x in range(0, 879):
    y = 256*x
    window2[x] = data[0 +y:512 + y]

for y in range(0, 879):
    for x in range(0, 512):
        window3[y][x] = window2[y][x] * gaussianwindow[x]

for x in range(0, 879):
    window4[x] = np.abs(np.fft.fft(window3[x]))

for x in range(0, 879):
    window5[x] = np.mean(window4[x])

plt.plot(window5)
plt.grid()
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude in V')
plt.savefig('data/img/14_2.png')
plt.xlim(0, 880)
plt.show()