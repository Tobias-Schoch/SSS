import numpy as np
import cv2
import matplotlib

# ------------------------------ Aufgabe1.3 ------------------------------ #
vec1 = np.zeros((5, 3))
vec2 = np.zeros((5, 4))
ten = -1

print("\hline")
print("Stufe & Mittelwert & Hex-Value & Standartabweichung \\\\")

for x in range(1, 6):
    image = cv2.imread("data/korrigiert" + str(x) + ".png")
    ten += 1

    b, g, r, a = cv2.mean(image)
    b1 = b / 1000
    g1 = g / 1000
    r1 = r / 1000
    hex = matplotlib.colors.to_hex([b1, g1, r1])

    vec2[ten, 0] = x
    vec2[ten, 1] = (b + g + r) / 3
    vec2[ten, 2] = np.std(image)

    print("\hline")
    print("Stufe " + str(x) + " & " + str(vec2[ten, 1]) + " & " + hex + " & " + str(vec2[ten, 2]) + " \\\\")

print("\hline")
