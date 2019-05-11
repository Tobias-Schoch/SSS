import matplotlib.pyplot as plt
import numpy as np

sound = ["klein100", "klein200", "klein300", "klein400", "klein500", "klein700", "klein850", "klein1000",
         "klein1200", "klein1500", "klein1700", "klein2000", "klein3000", "klein4000", "klein5000", "klein6000",
         "klein10000", "gross100", "gross200", "gross300", "gross400", "gross500", "gross700", "gross850", "gross1000",
         "gross1200", "gross1500", "gross1700", "gross2000", "gross3000", "gross4000", "gross5000", "gross6000",
         "gross10000", "klein100_2", "klein200_2", "klein300_2", "klein400_2", "klein500_2", "klein700_2", "klein850_2",
         "klein1000_2", "klein1200_2", "klein1500_2", "klein1700_2", "klein2000_2", "klein3000_2", "klein4000_2",
         "klein5000_2", "klein6000_2", "klein10000_2", "gross100_2", "gross200_2", "gross300_2", "gross400_2",
         "gross500_2", "gross700_2", "gross850_2", "gross1000_2", "gross1200_2", "gross1500_2", "gross1700_2",
         "gross2000_2", "gross3000_2", "gross4000_2", "gross5000_2", "gross6000_2", "gross10000_2"]

for a in range(0,68):
    x, y = np.loadtxt('data/' + sound[a] + '.csv', delimiter=',', unpack=True)
    sound[a] = np.loadtxt('data/' + sound[a] + '.csv', delimiter=',', unpack=True)

    plt.plot(x, y, 'b')
    plt.ylabel('Spannung in V')
    plt.xlabel('Zeit t')
    plt.grid(True)
    plt.show()