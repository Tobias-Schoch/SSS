import numpy as np
import cv2

# ------------------------------ Aufgabe3.1 ------------------------------ #

# Vectoren für die 10 Weißbildern
vec1 = np.zeros((480, 640))
vec2 = np.zeros((480, 640))
vec3 = np.zeros((480, 640))
vec4 = np.zeros((480, 640))
vec5 = np.zeros((480, 640))
vec6 = np.zeros((480, 640))
vec7 = np.zeros((480, 640))
vec8 = np.zeros((480, 640))
vec9 = np.zeros((480, 640))
vec10 = np.zeros((480, 640))
# Vector für das Durchschnittsbild
average = np.zeros((480, 640))

# String für die einzelnen Dateinamen
whitepic = ["white1", "white2", "white3", "white4", "white5", "white6", "white7", "white8", "white9", "white10"]
# Vektornamen in einem Vektor
vector = [vec1, vec2, vec3, vec4, vec5, vec6, vec7, vec8, vec9, vec10]

# for-Schleife um auf alle 10 Dateien zuzugreifen
for x in range(0, 10):
    # Weißbilder einlesen
    whitepic[x] = cv2.imread('data/' + whitepic[x] + '.png', cv2.IMREAD_GRAYSCALE)

    # for-Schleife um auf alle 307200 Pixel zuzugreifen
    for y in range(0, 480):
        for z in range(0, 640):
            # Vektoren der Dateien füllen mit den Bildpixelvalues
            vector[x][y, z] = whitepic[x][y, z]

# for-Schleife um auf alle 307200 Pixel zuzugreifen
for y in range(0, 480):
    for z in range(0, 640):
        # Mean auf 0 zurück zu setzen
        mean = 0
        # for-Schleife um auf alle 10 Dateien zuzugreifen
        for file in range(0, 10):
            # Pixel aus allen Dateien welche auf der selben Stelle liegen addieren
            mean += vector[file][y, z]
        # Pixel nun durch die Anzahl der Dateien teilen um den Mittelwert des Pixels zu erlangen
        average[y, z] = float(mean / 10)

# Datei einlesen um sie zu überschreiben
image = cv2.imread("data/whiteaverage.png", 0)
# for-Schleife um auf alle 307200 Pixel zuzugreifen
for x in range(0, 480):
    for y in range(0, 640):
        # Bild erstellen mit den Mittelwert der Pixels
        image[x, y] = average[x, y]

# Bild exportieren
cv2.imwrite("data/whiteaverage.png", image)
# Bild anzeigen
cv2.imshow('image', image)

# Bild kontrastmaximiert darstellen
image_contrast = cv2.equalizeHist(image)

# kontrastmaximiertes Bild exportieren und anzeigen
cv2.imwrite("data/contrastwhiteaverage1.png", image_contrast)
cv2.imshow('image_contrast', image_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()
