import numpy as np
import cv2
import matplotlib

# ------------------------------ Aufgabe1.3 ------------------------------ #

blackpic = ["black1", "black2", "black3", "black4", "black5", "black6", "black7", "black8", "black9", "black10"]

for x in range(0, 10):
    blackpic[x] = cv2.imread('data/' + blackpic[x] + '.png')


