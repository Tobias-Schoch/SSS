import numpy as np
import cv2

# ------------------------------ Aufgabe3.2 ------------------------------ #

# Vektor um die Werte der Subtraktion zu speichern
white_minus_black = np.zeros((480, 640))

# Weiß und Schwarz einlesen
whiteavg = cv2.imread('data/whiteaverage.png')
blackavg = cv2.imread('data/blackaverage.png')

# for-Schleife um auf alle 307200 Pixel zuzugreifen
for y in range(0, 480):
    for z in range(0, 640):
        # Grau-Werte berechnen
        r1, g1, b1 = whiteavg[y, z]
        r2, g2, b2 = blackavg[y, z]
        # Weiß - Schwarz
        white_minus_black[y, z] = int(r1) - int(r2)

# Bild einlesen als Grundlage
image = cv2.imread("data/whiteminusblack.png")
# for-Schleife um auf alle 307200 Pixel zuzugreifen
for x in range(0, 480):
    for y in range(0, 640):
        # neue Pixel überschreiben von weiß - schwarz einfügen
        image[x, y] = white_minus_black[x, y]

# Bild exportieren und anzeigen
cv2.imwrite("data/whiteminusblack.png", image)
cv2.imshow('image', image)

# Bild kontrastmaximiert darstellen
image_contrast = cv2.equalizeHist(image)

# Bild exportieren und anzeigen
cv2.imwrite("data/contrastwhiteaverage2.png", image_contrast)
cv2.imshow('image_contrast', image_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()
