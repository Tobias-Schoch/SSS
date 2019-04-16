import numpy as np
import cv2

# ------------------------------ Aufgabe3.2 ------------------------------ #

white_minus_black = np.zeros((480, 640))

whiteavg = cv2.imread('data/whiteaverage.png')
blackavg = cv2.imread('data/blackaverage.png')




for y in range(0, 480):
    for z in range(0, 640):
        r1, g1, b1 = whiteavg[y, z]
        r2, g2, b2 = blackavg[y, z]
        white_minus_black[y, z] = int(r1) - int(r2)

image = cv2.imread("data/whiteminusblack.png")
for x in range(0, 480):
    for y in range(0, 640):
        image[x, y] = white_minus_black[x, y]

cv2.imwrite("data/whiteminusblack.png", image)
cv2.imshow('image', image)

# Convert to YUV
image_contrast = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
# Apply histogram equalization
image_contrast[:, :, 0] = cv2.equalizeHist(image_contrast[:, :, 0])
# Convert to RGB
image_contrast = cv2.cvtColor(image_contrast, cv2.COLOR_YUV2RGB)

cv2.imwrite("data/contrastwhiteaverage2.png", image_contrast)
cv2.imshow('image_contrast', image_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()
