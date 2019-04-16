import numpy as np
import cv2

# ------------------------------ Aufgabe2.2 ------------------------------ #

korrigiertes_bild = np.zeros((480, 640))

grey = cv2.imread('data/Versuch1a.png')
image = cv2.cvtColor(grey, cv2.COLOR_BGR2GRAY)
blackavg = cv2.imread('data/blackaverage.png')


for y in range(0, 480):
    for z in range(0, 640):
        r1, g1, b1 = grey[y, z]
        r2, g2, b2 = blackavg[y, z]
        korrigiertes_bild[y, z] = int(r1) - int(r2)

image = cv2.imread("data/korrigiertes_bild2.png")
for x in range(0, 480):
    for y in range(0, 640):
        image[x, y] = korrigiertes_bild[x, y]

cv2.imwrite("data/korrigiertes_bild2.png", image)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
