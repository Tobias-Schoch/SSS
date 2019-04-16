import numpy as np
import cv2

image = cv2.imread('data/Versuch1.png')

for ()
y = 0
x = 0
h = 480
w = 105
crop = image[y:y + h, x:x + w]
cv2.imshow('Image', crop)
cv2.waitKey(0)
