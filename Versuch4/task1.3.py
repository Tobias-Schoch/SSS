# -------------------------------------
# Task 1.3
# -------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# Einlesen der .npy Datei
data = np.load('data/test.npy')
freq = np.zeros(225280)

# Darstellung des Amplitudenspektrums
plt.plot(data)
plt.grid()
plt.xlabel('Zeit')
plt.ylabel('Amplitude')
plt.savefig('data/img/testamp.png')
plt.show()

# Einlesen der .csv Datei
data2 = np.load('data/rechts2.npy')

# Darstellung des Amplitudenspektrums
plt.plot(data2)
plt.grid()
plt.xlabel('Zeit')
plt.ylabel('Amplitude')
plt.savefig('data/img/rechtsamp.png')
plt.show()

# Darstellung des Amplitudenspektrums
plt.plot(data)
plt.grid()
plt.xlabel('Zeit')
plt.ylabel('Amplitude')
plt.xlim(50000, 75000)
plt.savefig('data/img/testamp2.png')
plt.show()

# Der zweite Wert wird absolut minus den ersten absoluten wert gerechnet um später den Wert
difference = 2 / 225280
# Die zweite Spalte der .csv Datei wird Fouriertransformiert
fourier = np.fft.fft(data[:225280])
# Die Fouriertransformierte Frequenz wird absolutiert, so dass kein negativer Wert mehr vorzufinden ist
spektrum = np.abs(fourier)
# Formel um die Anzahl der Schwingungen in die Freuquenz umzurechnen - f = n / (M * t)
for x in range(0, 225280, 1):
    freq[x] = (x / (difference * 225280))

# Darstellung des Amplitudenspektrums
plt.plot(freq, spektrum)
plt.grid()
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude in V')
plt.xlim(0, 60000)
plt.savefig('data/img/testspektrum1.png')
plt.show()

# Darstellung des Amplitudenspektrums in vergrößerter Darstellung
plt.plot(freq, spektrum)
plt.grid()
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude in V')
plt.xlim(0, 35000)
plt.savefig('data/img/testspektrum2.png')
plt.show()

# Darstellung des Amplitudenspektrums in vergrößerter Darstellung
plt.plot(freq, spektrum)
plt.grid()
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude in V')
plt.xlim(0, 1000)
plt.savefig('data/img/testspektrum3.png')
plt.show()