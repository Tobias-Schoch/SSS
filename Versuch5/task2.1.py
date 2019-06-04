# -------------------------------------
# Task 2.1
# -------------------------------------

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

# Definieren der Dateinamen
num = ["hoch1", "hoch2", "hoch3", "hoch4", "hoch5", "tief1", "tief2", "tief3", "tief4", "tief5", "links1",
       "links2", "links3", "links4", "links5", "rechts1", "rechts2", "rechts3", "rechts4", "rechts5"]
num2 = ["ahoch1", "ahoch2", "ahoch3", "ahoch4", "ahoch5", "atief1", "atief2", "atief3", "atief4", "atief5",
        "alinks1", "alinks2", "alinks3", "alinks4", "alinks5", "arechts1", "arechts2", "arechts3", "arechts4",
        "arechts5"]
numm = ["hoch1", "hoch2", "hoch3", "hoch4", "hoch5", "tief1", "tief2", "tief3", "tief4", "tief5", "links1",
        "links2", "links3", "links4", "links5", "rechts1", "rechts2", "rechts3", "rechts4", "rechts5"]
nummm = ["hoch1", "hoch2", "hoch3", "hoch4", "hoch5", "tief1", "tief2", "tief3", "tief4", "tief5", "links1",
         "links2", "links3", "links4", "links5", "rechts1", "rechts2", "rechts3", "rechts4", "rechts5"]
capital = ["hoch", "tief", "links", "rechts"]
capital2 = ["hoch", "tief", "links", "rechts"]
capital3 = ["hoch", "tief", "links", "rechts"]

# Gaußfenster definieren mit Fensterbreite Standardabweichung 4
gaussianwindow = signal.windows.gaussian(512, std=4)

# Darstellung des Gaußfensters
# plt.plot(gaussianwindow)
# plt.grid(True)
# plt.xlabel('Samples')
# plt.ylabel('Amplitude')
# plt.savefig('data/img/gauss.png')
# plt.show()

# For loop um alle Dateien zu analysieren
for a in range(0, 20):
    # Einlesen der Numpy Dateien von Person 1 & 2
    data = np.load('data/' + str(num[a]) + '.npy')
    data2 = np.load('data/' + str(num2[a]) + '.npy')
    # Definieren eines leeren Vectors für Person 1 & 2
    num[a] = np.zeros((171, 512))
    num2[a] = np.zeros((171, 512))
    z = 256

    # For loop um die einzelnen Windows zu erstellen
    for y in range(0, 171):
        z = z - 256
        # For loop um die einzelnen Frames zu berechnen
        for x in range(0, 512):
            # Signale * Gaußfenster, das wiederrum wird absolut fouriertransformiert.
            # Daraus der Durchschnitt ergibt den Windowingwert
            num[a][y, x] = np.mean(np.abs(np.fft.fft(data[z] * gaussianwindow)))
            num2[a][y, x] = np.mean(np.abs(np.fft.fft(data2[z] * gaussianwindow)))
            z = z + 1
        # plt.plot(num[a][y])
        # plt.title('Windownr' + str(y+1+(a*171)))
        # plt.xlabel('Signalnr.')
        # plt.ylabel('Frequenz')
        # plt.grid(True)
        # plt.savefig('data/img/' + str(y+1+(a*171)) + '.png')
        # plt.show()

    # For loop um die einzelnen Windows zu erstellen
    for y in range(0, 171):
        # For loop um die einzelnen Frames zu berechnen
        for x in range(0, 512):
            # Signale * Gaußfenster, das wiederrum wird absolut fouriertransformiert.
            # Daraus der Durchschnitt ergibt den Windowingwert
            num[a][y, x] = num[a][y, x] * gaussianwindow[x]
            num2[a][y, x] = num2[a][y, x] * gaussianwindow[x]
        num[a][y] = np.abs(np.fft.fft(num[a][y]))
        num2[a][y] = np.abs(np.fft.fft(num2[a][y]))
        num[a][y] = np.mean(num[a][y])
        num2[a][y] = np.mean(num2[a][y])

    # plt.plot(num[a], 'r')  # Plot zur Darstellung der Mittelung der Windows
    # plt.title(str(nummm[a]))
    # plt.grid(True)
    # plt.xlabel('Window')
    # plt.ylabel('Amplitude')
    # plt.savefig('data/img/' + numm[a] + 'AlleRichtig.png')
    # plt.show()

# For loop zur Ausgabe der endgültig berechneten Plots
for z in range(0, 4):
    # Vektoren zum Speichern der Plots
    capital[z] = np.zeros((171, 512))
    capital2[z] = np.zeros((171, 512))
    # For loop für die einzelnen Windows
    for y in range(0, 171):
        # For loop für die einzelnen Samples
        for x in range(0, 512):
            # Hoch Mittelung
            if (z == 0):
                capital[z][y, x] = (num[0][y, x] + num[1][y, x] + num[2][y, x] + num[3][y, x]
                                    + num[4][y, x]) / 5
                capital2[z][y, x] = (num2[0][y, x] + num2[1][y, x] + num2[2][y, x]
                                     + num2[3][y, x] + num2[4][y, x]) / 5
            # Tief Mittelung
            elif (z == 1):
                capital[z][y, x] = (num[5][y, x] + num[6][y, x] + num[7][y, x] + num[8][y, x]
                                    + num[9][y, x]) / 5
                capital2[z][y, x] = (num2[5][y, x] + num2[6][y, x] + num2[7][y, x] + num2[8][y, x]
                                     + num2[9][y, x]) / 5
            # Links Mittelung
            elif (z == 2):
                capital[z][y, x] = (num[10][y, x] + num[11][y, x] + num[12][y, x] + num[13][y, x]
                                    + num[14][y, x]) / 5
                capital2[z][y, x] = (num2[10][y, x] + num2[11][y, x] + num2[12][y, x] + num2[13][y, x]
                                     + num2[14][y, x]) / 5
            # Rechts Mittelung
            elif (z == 3):
                capital[z][y, x] = (num[15][y, x] + num[16][y, x] + num[17][y, x] + num[18][y, x]
                                    + num[19][y, x]) / 5
                capital2[z][y, x] = (num2[15][y, x] + num2[16][y, x] + num2[17][y, x] + num2[18][y, x]
                                     + num2[19][y, x]) / 5
    plt.plot(capital[z], 'r')  # Geplotete Endwerte
    plt.grid(True)
    plt.xlabel('Window')
    plt.ylabel('Amplitude')
    plt.savefig('data/img/Average' + capital3[z] + '.png')
    plt.show()
