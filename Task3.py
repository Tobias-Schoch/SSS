import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

ten = -1
data = 0
vec2 = np.zeros((21, 2))
vec3 = np.zeros((21, 2))
vec4 = np.zeros((21, 1))

rang = ["10", "13", "16", "19", "22", "25", "28", "31", "34", "37", "40", "43", "46", "49", "52", "55", "58", "61",
        "64", "67", "70"]

for x in rang:
    ten += 1
    data = np.genfromtxt('data/DinA4Breit.csv', delimiter=",", skip_header=1000, skip_footer=499,
                         usecols=(4))
    data = np.genfromtxt('data/DinA4.csv', delimiter=",", skip_header=1000, skip_footer=499,
                         usecols=(4))

    vec2[ten, 0] = np.log(int(rang[ten]))
    vec2[ten, 1] = np.log(np.mean(data))

    vec3[ten, 0] = rang[ten]
    vec3[ten, 1] = np.mean(data)

    print("Distanz: " + str(vec3[ten, 0]))
    print("Spannung: " + str(vec3[ten, 1]))

    vec4[ten, 0] = (vec2[ten, 0] / vec2[ten, 1]) * vec2[ten, 1]