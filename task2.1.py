import numpy as np
import cv2

# ------------------------------ Aufgabe2.2 ------------------------------ #

vec = np.zeros((10, 3079000))
anzahl = 0
mean = 0

vec1 = np.zeros((480, 640))
vec2 = np.zeros((480, 640))
vec3 = np.zeros((480, 640))
vec4 = np.zeros((480, 640))
vec5 = np.zeros((480, 640))
vec6 = np.zeros((480, 640))
vec7 = np.zeros((480, 640))
vec8 = np.zeros((480, 640))
vec9 = np.zeros((480, 640))
vec10 = np.zeros((480, 640))

average = np.zeros((480, 640))

blackpic = ["black1", "black2", "black3", "black4", "black5", "black6", "black7", "black8", "black9", "black10"]
vector = [vec1, vec2, vec3, vec4, vec5, vec6, vec7, vec8, vec9, vec10]

for x in range(0, 10):
    blackpic[x] = cv2.imread('data/' + blackpic[x] + '.png')
    blackpic[x] = cv2.cvtColor(blackpic[x], cv2.COLOR_BGR2GRAY)

    print("Datei: " + str(x + 1) + ".png erfolgreich")
    for y in range(0, 480):
        for z in range(0, 640):
            b = blackpic[x][y, z]
            vector[x][y, z] = b
            anzahl += 1
    print("-----------------------------------")

for y in range(0, 480):
    for z in range(0, 640):
        mean = 0
        for file in range(0, 10):
            mean += vector[file][y, z]
        mean = float(mean / 10)
        average[y, z] = mean

image = cv2.imread("data/whited.png")
for x in range(0, 480):
    for y in range(0, 640):
        image[x, y] = average[x, y]

cv2.imwrite("data/blackaverage.png", image)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()