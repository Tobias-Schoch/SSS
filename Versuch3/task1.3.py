import matplotlib.pyplot as plt
import numpy as np

# Einlesen der .csv Datei
data = np.genfromtxt('data/eins.csv', delimiter=',', skip_header=0, skip_footer=0)

# linke Spalte der .csv Datei in t schreiben - t = zeit in s
t = data[:, 0]

# 2 Zeilen aus der linken Spalte in time schreiben
time = data[:2, 0]
# Der zweite Wert wird absolut minus den ersten absoluten wert gerechnet um später den Wert
time_diff = np.abs(time[1] - time[0])
# Die zweite Spalte der .csv Datei wird Fouriertransformiert
data_array_transformed = np.fft.fft(data[:, 1])
# Die Fouriertransformierte Frequenz wird absolutiert, so dass kein negativer Wert mehr vorzufinden ist
data_array_spectrum = np.abs(data_array_transformed)
# Formel um die Anzahl der Schwingungen in die Freuquenz umzurechnen - f = n / (M * Δt)
freq_spectrum = range(0, 2500, 1) / (time_diff * 2500)

# Darstellung des Amplitudenspektrums
plt.plot(freq_spectrum, data_array_spectrum)
plt.grid()
plt.xlabel('frequency')
plt.ylabel('amplitude')
plt.xlim(0, 20000)
plt.show()

file = open("data/eins.csv")
signallaenge = len(file.readlines())
abtastintervall = round((time_diff * 1000000), 2)

# Berechnung der größten Amplitude
print("Maximalster Amplitudenausschlag", round((np.max(freq_spectrum) / 100), 1))
print("Frequenz mit der größten Amplitude", np.max(data_array_spectrum))
print("Abtastintervall ∆t:", abtastintervall, "μs")
print("Signallänge M: ", signallaenge)
print("Grundperiode:", (abtastintervall * signallaenge)/1000, "ms")
