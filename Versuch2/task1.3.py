import numpy as np
import cv2
import matplotlib
import matplotlib.pyplot as plt

# -------- Aufgabe1.3 -------- #

vec = np.zeros((10, 3))

# LaTeX Tabellenformat
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
    print("Stufe " + str(x) + " & " + str((b + g + r) / 3) + " & " + hex + " & " + str(np.std(image)) + " \\\\")

    vec[x-1, 0] = x
    vec[x-1, 1] = (b + g + r) / 3
    vec[x-1, 2] = np.std(image)

# Darstellung des Grauwerts in einem Graphen
plt.plot([vec[0, 0], vec[1, 0], vec[2, 0], vec[3, 0], vec[4, 0]],
         [vec[0, 1], vec[1, 1], vec[2, 1], vec[3, 1], vec[4, 1]], 'b')
plt.ylabel('Grauwert in RGB')
plt.xlabel('Grauwertkeil')
plt.grid(True)
plt.show()

# Darstellung der Standartabweichung in einem Graphen

plt.plot([vec[0, 0], vec[1, 0], vec[2, 0], vec[3, 0], vec[4, 0]],
         [vec[0, 2], vec[1, 2], vec[2, 2], vec[3, 2], vec[4, 2]], 'b')
plt.ylabel('Standartabweichung in RGB')
plt.xlabel('Grauwertkeil')
plt.grid(True)
plt.show()

print("\hline")
