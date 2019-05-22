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


