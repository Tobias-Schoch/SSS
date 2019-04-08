import numpy as np

ten = -1
data = 0
count = 0
average = 0

vec = np.zeros((21, 3))
rang = ["10", "13", "16", "19", "22", "25", "28", "31", "34", "37", "40", "43", "46", "49", "52", "55", "58", "61",
        "64", "67", "70"]

between = range[1001, 2000, 1]

for x in rang:
    for y in between:
        ten += 1
        data = np.genfromtxt('data/' + str(rang[ten]) + '.csv', delimiter=",")
        count += 1
        average = average

    print("Der Durchschnitt bei " + str(rang[ten]) + "cm Entfernung beträgt: " + str(average) + " cm")

    vec[ten, 0] = str(rang[ten])
    #vec[ten, 1] = np.mean(data[1001, 2000])
    #vec[ten, 2] = np.std(data[1001, 2000])

