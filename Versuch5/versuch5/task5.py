import redlab as rl
from time import sleep

import numpy as np
import matplotlib.pyplot as plt

print("-------einzelneWerte-------------------------")
print("16BitValue:" + str(rl.cbAIn(0, 0, 1)))
print("VoltageValue:" + str(rl.cbVIn(0, 0, 1)))
print("-------Messreihe-------------------------")
print("Messreihe:" + str(rl.cbAInScan(0, 0, 0, 300, 8000, 1)))
print("Messreihe:" + str(rl.cbVInScan(0, 0, 0, 300, 8000, 1)))
print("Samplerate:" + str(rl.cbInScanRate(0, 0, 0, 8000)))
print("Nyquist:" + str(rl.cbInScanRate(0, 0, 0, 8000) / 2))
print("-------Ausgabe-------------------------")

sin = [np.sin(2 * np.pi * 2 * (i / 30)) for i in range(0, 30)]

vec = np.zeros((8000))
data = rl.cbVInScan(0, 0, 0, 300, 8000, 1)
plt.plot(data)
plt.show()
