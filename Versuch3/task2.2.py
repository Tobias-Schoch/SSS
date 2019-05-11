import matplotlib.pyplot as plt
import numpy as np

# Array um die einzelnen .csv Dateien einzulesen des kleinen Lautsprechers
klein = ["klein100", "klein200", "klein300", "klein400", "klein500", "klein700", "klein850", "klein1000",
         "klein1200", "klein1500", "klein1700", "klein2000", "klein3000", "klein4000", "klein5000", "klein6000",
         "klein10000"]
# Array um die einzelnen .csv Dateien einzulesen des großen Lautsprechers
gross = ["gross100", "gross200", "gross300", "gross400", "gross500", "gross700", "gross850", "gross1000",
         "gross1200", "gross1500", "gross1700", "gross2000", "gross3000", "gross4000", "gross5000", "gross6000",
         "gross10000"]

# Die für jeweils den großen und den kleinen Lautsprecher gemessenen Zeiten
zeit = [100, 200, 300, 400, 500, 700, 850, 1000, 1200, 1500, 1700, 2000, 3000, 4000, 5000, 6000, 10000]
# Die für den kleinen Lautpsrecher von Hand berechneten Phasenverschiebungen in µs
kleinphase = [228, 295, 113.2, 105.2, 70.6, 64.8, 34, 4.2, 1.8, 12.2, 12.1, 14.7, 8.88, 11.60, 5.92, 6.92, 3.67]
# Die für den großen Lautpsrecher von Hand berechneten Phasenverschiebungen in µs
grossphase = [505, 82, 1, 10, 17, 12.4, 15.2, 14.8, 15.6, 12.8, 13.2, 14.4, 19.7, 12.52, 5.32, 3.32, 4.74]
# Die einzelnen Abtastintervalle für die einzelnen Frequenzen des großen Lautsprechers
grossintervall = [1, 1, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2, 0.2, 0.1, 0.1, 0.1, 0.04, 0.04, 0.04, 0.02, 0.01]
# Die einzelnen Abtastintervalle für die einzelnen Frequenzen des kleinen Lautsprechers
kleinintervall = [1, 1, 1, 1, 1, 0.4, 0.4, 0.4, 0.4, 0.2, 0.2, 0.2, 0.1, 0.04, 0.04, 0.04, 0.02]
# Ein Vektor in dem später für den kleinen Lautsprecher die Amplituden gespeichert werden
kleinamp = np.zeros(17)
# Ein Vektor in dem später für den großen Lautsprecher die Amplituden gespeichert werden
grossamp = np.zeros(17)

# For Schleife von 0-16 um die einzelnen .csv Dateien einzulesen und auszuwerten
for a in range(0, 17):
    # Einlesen der kleinen Dateien - dabei wird die linke Spalte als x und die rechte als y definiert
    x, y = np.loadtxt('data/' + klein[a] + '.csv', delimiter=',', unpack=True)
    # Einlesen der großen Dateien - dabei wird die linke Spalte als u und die rechte als v definiert
    u, v = np.loadtxt('data/' + gross[a] + '.csv', delimiter=',', unpack=True)

    # Berechnung für jede Datei des kleinen Lautsprechers den maximalen absoluten Amplitudenwert
    kleinamp[a] = np.max(np.abs(y))
    # Berechnung für jede Datei des großen Lautsprechers den maximalen absoluten Amplitudenwert
    grossamp[a] = np.max(np.abs(v))

# Darstellung der Amplitudenmaxima für beide Lautsprecher im Verhältnis zur Dateinr.
plt.plot(kleinamp, 'b')
plt.plot(grossamp, 'y')
plt.title("Amplitude")
plt.ylabel('Amplitude')
plt.xlabel('Versuchnr.')
plt.grid(True)
plt.savefig('amplitudeanzahl.png')
plt.show()

# Darstellung der Amplitudenmaxima für beide Lautsprecher im Verhältnis zur Frequenz
plt.plot(zeit, kleinamp, 'b')
plt.plot(zeit, grossamp, 'y')
plt.title("Amplitude")
plt.ylabel('Amplitude')
plt.xlabel('Frequenz f')
plt.grid(True)
plt.savefig('amplitudefrequenz.png')
plt.show()

# Darstellung des Phasengangs für beide Lautsprecher im Verhältnis zur Dateinr.
plt.plot(kleinphase, 'b')
plt.plot(grossphase, 'y')
plt.title("Phasengang")
plt.ylabel('Phasenverschiebung')
plt.xlabel('Versuchnr.')
plt.grid(True)
plt.savefig('phasenanzahl.png')
plt.show()

# Darstellung des Phasengangs für beide Lautsprecher im Verhältnis zur Frequenz
plt.plot(zeit, kleinphase, 'b')
plt.plot(zeit, grossphase, 'y')
plt.title("Phasenverschiebung")
plt.ylabel('Phasenverschiebung')
plt.xlabel('Frequenz f')
plt.grid(True)
plt.savefig('phasenfrequenz.png')
plt.show()

# for Schleife zum Berechnen des Bode Diagramms
for a in range(0, 17):
    # 20 log10 zur Berechnung des Bode-Diagramms für den großen Lautsprecher
    grossamp[a] = 1 / grossamp[a]
    grossamp[a] = 20 * np.log10(grossamp[a])
    # 20 log10 zur Berechnung des Bode-Diagramms für den großen Lautsprecher
    kleinamp[a] = 1 / kleinamp[a]
    kleinamp[a] = 20 * np.log10(kleinamp[a])
    # Berechnung des Phasenwinkels mit −∆t * f * 360 für den großen Lautsprecher
    grossphase[a] = (grossphase[a] * -1) * zeit[a] * 360
    # Berechnung des Phasenwinkels mit −∆t * f * 360 für den kleinen Lautsprecher
    kleinphase[a] = (kleinphase[a] * -1) * zeit[a] * 360

# Darstellung des Phasengangs für beide Lautsprecher im Verhältnis zur Dateinr.
plt.plot(kleinamp, 'b')
plt.plot(grossamp, 'y')
plt.title("Bode-Amplitude")
plt.ylabel('Amplitude')
plt.xlabel('Versuchnr.')
plt.grid(True)
plt.semilogx()
plt.savefig('bodeamplitudeanzahl.png')
plt.show()

# Darstellung des Phasengangs für beide Lautsprecher im Verhältnis zur Frequenz
plt.plot(zeit, kleinamp, 'b')
plt.plot(zeit, grossamp, 'y')
plt.title("Bode-Amplitude")
plt.ylabel('Amplitude')
plt.xlabel('Frequenz f')
plt.grid(True)
plt.semilogx()
plt.savefig('bodeamplitudefrequenz.png')
plt.show()

# Darstellung des Phasengangs für beide Lautsprecher im Verhältnis zur Dateinr.
plt.plot(kleinphase, 'b')
plt.plot(grossphase, 'y')
plt.title("Bode-Phasengang")
plt.ylabel('Phasenverschiebung')
plt.xlabel('Versuchnr.')
plt.grid(True)
plt.semilogx()
plt.savefig('bodephasenanzahl.png')
plt.show()

# Darstellung des Phasengangs für beide Lautsprecher im Verhältnis zur Frequenz
plt.plot(zeit, kleinphase, 'b')
plt.plot(zeit, grossphase, 'y')
plt.title("Bode-Phasenverschiebung")
plt.ylabel('Phasenverschiebung')
plt.xlabel('Frequenz f')
plt.grid(True)
plt.semilogx()
plt.savefig('bodephasenfrequenz.png')
plt.show()
