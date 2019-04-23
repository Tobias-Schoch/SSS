import numpy as np
import cv2

# -------- Aufgabe2.2 -------- #

# Vector für das Korrekturbild
korrigiertes_bild = np.zeros((480, 640))

# Bild des Grauwertkeils einlesen und in Schwarz-Weiß umwandeln
grey = cv2.imread('data/Versuch1a.png', cv2.IMREAD_GRAYSCALE)
# Bild des Pixelweisen Mittelwerts einlesen
blackavg = cv2.imread('data/blackaverage.png')

# for-Schleife um auf alle 307200 Pixel zuzugreifen
for y in range(0, 480):
    for z in range(0, 640):
        # Auf Grauwert des Pixels zugreifen des Grauwertkeils
        r1, g1, b1 = grey[y, z]
        # Auf Grauwert des Pixels zugreifen des Dunkelbildes
        r2, g2, b2 = blackavg[y, z]
        # Grauwertkeil - Dunkelbild
        korrigiertes_bild[y, z] = int(r1) - int(r2)

# Datei einlesen um sie zu überschreiben
image = cv2.imread("data/korrigiertes_bild.png")
# for-Schleife um auf alle 307200 Pixel zuzugreifen
for x in range(0, 480):
    for y in range(0, 640):
        # Bild erstellen mit den Mittelwert der Pixels
        image[x, y] = korrigiertes_bild[x, y]

# Bild exportieren und anzeigen
cv2.imwrite("data/korrigiertes_bild.png", image)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
