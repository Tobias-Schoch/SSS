from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

# Einlesen der .csv Datei

num = ["hoch1", "hoch2", "hoch3", "hoch4", "hoch5", "tief1", "tief2", "tief3", "tief4", "tief5", "links1",
       "links2", "links3", "links4", "links5", "rechts1", "rechts2", "rechts3", "rechts4", "rechts5"]
anderer = ["ahoch1", "ahoch2", "ahoch3", "ahoch4", "ahoch5", "atief1", "atief2", "atief3", "atief4", "atief5",
           "alinks1", "alinks2", "alinks3", "alinks4", "alinks5", "arechts1", "arechts2", "arechts3", "arechts4",
           "arechts5"]
moi = ["mhoch1", "mhoch2", "mhoch3", "mhoch4", "mhoch5", "mtief1", "mtief2", "mtief3", "mtief4", "mtief5",
       "mlinks1", "mlinks2", "mlinks3", "mlinks4", "mlinks5", "mrechts1", "mrechts2", "mrechts3", "mrechts4",
       "arechts5"]
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
                capital[z][y, x] = (num[0][y, x] + num[1][y, x] + num[2][y, x] + num[3][y, x]
                                    + num[4][y, x]) / 4
            elif (z == 1):
                capital[z][y, x] = (num[5][y, x] + num[6][y, x] + num[7][y, x] + num[8][y, x]
                                    + num[9][y, x]) / 4
            elif (z == 2):
                capital[z][y, x] = (num[10][y, x] + num[11][y, x] + num[12][y, x] + num[13][y, x]
                                    + num[14][y, x]) / 4
            elif (z == 3):
                capital[z][y, x] = (num[15][y, x] + num[16][y, x] + num[17][y, x] + num[18][y, x]
                                    + num[19][y, x]) / 4
    capital[z] = capital[z].ravel()

for x in range(0, 20):
    num[x] = num[x].ravel()
    moi[x] = moi[x].ravel()
    anderer[x] = anderer[x].ravel()


r1, p = scipy.stats.pearsonr(capital[0], moi[0])
print("capital-moi1 r:", r1, "p:", p)
r2, p = scipy.stats.pearsonr(capital[0], moi[1])
print("capital-moi2 r:", r2, "p:", p)
r3, p = scipy.stats.pearsonr(capital[0], moi[2])
print("capital-moi3 r:", r3, "p:", p)
r4, p = scipy.stats.pearsonr(capital[0], moi[3])
print("capital-moi4 r:", r4, "p:", p)
r5, p = scipy.stats.pearsonr(capital[0], moi[4])
print("capital-moi5 r:", r5, "p:", p)

s1, p = scipy.stats.pearsonr(capital[0], anderer[0])
print("capital-anderer1 r:", s1, "p:", p)
s2, p = scipy.stats.pearsonr(capital[0], anderer[1])
print("capital-anderer2 r:", s2, "p:", p)
s3, p = scipy.stats.pearsonr(capital[0], anderer[2])
print("capital-anderer3 r:", s3, "p:", p)
s4, p = scipy.stats.pearsonr(capital[0], anderer[3])
print("capital-anderer4 r:", s4, "p:", p)
s5, p = scipy.stats.pearsonr(capital[0], anderer[4])
print("capital-anderer5 r:", s5, "p:", p)

print()
r1 = (r1 + r2 + r3 + r4 + r5) / 5
print(r1)
s1 = (s1 + s2 + s3 + s4 + s5) / 5
print(s1)
print()
# ------------------------------------------------

r6, p = scipy.stats.pearsonr(capital[1], moi[5])
print("capital-moi1 r:", r6, "p:", p)
r7, p = scipy.stats.pearsonr(capital[1], moi[6])
print("capital-moi2 r:", r7, "p:", p)
r8, p = scipy.stats.pearsonr(capital[1], moi[7])
print("capital-moi3 r:", r8, "p:", p)
r9, p = scipy.stats.pearsonr(capital[1], moi[8])
print("capital-moi4 r:", r9, "p:", p)
r10, p = scipy.stats.pearsonr(capital[1], moi[9])
print("capital-moi5 r:", r10, "p:", p)

s6, p = scipy.stats.pearsonr(capital[1], anderer[5])
print("capital-anderer1 r:", s6, "p:", p)
s7, p = scipy.stats.pearsonr(capital[1], anderer[6])
print("capital-anderer2 r:", s7, "p:", p)
s8, p = scipy.stats.pearsonr(capital[1], anderer[7])
print("capital-anderer3 r:", s8, "p:", p)
s9, p = scipy.stats.pearsonr(capital[1], anderer[8])
print("capital-anderer4 r:", s9, "p:", p)
s10, p = scipy.stats.pearsonr(capital[1], anderer[9])
print("capital-anderer5 r:", s10, "p:", p)

print()
r1 = (r6 + r7 + r8 + r9 + r10) / 5
print(r1)
s1 = (s6 + s7 + s8 + s9 + s10) / 5
print(s1)
print()
# ------------------------------------------------

r11, p = scipy.stats.pearsonr(capital[2], moi[10])
print("capital-moi1 r:", r11, "p:", p)
r12, p = scipy.stats.pearsonr(capital[2], moi[11])
print("capital-moi2 r:", r12, "p:", p)
r13, p = scipy.stats.pearsonr(capital[2], moi[12])
print("capital-moi3 r:", r13, "p:", p)
r14, p = scipy.stats.pearsonr(capital[2], moi[13])
print("capital-moi4 r:", r14, "p:", p)
r15, p = scipy.stats.pearsonr(capital[2], moi[14])
print("capital-moi5 r:", r15, "p:", p)

s11, p = scipy.stats.pearsonr(capital[2], anderer[10])
print("capital-anderer1 r:", s11, "p:", p)
s12, p = scipy.stats.pearsonr(capital[2], anderer[11])
print("capital-anderer2 r:", s12, "p:", p)
s13, p = scipy.stats.pearsonr(capital[2], anderer[12])
print("capital-anderer3 r:", s13, "p:", p)
s14, p = scipy.stats.pearsonr(capital[2], anderer[13])
print("capital-anderer4 r:", s14, "p:", p)
s15, p = scipy.stats.pearsonr(capital[2], anderer[14])
print("capital-anderer5 r:", s15, "p:", p)

print()
r1 = (r11 + r12 + r13 + r14 + r15) / 5
print(r1)
s1 = (s11 + s12 + s13 + s14 + s15) / 5
print(s1)
print()
# ------------------------------------------------

r16, p = scipy.stats.pearsonr(capital[3], moi[15])
print("capital-moi1 r:", r16, "p:", p)
r17, p = scipy.stats.pearsonr(capital[3], moi[16])
print("capital-moi2 r:", r17, "p:", p)
r18, p = scipy.stats.pearsonr(capital[3], moi[17])
print("capital-moi3 r:", r18, "p:", p)
r19, p = scipy.stats.pearsonr(capital[3], moi[18])
print("capital-moi4 r:", r19, "p:", p)
r20, p = scipy.stats.pearsonr(capital[3], moi[19])
print("capital-moi5 r:", r20, "p:", p)

s16, p = scipy.stats.pearsonr(capital[3], anderer[15])
print("capital-anderer1 r:", s16, "p:", p)
s17, p = scipy.stats.pearsonr(capital[3], anderer[16])
print("capital-anderer2 r:", s17, "p:", p)
s18, p = scipy.stats.pearsonr(capital[3], anderer[17])
print("capital-anderer3 r:", s18, "p:", p)
s19, p = scipy.stats.pearsonr(capital[3], anderer[18])
print("capital-anderer4 r:", s19, "p:", p)
s20, p = scipy.stats.pearsonr(capital[3], anderer[19])
print("capital-anderer5 r:", s20, "p:", p)

print()
r1 = (r16 + r17 + r18 + r19 + r20) / 5
print(r1)
s1 = (s16 + s17 + s18 + s19 + s20) / 5
print(s1)
print()