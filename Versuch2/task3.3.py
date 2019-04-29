import numpy as np
import cv2

# -------- Aufgabe3.3 -------- #

# Vektor zum Speichern des korrigierten Bildes
korrigiertes_bild = np.zeros((480, 640))

# Bild einlesen und evtl in Schwarz Weiß einlesen
grey = cv2.imread('data/Versuch1a.png', cv2.IMREAD_GRAYSCALE)
blackavg = cv2.imread('data/blackaverage.png')
whiteaverage = cv2.imread('data/whiteaverage.png')
whiteminusblack = cv2.imread('data/whiteminusblack.png')

# for-Schleife um auf alle 307200 Pixel zuzugreifen
for y in range(0, 480):
    for z in range(0, 640):
        # (Weiß-Schwarz) - avg(Weiß-Schwarz)
        r, g, b = whiteaverage[y, z] - np.mean(whiteaverage)
        # Grau-Werte berechnen
        r1 = grey[y, z]
        r2, g2, b2 = blackavg[y, z]
        # Weiß - Schwarz
        korrigiertes_bild[y, z] = int(r1) - int(r2)
        # / ((Weiß-Schwarz) - avg(Weiß-Schwarz))
        korrigiertes_bild[y, z] /= r

# Bild einlesen als Grundlage
image = cv2.imread("data/korrigiertes_bild.png")
# for-Schleife um auf alle 307200 Pixel zuzugreifen
for x in range(0, 480):
    for y in range(0, 640):
        # neue Pixel überschreiben von weiß - schwarz einfügen
        image[x, y] = korrigiertes_bild[x, y]

# Bild exportieren und anzeigen
cv2.imwrite("data/korrigiertes_bild2.png", image)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
