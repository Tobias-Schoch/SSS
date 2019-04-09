import numpy as np

ten = -1
data = 0
count = 0
average = 0
dumob = 0

vec = np.zeros((21, 3))
rang = ["10", "13", "16", "19", "22", "25", "28", "31", "34", "37", "40", "43", "46", "49", "52", "55", "58", "61",
        "64", "67", "70"]

for x in rang:
    ten += 1
    data = np.genfromtxt('data/' + str(rang[ten]) + '.csv', delimiter=",", skip_header=1000, skip_footer=499)

    print("Durchschnitt " + str(rang[ten]) + "cm:" + str(np.nanmean(data)))
    print("Standartabweichung " + str(rang[ten]) + "cm:" + str(np.nanstd(data)) + "\n")