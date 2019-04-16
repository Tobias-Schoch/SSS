import numpy as np
import cv2
import matplotlib

# ------------------------------ Aufgabe1.3 ------------------------------ #
vec1 = np.zeros((5, 3))
vec2 = np.zeros((5, 5))
ten = -1

print("\hline")
print("Stufe & Mittelwert & Hex-Value & Standartabweichung \\\\")

for x in range(1, 6):
    image = cv2.imread("data/bild" + str(x) + ".png")
    ten += 1

    b, g, r, a = cv2.mean(image)
    b1 = b / 1000
    g1 = g / 1000
    r1 = r / 1000
    hex = matplotlib.colors.to_hex([b1, g1, r1])

    vec2[ten, 0] = x
    vec2[ten, 1] = b
    vec2[ten, 2] = g
    vec2[ten, 3] = r
    vec2[ten, 4] = np.std(image)

    print("\hline")
    print("Stufe " + str(x) + " & " + str(vec2[ten, 1]) + " & " + str(vec2[ten, 2]) + " & " + str(vec2[ten, 3]) + " & " + hex + " & " + str(vec2[ten, 4]) + " \\\\")

print("\hline")

