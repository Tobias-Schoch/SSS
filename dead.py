import numpy as np
import cv2

# ------------------------------ Aufgabe3.1 ------------------------------ #

vec = np.zeros((10, 3079000))
anzahl = 0
cir1 = 1000
cir2 = 1000
cir3 = 0
cir4 = 0
value = 0
high1 = 1000
high4 = 0

vec1 = np.zeros((480, 640))

white1 = cv2.imread('data/white1.png')
white1 = cv2.cvtColor(white1, cv2.COLOR_BGR2GRAY)

print("Datei: white1.png erfolgreich")
b, g, r, a = cv2.mean(white1)
b = (b + g + r) / 3
value = np.std(white1)
print("-----------------------------------")

image = cv2.imread("data/zzz.png")
for x in range(0, 480):
    for y in range(0, 640):
        value = white1[x, y]
        if (value < 222 and value < high1):
            cir1 = x
            cir2 = y
            print(str(x) + " " + str(y))
        if(value > 244 and value > high4):
            cir3 = x
            cir4 = y
            print(str(x) + " " + str(y))

cv2.circle(image, (cir2, cir1), 5, (142, 123, 228), 2)
cv2.circle(image, (cir4, cir3), 5, (46, 179, 66), 2)

cv2.imshow('image',image)
cv2.imwrite("zzz.png", image)
cv2.waitKey(0)
cv2.destroyAllWindows()