import matplotlib.pyplot as plt
import numpy as np

# Einlesen der .csv Datei
data = np.load('data/test.npy')
freq = np.zeros(225280)

# Darstellung des Amplitudenspektrums
plt.plot(data)
plt.grid()
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude in V')
plt.savefig('data/img/hoch1.png')
plt.show()

# Der zweite Wert wird absolut minus den ersten absoluten wert gerechnet um später den Wert
difference = 2 / 225280
# Die zweite Spalte der .csv Datei wird Fouriertransformiert
fourier = np.fft.fft(data[:225280])
# Die Fouriertransformierte Frequenz wird absolutiert, so dass kein negativer Wert mehr vorzufinden ist
spektrum = np.abs(fourier)
# Formel um die Anzahl der Schwingungen in die Freuquenz umzurechnen - f = n / (M * Δt)
for x in range(0, 225280, 1):
    freq[x] = x / (difference * 225280)

# Darstellung des Amplitudenspektrums
plt.plot(freq, spektrum)
plt.grid()
plt.xlabel('Frequency in Hz')
plt.ylabel('Amplitude in V')
plt.savefig('data/img/hoch1.png')
plt.xlim(0, 40000)
plt.show()
