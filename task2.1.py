import numpy as np
import cv2

# ------------------------------ Aufgabe2.2 ------------------------------ #

vec = np.zeros((10, 3079000))
anzahl = 0
mean = 0
average = np.zeros((1, 3079000))

blackpic = ["black1", "black2", "black3", "black4", "black5", "black6", "black7", "black8", "black9", "black10"]

for x in range(0, 10):
    blackpic[x] = cv2.imread('data/' + blackpic[x] + '.png')
    blackpic[x] = cv2.cvtColor(blackpic[x], cv2.COLOR_BGR2GRAY)

    print("Datei: " + str(x + 1) + ".png erfolgreich")
    for y in range(0, 480):
        for z in range(0, 640):
            b = blackpic[x][y, z]
            print(b)
            vec[x, anzahl] = b
            anzahl += 1
    print("-----------------------------------")

for pix in range(0, 307200):

    mean = 0
    for file in range(0, 10):
        mean += vec[file, pix]
    mean = float(mean / 10)
    average[0, pix] = mean
