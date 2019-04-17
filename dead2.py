import numpy as np
import cv2

# ------------------------------ Aufgabe3.1 ------------------------------ #

anzahl = 0
cir1 = 1000
cir2 = 1000
cir3 = 0
cir4 = 0
value = 0
high1 = 1000
high4 = 0

vec1 = np.zeros((480, 640))

white1 = cv2.imread('data/Versuch1b.png')
white1 = cv2.cvtColor(white1, cv2.COLOR_BGR2GRAY)
value = np.std(white1)

image = cv2.imread("data/zzz2.png")
for x in range(0, 480):
    for y in range(0, 640):
        value = white1[x, y]
        if (value < high1):
            cir1 = x
            cir2 = y
            high1 = value

        if (value > high4):
            cir3 = x
            cir4 = y
            high4 = value

print("Der dunkelste Punkt liegt bei: " + str(cir1) + " " + str(cir2))
print("Der hellste Punkt liegt bei: " + str(cir3) + " " + str(cir4))

cv2.circle(image, (cir2, cir1), 5, (142, 123, 228), 2)
cv2.circle(image, (cir4, cir3), 5, (46, 179, 66), 2)

cv2.imshow('image', image)
cv2.imwrite("zzz2.png", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
