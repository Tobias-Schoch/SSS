import numpy as np
import cv2

# -------- Aufgabe3.4 -------- #

# Vector um Grenz- und Breitenwert zu speichern
vec = np.zeros((5, 2))
crop = ["crop1", "crop2", "crop3", "crop4", "crop5"]

# Bild einlesen und in Schwarz - Weiß umwandeln
image = cv2.imread('data/korrigiertes_bild2.png', cv2.IMREAD_GRAYSCALE)

# Grenz- und Breitenwerte für Bild 1
vec[0, 0] = 0
vec[0, 1] = 105
# Grenz- und Breitenwerte für Bild 2
vec[1, 0] = 111
vec[1, 1] = 135
# Grenz- und Breitenwerte für Bild 3
vec[2, 0] = 249
vec[2, 1] = 137
# Grenz- und Breitenwerte für Bild 4
vec[3, 0] = 389
vec[3, 1] = 132
# Grenz- und Breitenwerte für Bild 5
vec[4, 0] = 529
vec[4, 1] = 111

# Auf alle 5 Dateien zugreifen
for z in range(1, 6):

    # Ab welchem Pixel in der Höhe y soll begonnen werden
    y = 0
    # Ab welchem Pixel in der Breite x soll begonnen werden
    x = int(vec[z-1, 0])
    # Wie tief soll der Pixel gehen in h
    h = 480
    # Wie breit soll der Pixel gehen in w
    w = int(vec[z-1, 1])

    # Schneiden des Bildes mit den Variablen von oben
    crop[z - 1] = image[y:y + h, x:x + w]
    # geschnittene Bilder anzeigen
    cv2.imshow("Crop" + str(z), crop[z - 1])
    # geschnittene Bilder exportieren
    cv2.imwrite("korrigiert" + str(z) + ".png", crop[z-1])

cv2.waitKey(0)
