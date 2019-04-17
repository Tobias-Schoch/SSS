import numpy as np
import cv2

# ------------------------------ Aufgabe3.1 ------------------------------ #

# Values for dark x & y
cir1 = 1000
cir2 = 1000
# Values for light  x & y
cir3 = 0
cir4 = 0
# actual pixelvalue
value = 0
# highscores
high1 = 1000
high4 = 0

# Bild einlesen
white1 = cv2.imread('data/white1.png', cv2.IMREAD_GRAYSCALE)
image = cv2.imread("data/zzz.png")

# for-Schleife um auf alle 307200 Pixel zuzugreifen
for x in range(0, 480):
    for y in range(0, 640):
        # den aktuellen Pixelwert in value speichern
        value = white1[x, y]
        # dunkelsten x Punkt mit aktuellem Wert überprüfen
        if (value < high1):
            cir1 = x
            cir2 = y
            # falls dunkler neuer Highscore
            high1 = value
        # hellsten x Punkt mit aktuellem Wert überprüfen
        if (value > high4):
            cir3 = x
            cir4 = y
            # falls heller neuer Highscore
            high4 = value

# Hellster und Dunkelster Pixel ausgeben
print("Der dunkelste Punkt liegt bei: " + str(cir1) + " " + str(cir2))
print("Der hellste Punkt liegt bei: " + str(cir3) + " " + str(cir4))

# Kreise bei den dunkelsten bzwh hellsten Pixeln zu machen
cv2.circle(image, (cir2, cir1), 5, (142, 123, 228), 2)
cv2.circle(image, (cir4, cir3), 5, (46, 179, 66), 2)

# Bild anzeigen und exportieren
cv2.imshow('image', image)
cv2.imwrite("zzz.png", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
