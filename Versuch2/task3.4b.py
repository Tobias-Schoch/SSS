import numpy as np
import cv2
import matplotlib

# ------------------------------ Aufgabe1.3 ------------------------------ #

# Vektor zum speichern
vec2 = np.zeros((5, 4))

# LaTeX Table format
print("\hline")
print("Stufe & Mittelwert & Hex-Value & Standartabweichung \\\\")

# for-Schleife um jede der 5 Dateien zu erreichen
for x in range(1, 6):
    # einlesen der aufgeteilten Bilder
    image = cv2.imread("data/bild" + str(x) + ".png")

    # Durchschnitt des aufgeteilten Bildes bekommen
    b, g, r, a = cv2.mean(image)
    # bgr durch 1000 da die hexfunktion Werte zwischen 0 und 1 braucht
    b1 = b / 1000
    g1 = g / 1000
    r1 = r / 1000
    # Hex Wert berechnen
    hex = matplotlib.colors.to_hex([b1, g1, r1])

    # LaTeX Tabellenformat für jede Stufe
    print("\hline")
    print("Stufe " + str(x) + " & " + str((b + g + r) / 3) + " & " + str(hex) + " & " + str(np.std(image)) + " \\\\")

print("\hline")
