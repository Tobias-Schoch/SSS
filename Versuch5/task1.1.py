import numpy as np
import matplotlib.pyplot as plt

hz = ["2060", "2910", "3760", "4615", "5498", "6387", "8020"]
plot = ["2060", "2910", "3760", "4615", "5498", "6387", "8020"]
color = ["c", "r", "b", "y", "g", "k", "m"]

for x in range(0, 7):
    hz[x] = np.load("data/numpy/" + hz[x] + ".npy")
    plt.xlabel("Samples")
    plt.ylabel("Spannung")
    plt.title("Frequenz" + plot[x])
    plt.plot(hz[x], label=plot[x], color=color[x])
    plt.grid(True)
    plt.legend()
    plt.savefig("data/img/" + plot[x] + "plot.png")
    plt.show()