from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

# Einlesen der .csv Datei

num = ["hoch1", "hoch2", "hoch3", "hoch4", "hoch5", "tief1", "tief2", "tief3", "tief4", "tief5", "links1", "links2",
       "links3", "links4", "links5", "rechts1", "rechts2", "rechts3", "rechts4", "rechts5"]
anderer = ["ahoch1", "ahoch2", "ahoch3", "ahoch4", "ahoch5", "atief1", "atief2", "atief3", "atief4", "atief5", "alinks1", "alinks2",
        "alinks3", "alinks4", "alinks5", "arechts1", "arechts2", "arechts3", "arechts4", "arechts5"]
moi = ["mhoch1", "mhoch2", "mhoch3", "mhoch4", "mhoch5", "mtief1", "mtief2", "mtief3", "mtief4", "mtief5", "mlinks1", "mlinks2",
        "mlinks3", "mlinks4", "mlinks5", "mrechts1", "mrechts2", "mrechts3", "mrechts4", "arechts5"]
capital = ["hoch", "tief", "links", "rechts"]
capital2 = ["hoch", "tief", "links", "rechts"]

gaussianwindow = signal.windows.gaussian(512, std=4)

for a in range(0, 20):
    data = np.load('data/' + str(num[a]) + '.npy')
    data2 = np.load('data/' + str(anderer[a]) + '.npy')
    data3 = np.load('data/' + str(moi[a]) + '.npy')
    num[a] = np.zeros((171, 512))
    moi[a] = np.zeros((171, 512))
    anderer[a] = np.zeros((171, 512))
    z = 256

    for y in range(0, 171):
        z = z - 256
        for x in range(0, 512):
            num[a][y, x] = np.mean(np.abs(np.fft.fft(data[z] * gaussianwindow)))
            anderer[a][y, x] = np.mean(np.abs(np.fft.fft(data2[z] * gaussianwindow)))
            moi[a][y, x] = np.mean(np.abs(np.fft.fft(data3[z] * gaussianwindow)))
            z = z + 1

    for y in range(0, 171):
        for x in range(0, 512):
            num[a][y, x] = num[a][y, x] * gaussianwindow[x]
            anderer[a][y, x] = anderer[a][y, x] * gaussianwindow[x]
            moi[a][y, x] = moi[a][y, x] * gaussianwindow[x]
        num[a][y] = np.abs(np.fft.fft(num[a][y]))
        anderer[a][y] = np.abs(np.fft.fft(anderer[a][y]))
        moi[a][y] = np.abs(np.fft.fft(moi[a][y]))
        num[a][y] = np.mean(num[a][y])
        anderer[a][y] = np.mean(anderer[a][y])
        moi[a][y] = np.mean(moi[a][y])

for z in range(0, 4):
    capital[z] = np.zeros((171, 512))
    for y in range(0, 171):
        for x in range(0, 512):
            if (z == 0):
                capital[z][y, x] = (num[0][y, x] + num[1][y, x] + num[2][y, x] + num[3][y, x] + num[4][y, x]) / 4
            elif (z == 1):
                capital[z][y, x] = (num[5][y, x] + num[6][y, x] + num[7][y, x] + num[8][y, x] + num[9][y, x]) / 4
            elif (z == 2):
                capital[z][y, x] = (num[10][y, x] + num[11][y, x] + num[12][y, x] + num[13][y, x] + num[14][y, x]) / 4
            elif (z == 3):
                capital[z][y, x] = (num[15][y, x] + num[16][y, x] + num[17][y, x] + num[18][y, x] + num[19][y, x]) / 4
    capital[z] = capital[z].ravel()

for x in range(0, 20):
    num[x] = num[x].ravel()
    moi[x] = moi[x].ravel()
    anderer[x] = anderer[x].ravel()

r, p = scipy.stats.pearsonr(num[0], capital[0])
print("r:", r, "p:", p)

r, p = scipy.stats.pearsonr(moi[0], capital[0])
print("r:", r, "p:", p)

r, p = scipy.stats.pearsonr(anderer[0], capital[0])
print("r:", r, "p:", p)
