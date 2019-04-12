import numpy as np

data = 0
data2 = 0
faktor2 = 1.96

# Berechnung von 29,7 cm Messfehler #

# data sind die Werte aus der (21cm) breiten DinA4 Seite in die .csv Datei gespeichert wurden.
data = np.genfromtxt('data/DinA4Breit.csv', delimiter=",", skip_header=1000, skip_footer=499,
                     usecols=(4))

# data2 sind die Werte aus der (29,7cm) langen DinA4 Seite in die .csv Datei gespeichert wurden.
data2 = np.genfromtxt('data/DinA4Lang.csv', delimiter=",", skip_header=1000, skip_footer=499,
                      usecols=(4))

#Standartabweichung und Average ausrechnen aufgrund der Gaußverteilung mit 2sx und 4sx
avglang = np.mean(data2)
stdlang = np.std(data2) / np.sqrt(1000)
avgbreit = np.mean(data)
stdbreit = np.std(data) / np.sqrt(1000)

print("x(68%) = " + str(avglang) + "V +" + "1 * " + str(stdlang) + "V * 2")
print("x(95%) = " + str(avglang) + "V +" + "1,96 * " + str(stdbreit) + "V * 4")
print("x(68%) = " + str(avgbreit) + "V +" + "1 * " + str(stdlang) + "V * 2")
print("x(95%) = " + str(avgbreit) + "V +" + "1,96 * " + str(stdbreit) + "V * 4")
print()

# Funktionen zur Berechnung
a1 = np.log(29.7) / np.log(np.mean(data2))
b1 = np.log(29.7) - (a1 * np.log(np.mean(data2)))
z1 = (np.exp(b1) * a1 * np.mean(data2) ** (a1 - 1))

# Gaußverteilung mit 68,26% und 95%
# Korrekturfaktor = 1,0 und 1,96
korrektur_lang = (np.mean(data2) + faktor2 * stdlang) - np.mean(data2)
deltaya68 = z1 * stdlang
deltaya95 = z1 * korrektur_lang

# e^b * x^a  -  Umkehrung der doppelten Logarithmierung
y1 = np.exp(b1) * np.power(np.mean(data2), a1)

# Ausgeben der errechneten Messkorrekturen für die jeweilige Gaußverteilung
print("y(68%) = " + str(round(y1, 2)) + " cm +-" + str(deltaya68 * -1) + " cm")
print("y(95%) = " + str(round(y1, 2)) + " cm +-" + str(deltaya95 * -1) + " cm")

# Berechnung von 21 cm Messfehler #
a2 = np.log(21) / np.log(np.mean(data))
b2 = np.log(21) - (a2 * np.log(np.mean(data)))
z2 = (np.exp(b2) * a2 * np.mean(data) ** (a2 - 1))

# Gaußverteilung mit 68,26% und 95%
# Korrekturfaktor = 1,0 und 1,96
korrektur_breit = (np.mean(data) + faktor2 * stdbreit) - np.mean(data)
deltayb68 = z2 * stdbreit
deltayb95 = z2 * korrektur_breit

# e^b * x^a  -  Umkehrung der doppelten Logarithmierung
y2 = np.exp(b2) * np.power(np.mean(data), a2)

# Errechnung des Flächeninhalts
flache = round(y2, 2) * round(y1, 2)
# Ausgeben der errechneten Messkorrekturen für die jeweilige Gaußverteilung
print("y(68%) = " + str(round(y2, 2)) + " cm +-" + str(deltayb68 * -1) + " cm")
print("y(95%) = " + str(round(y2, 2)) + " cm +-" + str(deltayb95 * -1) + " cm")
print()
print("Ein DinA4 Blatt hat ein Flächeninhalt von " + str(round(flache, 2)) + " cm^2")
print("68% hat bei einem Flächeninhalt von " + str(round(flache, 2)) + "cm^2 einen Messfehler von +" + str(
    (deltaya68 + deltayb68)) + "cm")
print("95% hat bei einem Flächeninhalt von " + str(round(flache, 2)) + "cm^2 einen Messfehler von +" + str(
    (deltaya95 + deltayb95)) + "cm")
