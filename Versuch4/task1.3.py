import matplotlib.pyplot as plt
import numpy as np

# Einlesen der .csv Datei
data = np.load('data/Failure/Trial1/test.npy')
# 2 Zeilen aus der linken Spalte in time schreiben
#time = data[:2, 0]
# Der zweite Wert wird absolut minus den ersten absoluten wert gerechnet um später den Wert
#difference = np.abs(time[1] - time[0])
# Die zweite Spalte der .csv Datei wird Fouriertransformiert
#fourier = np.fft.fft(data[:, 1])
# Die Fouriertransformierte Frequenz wird absolutiert, so dass kein negativer Wert mehr vorzufinden ist
#spektrum = np.abs(fourier)
# Formel um die Anzahl der Schwingungen in die Freuquenz umzurechnen - f = n / (M * Δt)
freq = range(0, 44100, 1) / (difference * 2500)

# Darstellung des Amplitudenspektrums
#plt.plot(freq, spektrum)
#plt.grid()
#plt.xlabel('Frequency in Hz')
#plt.ylabel('Amplitude in V')
#plt.xlim(0, 20000)
#plt.savefig('data/img/mundharmonika2.png')
#plt.show()
print(data)
