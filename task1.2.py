import numpy as np
import cv2

# ------------------------------ Aufgabe1.2 ------------------------------ #

vec = np.zeros((5, 4))
ten = -1

image = cv2.imread('data/Versuch1.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

vec[0, 0] = 0
vec[0, 1] = 0
vec[0, 2] = 480
vec[0, 3] = 105
vec[1, 0] = 0
vec[1, 1] = 111
vec[1, 2] = 480
vec[1, 3] = 135
vec[2, 0] = 0
vec[2, 1] = 249
vec[2, 2] = 480
vec[2, 3] = 137
vec[3, 0] = 0
vec[3, 1] = 389
vec[3, 2] = 480
vec[3, 3] = 132
vec[4, 0] = 0
vec[4, 1] = 527
vec[4, 2] = 480
vec[4, 3] = 113

for x in range(1, 6):
    ten += 1

    y = int(vec[ten, 0])
    x = int(vec[ten, 1])
    h = int(vec[ten, 2])
    w = int(vec[ten, 3])

    crop1 = image[y:y + h, x:x + w]
    cv2.imshow("Crop" + str(x), crop1)
    cv2.imwrite("data/bild" + str(x) + ".png", crop1)


cv2.waitKey(0)
