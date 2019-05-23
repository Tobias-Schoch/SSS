from scipy import signal

import matplotlib.pyplot as plt
import numpy as np

# Einlesen der .csv Datei

num = ["hoch1", "hoch2", "hoch3", "hoch4", "hoch5", "tief1", "tief2", "tief3", "tief4", "tief5", "links1", "links2",
       "links3", "links4", "links5", "rechts1", "rechts2", "rechts3", "rechts4", "rechts5"]
gaussianwindow = signal.windows.gaussian(512, std=4)

# Darstellung des Amplitudenspektrums
plt.plot(gaussianwindow)
plt.grid(True)
plt.xlabel('Signalnr.')
plt.ylabel('Frequenz')
plt.savefig('data/img/gauss.png')
plt.show()

for a in range(0, 20):
    data = np.load('data/' + str(num[a]) + '.npy')
    window = np.zeros((86, 512))
    z = 256

    for y in range(0, 86):
        z = z - 256
        for x in range(0, 512):
            window[y, x] = np.mean(np.abs(np.fft.fft(data[z] * gaussianwindow)))
            z = z + 1
        # plt.plot(window[y])
        # plt.title('Windownr' + str(y+1))
        # plt.xlabel('Signalnr.')
        # plt.ylabel('Frequenz')
        # plt.grid(True)
        # plt.savefig('data/img/' + str(y) + '.png')
        # plt.show()

    for y in range(0, 86):
        for x in range(0, 512):
            window[y][x] = window[y][x] * gaussianwindow[x]
        window[y] = np.abs(np.fft.fft(window[y]))
        window[y] = np.mean(window[y])

    plt.plot(window, 'r')
    plt.grid(True)
    plt.xlabel('Signalnr.')
    plt.ylabel('Frequenz')
    plt.savefig('data/img/' + num[a] + 'AlleRichtig.png')
    plt.show()
