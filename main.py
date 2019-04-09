import numpy as np
import matplotlib.pyplot as plt
ten = -1
data = 0


vec = np.zeros((21, 3))
rang = ["10", "13", "16", "19", "22", "25", "28", "31", "34", "37", "40", "43", "46", "49", "52", "55", "58", "61",
        "64", "67", "70"]

for x in rang:
    ten += 1
    data = np.genfromtxt('data/' + str(rang[ten]) + '.csv', delimiter=",", skip_header=1000, skip_footer=499)

    print("Durchschnitt " + str(rang[ten]) + "cm:" + str(np.nanmean(data)))
    print("Standartabweichung " + str(rang[ten]) + "cm:" + str(np.nanstd(data)) + "\n")

data10 = np.genfromtxt('data/10.cv', delimiter=",", skip_header=1000, skip_footer=499)
data13 = np.genfromtxt('data/13.cv', delimiter=",", skip_header=1000, skip_footer=499)
data16 = np.genfromtxt('data/16.cv', delimiter=",", skip_header=1000, skip_footer=499)
data19 = np.genfromtxt('data/19.cv', delimiter=",", skip_header=1000, skip_footer=499)
data22 = np.genfromtxt('data/22.cv', delimiter=",", skip_header=1000, skip_footer=499)
data25 = np.genfromtxt('data/25.cv', delimiter=",", skip_header=1000, skip_footer=499)
data28 = np.genfromtxt('data/28.cv', delimiter=",", skip_header=1000, skip_footer=499)
data31 = np.genfromtxt('data/31.cv', delimiter=",", skip_header=1000, skip_footer=499)
data34 = np.genfromtxt('data/34.cv', delimiter=",", skip_header=1000, skip_footer=499)
data37 = np.genfromtxt('data/37.cv', delimiter=",", skip_header=1000, skip_footer=499)
data40 = np.genfromtxt('data/40.cv', delimiter=",", skip_header=1000, skip_footer=499)
data43 = np.genfromtxt('data/43.cv', delimiter=",", skip_header=1000, skip_footer=499)
data46 = np.genfromtxt('data/46.cv', delimiter=",", skip_header=1000, skip_footer=499)
data49 = np.genfromtxt('data/49.cv', delimiter=",", skip_header=1000, skip_footer=499)
data52 = np.genfromtxt('data/52.cv', delimiter=",", skip_header=1000, skip_footer=499)
data55 = np.genfromtxt('data/55.cv', delimiter=",", skip_header=1000, skip_footer=499)
data58 = np.genfromtxt('data/58.cv', delimiter=",", skip_header=1000, skip_footer=499)
data61 = np.genfromtxt('data/61.cv', delimiter=",", skip_header=1000, skip_footer=499)
data64 = np.genfromtxt('data/64.cv', delimiter=",", skip_header=1000, skip_footer=499)
data67 = np.genfromtxt('data/67.cv', delimiter=",", skip_header=1000, skip_footer=499)
data70 = np.genfromtxt('data/70.cv', delimiter=",", skip_header=1000, skip_footer=499)

data10std = np.nanstd(data10)
data13std = np.nanstd(data13)
data10std = np.nanstd(data10)
data10std = np.nanstd(data10)
data10std = np.nanstd(data10)
data10std = np.nanstd(data10)
data10std = np.nanstd(data10)
data10std = np.nanstd(data10)
data10std = np.nanstd(data10)
data10std = np.nanstd(data10)
data10std = np.nanstd(data10)
data10std = np.nanstd(data10)
data10std = np.nanstd(data10)
data10std = np.nanstd(data10)
data10std = np.nanstd(data10)
data10std = np.nanstd(data10)



plt.plot([data10std], [data13std])
plt.axis([0, 1, 0, 1])
plt.show()