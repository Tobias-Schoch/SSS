import matplotlib.pyplot as plt
import numpy as np

klein = ["klein100", "klein200", "klein300", "klein400", "klein500", "klein700", "klein850", "klein1000",
         "klein1200", "klein1500", "klein1700", "klein2000", "klein3000", "klein4000", "klein5000", "klein6000",
         "klein10000"]
gross = ["gross100", "gross200", "gross300", "gross400", "gross500", "gross700", "gross850", "gross1000",
         "gross1200", "gross1500", "gross1700", "gross2000", "gross3000", "gross4000", "gross5000", "gross6000",
         "gross10000"]

zeit = [100, 200, 300, 400, 500, 700, 850, 1000, 1200, 1500, 1700, 2000, 3000, 4000, 5000, 6000, 10000]
kleinphase = [228, 295, 113.2, 105.2, 70.6, 64.8, 34, 4.2, 1.8, 12.2, 12.1, 14.7, 8.88, 11.60, 5.92, 6.92, 3.67]
grossphase = [505, 82, 1, 10, 17, 12.4, 15.2, 14.8, 15.6, 12.8, 13.2, 14.4, 19.7, 12.52, 5.32, 3.32, 4.74]

kleinamp = np.zeros(17)
grossamp = np.zeros(17)

for a in range(0, 17):
    x, y = np.loadtxt('data/' + klein[a] + '.csv', delimiter=',', unpack=True)
    u, v = np.loadtxt('data/' + gross[a] + '.csv', delimiter=',', unpack=True)

    kleinamp[a] = np.max(np.abs(y))
    grossamp[a] = np.max(np.abs(v))

plt.plot(kleinamp, 'b')
plt.plot(grossamp, 'y')
plt.title("Amplitude")
plt.ylabel('Amplitude')
plt.xlabel('Versuchnr.')
plt.grid(True)
plt.savefig('amplitudeanzahl.png')
plt.show()

plt.plot(zeit, kleinamp, 'b')
plt.plot(zeit, grossamp, 'y')
plt.title("Amplitude")
plt.ylabel('Amplitude')
plt.xlabel('Zeit t')
plt.grid(True)
plt.savefig('amplitudefrequenz.png')
plt.show()

plt.plot(kleinphase, 'b')
plt.plot(grossphase, 'y')
plt.title("Phasengang")
plt.ylabel('Phasenverschiebung')
plt.xlabel('Versuchnr.')
plt.grid(True)
plt.savefig('phasenanzahl.png')
plt.show()

plt.plot(zeit, kleinphase, 'b')
plt.plot(zeit, grossphase, 'y')
plt.title("Phasenverschiebung")
plt.ylabel('Amplitude')
plt.xlabel('Zeit t')
plt.grid(True)
plt.savefig('phasenfrequenz.png')
plt.show()


