import numpy as np
import cv2

image = cv2.imread('data/Versuch1.png')

for x in range(1, 6):
    if x == 1:
        y = 0
        x = 0
        h = 480
        w = 105
        crop = image[y:y + h, x:x + w]
        cv2.imshow('Crop1', crop)
    if x == 2:
        y = 0
        x = 102
        h = 480
        w = 138
        crop2 = image[y:y + h, x:x + w]
        cv2.imshow('Crop2', crop2)
    if x == 3:
        y = 0
        x = 248
        h = 480
        w = 132
        crop3 = image[y:y + h, x:x + w]
        cv2.imshow('Crop3', crop3)
    if x == 4:
        y = 0
        x = 389
        h = 480
        w = 131
        crop4 = image[y:y + h, x:x + w]
        cv2.imshow('Crop4', crop4)
    if x == 5:
        y = 0
        x = 521
        h = 480
        w = 119
        crop5 = image[y:y + h, x:x + w]
        cv2.imshow('Crop5', crop5)

cv2.waitKey(0)
