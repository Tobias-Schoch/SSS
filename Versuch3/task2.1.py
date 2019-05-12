import matplotlib.pyplot as plt
import numpy as np

# Array um die einzelnen .csv Dateien einzulesen des kleinen Lautsprechers
klein = ["klein100", "klein200", "klein300", "klein400", "klein500", "klein700", "klein850", "klein1000",
         "klein1200", "klein1500", "klein1700", "klein2000", "klein3000", "klein4000", "klein5000",
         "klein6000", "klein10000"]
# Array um die einzelnen .csv Dateien einzulesen des großen Lautsprechers
gross = ["gross100", "gross200", "gross300", "gross400", "gross500", "gross700", "gross850", "gross1000",
         "gross1200", "gross1500", "gross1700", "gross2000", "gross3000", "gross4000", "gross5000",
         "gross6000", "gross10000"]

# for-Schleife für die 17 unterschiedlichen .csv Dateien
for a in range(0, 17):
    # Einlesen der kleinen Dateien - dabei wird die linke Spalte als x und die rechte als y definiert
    x, y = np.loadtxt('data/' + klein[a] + '.csv', delimiter=',', unpack=True)
    # Einlesen der großen Dateien - dabei wird die linke Spalte als u und die rechte als v definiert
    u, v = np.loadtxt('data/' + gross[a] + '.csv', delimiter=',', unpack=True)

    # Die einzelnen .csv Dateien des kleinen Lautsprechers werden in jeweils einem Plot dargestellt
    plt.plot(x, y, 'b')
    plt.title(klein[a])
    plt.ylabel('Spannung in V')
    plt.xlabel('Zeit t')
    plt.grid(True)
    plt.savefig(str(klein[a]) + '.png')
    plt.show()

    # Die einzelnen .csv Dateien des großen Lautsprechers werden in jeweils einem Plot dargestellt
    plt.plot(u, v, 'g')
    plt.title(gross[a])
    plt.ylabel('Spannung in V')
    plt.xlabel('Zeit t')
    plt.grid(True)
    plt.savefig(str(gross[a]) + '.png')
    plt.show()

    # Die ersten beiden Zeiten für den kleinen Lautsprecher werden in time1 geschrieben
    time1 = x[:2, ]
    # Die ersten beiden Zeiten für den großen Lautsprecher werden in time1 geschrieben
    time2 = u[:2, ]

    # Die zwei Zeiten des kleinen Lautsprechers werden subtrahiert und multipliziert
    # für eine mikrosekunden Darstellung
    # Zudem wird die berechnete Dauer gerundet
    timing1 = round((time1[1] - time1[0]) * 100000, 5)
    # Die zwei Zeiten des großen Lautsprechers werden subtrahiert und multipliziert
    # für eine mikrosekunden Darstellung
    # Zudem wird die berechnete Dauer gerundet
    timing2 = round((time2[1] - time2[0]) * 100000, 5)

    # Ausgeben einer Tabelle im LaTeX Format
    print("/hline")
    # Der maximale Amplitudenwert des kleinen Lautsprechers für die jeweilige Frequenz
    print("Amplitude:", klein[a], np.max(np.abs(y)))
    # Der maximale Amplitudenwert des großen Lautsprechers für die jeweilige Frequenz
    print("Amplitude:", gross[a], np.max(np.abs(v)))
    print("ms", klein[a], timing1)
    print("ms", gross[a], timing2)

print("/hline")
