import numpy as np
import cv2

image = cv2.imread('data/Versuch1.png')

y = 0
x = 0
h = 480
w = 105
crop1 = image[y:y + h, x:x + w]
cv2.imshow('Crop1', crop1)
cv2.imwrite("data/bild1.png", crop1)

y = 0
x = 111
h = 480
w = 135
crop2 = image[y:y + h, x:x + w]
cv2.imshow('Crop2', crop2)
cv2.imwrite("data/bild2.png", crop2)

y = 0
x = 249
h = 480
w = 137
crop3 = image[y:y + h, x:x + w]
cv2.imshow('Crop3', crop3)
cv2.imwrite("data/bild3.png", crop3)

y = 0
x = 389
h = 480
w = 132
crop4 = image[y:y + h, x:x + w]
cv2.imshow('Crop4', crop4)
cv2.imwrite("data/bild4.png", crop4)

y = 0
x = 527
h = 480
w = 113
crop5 = image[y:y + h, x:x + w]
cv2.imshow('Crop5', crop5)
cv2.imwrite("data/bild5.png", crop5)

cv2.waitKey(0)
