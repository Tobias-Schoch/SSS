import matplotlib.pyplot as plt
import numpy as np

klein = ["klein100", "klein200", "klein300", "klein400", "klein500", "klein700", "klein850", "klein1000",
         "klein1200", "klein1500", "klein1700", "klein2000", "klein3000", "klein4000", "klein5000", "klein6000",
         "klein10000"]
gross = ["gross100", "gross200", "gross300", "gross400", "gross500", "gross700", "gross850", "gross1000",
         "gross1200", "gross1500", "gross1700", "gross2000", "gross3000", "gross4000", "gross5000", "gross6000",
         "gross10000"]

for a in range(0, 17):
    x, y = np.loadtxt('data/' + klein[a] + '.csv', delimiter=',', unpack=True)
    u, v = np.loadtxt('data/' + gross[a] + '.csv', delimiter=',', unpack=True)

    plt.plot(x, y, 'b')
    plt.title(klein[a])
    plt.ylabel('Spannung in V')
    plt.xlabel('Zeit t')
    plt.grid(True)
    #plt.savefig(str(klein[a]) + '.png')
    #plt.show()

    plt.plot(u, v, 'g')
    plt.title(gross[a])
    plt.ylabel('Spannung in V')
    plt.xlabel('Zeit t')
    plt.grid(True)
    #plt.savefig(str(gross[a]) + '.png')
    #plt.show()

    time1 = x[:2,]
    time2 = u[:2,]

    timing1 = round((time1[1] - time1[0]) * 100000, 5)
    timing2 = round((time2[1] - time2[0]) * 100000, 5)

    print("/hline")
    #print("Amplitude:", klein[a], np.max(np.abs(y)))
    #print("Amplitude:", gross[a], np.max(np.abs(v)))
    print("ms", klein[a], timing1)
    print("ms", gross[a], timing2)

print("/hline")