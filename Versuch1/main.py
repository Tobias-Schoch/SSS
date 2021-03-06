import numpy as np
import matplotlib.pyplot as plt

#       Aufgabe1      #

ten = -1
data = 0
# Matrix gefüllt mit 0en 21 Zeilen, 3 Spalten
vec = np.zeros((21, 3))

# Abstandswerte in cm
rang = ["10", "13", "16", "19", "22", "25", "28", "31", "34", "37", "40", "43", "46", "49", "52", "55", "58", "61",
        "64", "67", "70"]

# Voltwerte für die entsprechenden Abstände
volt = ["1,34V", "1,15V", "1,05V", "0,935V", "0,838V", "0,775V", "0,696V", "0,657V", "0,617V", "0,580V",
        "0,560V", "0,519V", "0,499V", "0,479V", "0,457V", "0,434V", "0,412V", "0,395V", "0,374V", "0,395V",
        "0,374V"]

# For Schleife um die einzelnen Dateien einzulesen
for x in rang:
    # ten als Index
    ten += 1
    # data sind die Werte aus den .csv Dateien. Mit rang[ten] werden die einzelnen Abstandswerte aus rang abgerufen
    data = np.genfromtxt('data/' + str(rang[ten]) + '.csv', delimiter=",", skip_header=1000, skip_footer=499,
                         usecols=(4))

    # LaTeX Format für Tabellen um die Tabelle automatisch generieren zu lassen mittels der For Schleife
    print("\\hline")
    print(str(rang[ten]) + "cm & " + str(volt[ten]) + " & " + str(np.mean(data)) + " & " + str(np.std(data)) + " \\\\")

    # Stelle 0: Abstand in cm
    vec[ten, 0] = rang[ten]
    # Stelle 1: Durchschnitt der Spannung für einen bestimmten Abstand in cm
    vec[ten, 1] = np.mean(data)
    # Stelle 2: Standartabweichung der Spannung für einen bestimmten Abstand in cm
    vec[ten, 2] = np.std(data)

# Zeichnung des Graphen für den Durchschnitt der Spannung
plt.plot([10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70],
         [vec[0, 1], vec[1, 1], vec[2, 1], vec[3, 1], vec[4, 1], vec[5, 1], vec[6, 1], vec[7, 1], vec[8, 1], vec[9, 1],
          vec[10, 1], vec[11, 1], vec[12, 1], vec[13, 1], vec[14, 1], vec[15, 1], vec[16, 1], vec[17, 1], vec[18, 1],
          vec[19, 1], vec[20, 1]], 'b')
plt.ylabel('Durchschnitt der Spannung in V')
plt.xlabel('Abstand in cm')
plt.axis([0, 70, 0, 1.5])
plt.grid(True)
plt.show()

# Zeichnung des Graphen für die Standartabweichung der Spannung
plt.plot([10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70],
         [vec[0, 2], vec[1, 2], vec[2, 2], vec[3, 2], vec[4, 2], vec[5, 2], vec[6, 2], vec[7, 2], vec[8, 2], vec[9, 2],
          vec[10, 2], vec[11, 2], vec[12, 2], vec[13, 2], vec[14, 2], vec[15, 2], vec[16, 2], vec[17, 2], vec[18, 2],
          vec[19, 2], vec[20, 2]], 'r')
plt.ylabel('Standardabweichung der Spannung in V')
plt.xlabel('Abstand in cm')
plt.axis([0, 70, 0, 0.12])
plt.grid(True)
plt.show()
