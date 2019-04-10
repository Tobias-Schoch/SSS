import numpy as np
import matplotlib.pyplot as plt

ten = -1
data = 0
vec = np.zeros((21, 3))
vec2 = np.zeros((21, 3))

rang = ["10", "13", "16", "19", "22", "25", "28", "31", "34", "37", "40", "43", "46", "49", "52", "55", "58", "61",
        "64", "67", "70"]

for x in rang:
    ten += 1
    data = np.genfromtxt('data/' + str(rang[ten]) + '.csv', delimiter=",", skip_header=1000, skip_footer=499, usecols=(4))


    print("Durchschnitt " + str(rang[ten]) + "cm:" + str(np.mean(data)))
    print("Standartabweichung " + str(rang[ten]) + "cm:" + str(np.std(data)) + "\n")

    vec[ten, 0] = rang[ten]
    vec[ten, 1] = np.nanmean(data)
    vec[ten, 2] = np.nanstd(data)
    vec2[ten, 0] = rang[ten]
    vec2[ten, 1] = np.log(np.mean(data))
    vec2[ten, 2] = np.log(np.std(data))




plt.plot([10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70], [vec[0, 1], vec[1, 1], vec[2, 1], vec[3, 1], vec[4, 1], vec[5, 1], vec[6, 1], vec[7, 1], vec[8, 1], vec[9, 1], vec[10, 1], vec[11, 1], vec[12, 1], vec[13, 1], vec[14, 1], vec[15, 1], vec[16, 1], vec[17, 1], vec[18, 1], vec[19, 1], vec[20, 1]],  'b')
plt.ylabel('Durchschnitt')
plt.xlabel('cm')
plt.axis([0, 70, 0, 1.5])
plt.show()

plt.plot([10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70], [vec[0, 2], vec[1, 2], vec[2, 2], vec[3, 2], vec[4, 2], vec[5, 2], vec[6, 2], vec[7, 2], vec[8, 2], vec[9, 2], vec[10, 2], vec[11, 2], vec[12, 2], vec[13, 2], vec[14, 2], vec[15, 2], vec[16, 2], vec[17, 2], vec[18, 2], vec[19, 2], vec[20, 2]],  'r')
plt.ylabel('Standardabweichung')
plt.xlabel('cm')
plt.axis([0, 70, 0, 0.12])
plt.show()

plt.plot([vec2[0, 0], vec2[1, 0], vec2[2, 0], vec2[3, 0], vec2[4, 0], vec2[5, 0], vec2[6, 0], vec2[7, 0], vec2[8, 0], vec2[9, 0], vec2[10, 0], vec2[11, 0], vec2[12, 0], vec2[13, 0], vec2[14, 0], vec2[15, 0], vec2[16, 0], vec2[17, 0], vec2[18, 0], vec2[19, 0], vec2[20, 0]], [vec2[0, 1], vec2[1, 1], vec2[2, 1], vec2[3, 1], vec2[4, 1], vec2[5, 1], vec2[6, 1], vec2[7, 1], vec2[8, 1], vec2[9, 1], vec2[10, 1], vec2[11, 1], vec2[12, 1], vec2[13, 1], vec2[14, 1], vec2[15, 1], vec2[16, 1], vec2[17, 1], vec2[18, 1], vec2[19, 1], vec2[20, 1]],  'b')
plt.ylabel('Durchschnitt von Log')
plt.xlabel('cm')
plt.axis([0, 70, -1.2, 1])
plt.show()


