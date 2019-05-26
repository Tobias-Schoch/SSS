from scipy import signal

import matplotlib.pyplot as plt
import numpy as np

# Einlesen der .csv Datei
data = np.load('data/test.npy')
window = np.zeros((879, 512))
z = 256
freq = np.zeros(225280)
gaussianwindow = signal.windows.gaussian(512, std=4)
for y in range(0, 879):
    z = z - 256
    for x in range(0, 512):
        window[y, x] = np.mean(np.abs(np.fft.fft(data[z] * gaussianwindow)))
        z = z + 1
    # plt.plot(window[y])
    # plt.title('Windownr' + str(y+1))
    # plt.xlabel('Signalnr.')
    # plt.ylabel('Frequenz')
    # plt.grid(True)
    # plt.savefig('data/img/' + str(y) + '.png')
    # plt.show()

# Darstellung des Amplitudenspektrums
plt.plot(gaussianwindow)
plt.grid(True)
plt.xlabel('Signalnr.')
plt.ylabel('Frequenz')
plt.savefig('data/img/gauss.png')
plt.show()

# Darstellung des Amplitudenspektrums
plt.plot(window)
plt.grid(True)
plt.xlabel('Signalnr.')
plt.ylabel('Frequenz')
plt.savefig('data/img/Alle.png')
plt.show()

for y in range(0, 879):
    for x in range(0, 512):
        window[y][x] = window[y][x] * gaussianwindow[x]
    window[y] = np.abs(np.fft.fft(window[y]))
    window[y] = np.mean(window[y])

plt.plot(window, 'r')
plt.grid(True)
plt.xlabel('Signalnr.')
plt.ylabel('Frequenz')
plt.savefig('data/img/AlleRichtig.png')
plt.show()

# Der zweite Wert wird absolut minus den ersten absoluten wert gerechnet um später den Wert
difference = 2 / 225280
# Die zweite Spalte der .csv Datei wird Fouriertransformiert
fourier = np.fft.fft(window)
# Die Fouriertransformierte Frequenz wird absolutiert, so dass kein negativer Wert mehr vorzufinden ist
spektrum = np.abs(fourier)
# Formel um die Anzahl der Schwingungen in die Freuquenz umzurechnen - f = n / (M * t)
for x in range(0, 225280, 1):
    freq[x] = (x / (difference * 225280))

plt.plot(freq, 'r')
plt.grid(True)
plt.xlabel('Signalnr.')
plt.ylabel('Frequenz')
plt.savefig('data/img/ampwin.png')
plt.show()