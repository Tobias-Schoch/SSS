import matplotlib.pyplot as plt
import numpy as np

# Einlesen der .csv Datei
data = np.genfromtxt('data/eins.csv', delimiter=',', skip_header=0, skip_footer=0)

t = data[:, 0]
x = [2500, 5000, 7500, 10000]
f = 13 * np.sin(2 * np.pi * x[0] * t) + 3 * np.sin(2 * np.pi * x[1] * t) + 4 * np.sin(
    2 * np.pi * x[2] * t) + 1 * np.sin(2 * np.pi * x[3] * t)

time = data[:2, 0]
time_diff = np.abs(time[1] - time[0])
data_array_transformed = np.fft.fft(data[:, 1])
data_array_spectrum = np.abs(data_array_transformed)

f_transformed = np.fft.fft(f)
f_spectrum = np.abs(f_transformed)

N_f = len(f_transformed) / 2 + 1
freq_spectrum = range(0, 2500, 1) / (time_diff * 2500)


plt.plot(freq_spectrum, data_array_spectrum)
plt.grid()
plt.xlabel('frequency')
plt.ylabel('amplitude')
plt.xlim(0, 20000)
plt.show()

plt.plot(freq_spectrum, f_spectrum / N_f)
plt.grid()
plt.xlabel('frequency')
plt.ylabel('amplitude')
plt.xlim(0, 20000)
plt.show()