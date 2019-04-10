import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit
from scipy.optimize import differential_evolution
import warnings
from math import *

ten = -1
data = 0
vec2 = np.zeros((21, 2))
vec3 = np.zeros((21, 2))
vec4 = np.zeros((21, 1))

rang = ["10", "13", "16", "19", "22", "25", "28", "31", "34", "37", "40", "43", "46", "49", "52", "55", "58", "61",
        "64", "67", "70"]

for x in rang:
    ten += 1
    data = np.genfromtxt('data/' + str(rang[ten]) + '.csv', delimiter=",", skip_header=1000, skip_footer=499,
                         usecols=(4))

    vec2[ten, 0] = np.log(int(rang[ten]))
    vec2[ten, 1] = np.log(np.mean(data))

    vec3[ten, 0] = rang[ten]
    vec3[ten, 1] = np.mean(data)

    print("Distanz: " + str(vec3[ten, 0]))
    print("Spannung: " + str(vec3[ten, 1]))

    vec4[ten, 0] = (vec2[ten, 1] / vec2[ten, 0]) * vec3[ten, 1]

    print(str(vec4[ten, 0]))

x = np.array(
    [vec2[0, 0], vec2[1, 0], vec2[2, 0], vec2[3, 0], vec2[4, 0], vec2[5, 0], vec2[6, 0], vec2[7, 0], vec2[8, 0],
     vec2[9, 0], vec2[10, 0], vec2[11, 0], vec2[12, 0], vec2[13, 0], vec2[14, 0], vec2[15, 0], vec2[16, 0], vec2[17, 0],
     vec2[18, 0], vec2[19, 0], vec2[20, 0]])
y = np.array(
    [vec2[0, 1], vec2[1, 1], vec2[2, 1], vec2[3, 1], vec2[4, 1], vec2[5, 1], vec2[6, 1], vec2[7, 1], vec2[8, 1],
     vec2[9, 1], vec2[10, 1], vec2[11, 1], vec2[12, 1], vec2[13, 1], vec2[14, 1], vec2[15, 1], vec2[16, 1],
     vec2[17, 1], vec2[18, 1], vec2[19, 1], vec2[20, 1]])

gradient, intercept, r_value, p_value, std_err = stats.linregress(x, y)
mn = np.min(x)
mx = np.max(x)
x1 = np.linspace(mn, mx, 500)
y1 = gradient * x1 + intercept
plt.plot(x, y, 'ob')
plt.plot(x1, y1, '-r')
plt.show()

plt.plot([vec2[0, 0], vec2[1, 0], vec2[2, 0], vec2[3, 0], vec2[4, 0], vec2[5, 0], vec2[6, 0], vec2[7, 0], vec2[8, 0],
          vec2[9, 0], vec2[10, 0], vec2[11, 0], vec2[12, 0], vec2[13, 0], vec2[14, 0], vec2[15, 0], vec2[16, 0],
          vec2[17, 0], vec2[18, 0], vec2[19, 0], vec2[20, 0]],
         [vec2[0, 1], vec2[1, 1], vec2[2, 1], vec2[3, 1], vec2[4, 1], vec2[5, 1], vec2[6, 1], vec2[7, 1], vec2[8, 1],
          vec2[9, 1], vec2[10, 1], vec2[11, 1], vec2[12, 1], vec2[13, 1], vec2[14, 1], vec2[15, 1], vec2[16, 1],
          vec2[17, 1], vec2[18, 1], vec2[19, 1], vec2[20, 1]], 'b')
plt.ylabel('Durchschnitt von Log')
plt.xlabel('cm')
plt.axis([2, 4.5, -1.2, 1])
plt.show()


plt.plot([vec2[0, 0], vec2[1, 0], vec2[2, 0], vec2[3, 0], vec2[4, 0], vec2[5, 0], vec2[6, 0], vec2[7, 0], vec2[8, 0],
          vec2[9, 0], vec2[10, 0], vec2[11, 0], vec2[12, 0], vec2[13, 0], vec2[14, 0], vec2[15, 0], vec2[16, 0],
          vec2[17, 0], vec2[18, 0], vec2[19, 0], vec2[20, 0]],
         [vec4[0, 0], vec4[1, 0], vec4[2, 0], vec4[3, 0], vec4[4, 0], vec4[5, 0], vec4[6, 0], vec4[7, 0], vec4[8, 0],
          vec4[9, 0], vec4[10, 0], vec4[11, 0], vec4[12, 0], vec4[13, 0], vec4[14, 0], vec4[15, 0], vec4[16, 0],
          vec4[17, 0], vec4[18, 0], vec4[19, 0], vec4[20, 0]], 'g')
plt.ylabel('Durchschnitt von Log')
plt.xlabel('cm')
plt.show()
