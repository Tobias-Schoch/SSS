import numpy as np
import cv2

# ------------------------------ Aufgabe2.1 ------------------------------ #

vec = np.zeros((10, 307200))
pixel = 0, 0, 0
anzahl = 0

whitepic = ["white1", "white2", "white3", "white4", "white5", "white6", "white7", "white8", "white9", "white10"]

for x in range(0, 10):
    whitepic[x] = cv2.imread('data/' + whitepic[x] + '.png')
    whitepic[x] = cv2.cvtColor(whitepic[x], cv2.COLOR_BGR2GRAY)

    for y in range(0, 640):
        for z in range(0, 480):
            b = float(whitepic[x][y, z])
            print(b)
            vec[x, anzahl] = b
            anzahl += 1


