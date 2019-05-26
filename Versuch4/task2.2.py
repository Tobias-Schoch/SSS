# -------------------------------------
# Task 2.2
# -------------------------------------

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

# Definieren der Dateinamen
num = ["hoch1", "hoch2", "hoch3", "hoch4", "hoch5", "tief1", "tief2", "tief3", "tief4", "tief5", "links1",
       "links2", "links3", "links4", "links5", "rechts1", "rechts2", "rechts3", "rechts4", "rechts5"]
numm = ["hoch1", "hoch2", "hoch3", "hoch4", "hoch5", "tief1", "tief2", "tief3", "tief4", "tief5", "links1",
        "links2", "links3", "links4", "links5", "rechts1", "rechts2", "rechts3", "rechts4", "rechts5"]
capital = ["hoch", "tief", "links", "rechts"]
capital2 = ["hoch", "tief", "links", "rechts"]

# Gaußfenster definieren mit Fensterbreite Standardabweichung 4
gaussianwindow = signal.windows.gaussian(512, std=4)

# For loop um alle Dateien zu analysieren
for a in range(0, 20):
    # Einlesen der Numpy Dateien von Person 1
    data = np.load('data/' + str(num[a]) + '.npy')
    # Definieren eines leeren Vectors für Person 1
    num[a] = np.zeros((171, 512))
    z = 256

    # For loop um die einzelnen Windows zu erstellen
    for y in range(0, 171):
        z = z - 256
        # For loop um die einzelnen Frames zu berechnen
        for x in range(0, 512):
            # Signale * Gaußfenster, das wiederrum wird absolut fouriertransformiert.
            # Daraus der Durchschnitt ergibt den Windowingwert
            num[a][y, x] = np.mean(np.abs(np.fft.fft(data[z] * gaussianwindow)))
            z = z + 1

    for y in range(0, 171): # For loop um die einzelnen Windows zu erstellen
        for x in range(0, 512): # For loop um die einzelnen Frames zu berechnen
            # Signale * Gaußfenster, das wiederrum wird absolut fouriertransformiert.
            # Daraus der Durchschnitt ergibt den Windowingwert
            num[a][y, x] = num[a][y, x] * gaussianwindow[x]
        num[a][y] = np.abs(np.fft.fft(num[a][y]))
        num[a][y] = np.mean(num[a][y])

# For loop zur Ausgabe der endgültig berechneten Plots
for z in range(0, 4):
    # Vektoren zum Speichern der Plots
    capital[z] = np.zeros((171, 512))
    for y in range(0, 171): # For loop für die einzelnen Windows
        for x in range(0, 512): # For loop für die einzelnen Samples
            # Hoch Mittelung
            if (z == 0):
                capital[z][y, x] = (num[0][y, x] + num[1][y, x] + num[2][y, x] + num[3][y, x]
                                    + num[4][y, x]) / 4
            # Tief Mittelung
            elif (z == 1):
                capital[z][y, x] = (num[5][y, x] + num[6][y, x] + num[7][y, x] + num[8][y, x]
                                    + num[9][y, x]) / 4
            # Links Mittelung
            elif (z == 2):
                capital[z][y, x] = (num[10][y, x] + num[11][y, x] + num[12][y, x] + num[13][y, x]
                                    + num[14][y, x]) / 4
            # Rechts Mittelung
            elif (z == 3):
                capital[z][y, x] = (num[15][y, x] + num[16][y, x] + num[17][y, x] + num[18][y, x]
                                    + num[19][y, x]) / 4
    capital[z] = capital[z].ravel()

# 2D Array in 1D Array für Bravais-Pearson Methode
for x in range(0, 20):
    num[x] = num[x].ravel()

# Korrelationskoeffizient berechnet
r, p = scipy.stats.pearsonr(num[0], num[0])
print("r:", r, "p:", p)
r, p = scipy.stats.pearsonr(num[0], capital[0])
print("r:", r, "p:", p)
r, p = scipy.stats.pearsonr(num[0], capital[0])
print("r:", r, "p:", p)