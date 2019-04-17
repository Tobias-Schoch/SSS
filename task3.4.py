import numpy as np
import cv2

# ------------------------------ Aufgabe1.2 ------------------------------ #

vec = np.zeros((5, 4))
crop = ["crop1", "crop2", "crop3", "crop4", "crop5"]
ten = -1

image = cv2.imread('data/korrigiertes_bild2.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

vec[0, 0] = 0
vec[0, 1] = 480
vec[0, 2] = 105
vec[1, 0] = 111
vec[1, 1] = 480
vec[1, 2] = 135
vec[2, 0] = 249
vec[2, 1] = 480
vec[2, 2] = 137
vec[3, 0] = 389
vec[3, 1] = 480
vec[3, 2] = 132
vec[4, 0] = 529
vec[4, 1] = 480
vec[4, 2] = 111

for z in range(1, 6):
    ten += 1

    y = 0
    x = int(vec[ten, 0])
    h = int(vec[ten, 1])
    w = int(vec[ten, 2])

    crop[ten] = image[y:y + h, x:x + w]
    cv2.imshow("Crop" + str(z), crop[ten])
    cv2.imwrite("korrigiert" + str(z) + ".png", crop[ten])

cv2.waitKey(0)
