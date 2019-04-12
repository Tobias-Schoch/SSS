import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math as m

#       Aufgabe2      #

ten = -1
data = 0
# Matrix gefüllt mit 0en 21 Zeilen, 2 Spalten
vec2 = np.zeros((21, 2))

# Abstandswerte in cm
rang = ["10", "13", "16", "19", "22", "25", "28", "31", "34", "37", "40", "43", "46", "49", "52", "55", "58", "61",
        "64", "67", "70"]

# For Schleife um die einzelnen Dateien einzulesen
for x in rang:
    # ten als Index
    ten += 1
    # data sind die Werte aus den .csv Dateien. Mit rang[ten] werden die einzelnen Abstandswerte aus rang abgerufen
    data = np.genfromtxt('data/' + str(rang[ten]) + '.csv', delimiter=",", skip_header=1000, skip_footer=499,
                         usecols=(4))

    # Stelle 0: Logarithmus des Abstandes in cm
    vec2[ten, 0] = np.log(int(rang[ten]))
    # Stelle 1: Logarithmus des Durchschnittes der Spannung in Volt
    vec2[ten, 1] = np.log(np.mean(data))

    # LaTeX Format für Tabellen um die Tabelle automatisch generieren zu lassen mittels der For Schleife
    print("\\hline")
    print(str(rang[ten]) + "cm & " + str(vec2[ten, 0]) + " & " + str(vec2[ten, 1]) + " \\\\")

# x-Werte des Graphen  zur Darstellung der Linearen Regression
x = np.array(
    [vec2[0, 0], vec2[1, 0], vec2[2, 0], vec2[3, 0], vec2[4, 0], vec2[5, 0], vec2[6, 0], vec2[7, 0], vec2[8, 0],
     vec2[9, 0], vec2[10, 0], vec2[11, 0], vec2[12, 0], vec2[13, 0], vec2[14, 0], vec2[15, 0], vec2[16, 0], vec2[17, 0],
     vec2[18, 0], vec2[19, 0], vec2[20, 0]])
# y-Werte des Graphen  zur Darstellung der Linearen Regression
y = np.array(
    [vec2[0, 1], vec2[1, 1], vec2[2, 1], vec2[3, 1], vec2[4, 1], vec2[5, 1], vec2[6, 1], vec2[7, 1], vec2[8, 1],
     vec2[9, 1], vec2[10, 1], vec2[11, 1], vec2[12, 1], vec2[13, 1], vec2[14, 1], vec2[15, 1], vec2[16, 1],
     vec2[17, 1], vec2[18, 1], vec2[19, 1], vec2[20, 1]])

# Funktion zur Generierung der Linearen Regression in Python
gradient, intercept, r_value, p_value, std_err = stats.linregress(x, y)
mn = np.min(x)
mx = np.max(x)
x1 = np.linspace(mn, mx, 500)
y1 = gradient * x1 + intercept

# Darstellung der Linearen Regression in einem Graphen
plt.plot(x, y, 'ob')
plt.plot(x1, y1, '-r')
plt.show()

# Darstellung der Logarithmierung von der avg Spannung und dem Abstand
plt.plot([vec2[0, 0], vec2[1, 0], vec2[2, 0], vec2[3, 0], vec2[4, 0], vec2[5, 0], vec2[6, 0], vec2[7, 0], vec2[8, 0],
          vec2[9, 0], vec2[10, 0], vec2[11, 0], vec2[12, 0], vec2[13, 0], vec2[14, 0], vec2[15, 0], vec2[16, 0],
          vec2[17, 0], vec2[18, 0], vec2[19, 0], vec2[20, 0]],
         [vec2[0, 1], vec2[1, 1], vec2[2, 1], vec2[3, 1], vec2[4, 1], vec2[5, 1], vec2[6, 1], vec2[7, 1], vec2[8, 1],
          vec2[9, 1], vec2[10, 1], vec2[11, 1], vec2[12, 1], vec2[13, 1], vec2[14, 1], vec2[15, 1], vec2[16, 1],
          vec2[17, 1], vec2[18, 1], vec2[19, 1], vec2[20, 1]], 'b')
plt.ylabel('logarithmierter Durchschnitt der Spannung in V')
plt.xlabel('logarithmierter Abstand in cm')
plt.show()

# Darstellung der Kennlinie in einem Graphen
plt.plot([vec2[0, 0], vec2[1, 0], vec2[2, 0], vec2[3, 0], vec2[4, 0], vec2[5, 0], vec2[6, 0], vec2[7, 0], vec2[8, 0],
          vec2[9, 0], vec2[10, 0], vec2[11, 0], vec2[12, 0], vec2[13, 0], vec2[14, 0], vec2[15, 0], vec2[16, 0],
          vec2[17, 0], vec2[18, 0], vec2[19, 0], vec2[20, 0]],
         [vec2[0, 0], vec2[1, 0], vec2[2, 0], vec2[3, 0], vec2[4, 0], vec2[5, 0], vec2[6, 0], vec2[7, 0], vec2[8, 0],
          vec2[9, 0], vec2[10, 0], vec2[11, 0], vec2[12, 0], vec2[13, 0], vec2[14, 0], vec2[15, 0], vec2[16, 0],
          vec2[17, 0], vec2[18, 0], vec2[19, 0], vec2[20, 0]], marker="o")
plt.ylabel('logarithmierter Abstand in cm')
plt.xlabel('logarithmierter Abstand in cm')
plt.show()
