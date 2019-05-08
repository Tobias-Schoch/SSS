import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('data/Mundharmonika/eins.csv', delimiter=',', unpack=True)
data = np.loadtxt('data/Mundharmonika/eins.csv', delimiter=',', unpack=True)
data_fft = np.fft.fft(data[:,1])

plt.plot(x, y)
plt.figure()
plt.ylabel('Spannung in V')
plt.xlabel('Zeit t')
plt.show()

# Grundperiode:     1,586 ms
# Grundfrequenz:    630,52 Hz
# Signaldauer:      10 ms
# Abtastintervall:  4 μs
# Signallänge:      2500
# Abtastfrequenz:   4 MH
period = 1.586
frequence = 630.52
singaltime = 10
keyintervall = 4
signallength = 2499
keyfrequence = 4
step = 1
result = np.zeros((step,signallength+1))
amplitude = signallength * keyfrequence
i = 0

for x in range(1,signallength,1):
    i = i + 1
    print(i)
    print(y[x], "\n")

for x in range(step,signallength,step):
    result[0, x-1] = x / amplitude

#plt.plot(result, y)
#plt.figure()
#plt.ylabel('Spannung in V')
#plt.xlabel('Zeit t')
#plt.show()