import numpy as np
import cv2

# ------------------------------ Aufgabe2.1 ------------------------------ #

vec = np.zeros((10, 3079000))
anzahl = 0
mean = 0
average = np.zeros((1, 3079000))

whitepic = ["white1", "white2", "white3", "white4", "white5", "white6", "white7", "white8", "white9", "white10"]

for x in range(0, 10):
    whitepic[x] = cv2.imread('data/' + whitepic[x] + '.png')
    whitepic[x] = cv2.cvtColor(whitepic[x], cv2.COLOR_BGR2GRAY)

    print("Datei: " + str(x + 1) + ".png erfolgreich")
    for y in range(0, 480):
        for z in range(0, 640):
            b = whitepic[x][y, z]
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
