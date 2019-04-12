import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math


data = 0
data2 = 0
vec1 = np.zeros((2, 3))
korrektur_breit1 = 0
korrektur_lang1 = 0
korrektur_breit2 = 0
korrektur_lang2 = 0
faktor1 = 1
faktor2 = 1.96

data = np.genfromtxt('data/DinA4Breit.csv', delimiter=",", skip_header=1000, skip_footer=499,
                     usecols=(4))
data2 = np.genfromtxt('data/DinA4Lang.csv', delimiter=",", skip_header=1000, skip_footer=499,
                      usecols=(4))



vec1[0, 0] = 21
vec1[0, 1] = np.mean(data)
vec1[0, 2] = np.std(data)

vec1[1, 0] = 29.7
vec1[1, 1] = np.mean(data2)
vec1[1, 2] = np.std(data2)

korrektur_breit1 = 0.861 + faktor1 * vec1[0, 2]
korrektur_lang1 = 0.662 + faktor1 * vec1[1, 2]
korrektur_breit2 = 0.861 + faktor2 * vec1[0, 2]
korrektur_lang2 = 0.662 + faktor2 * vec1[1, 2]

x = math.exp(np.log(vec1[1, 1]))
x1 = np.array([vec1[0, 1]])
x2 = np.array([vec1[0, 1]])

gradient, intercept, r_value, p_value, std_err = stats.linregress(x1, x2)
z1 = (math.exp(intercept)*gradient*x**(gradient-1)) * korrektur_breit1
z2 = math.exp(intercept)*gradient*x**(gradient-1) * korrektur_breit2



print("68,26%: " + str(vec1[0, 1]))
print("68,26%: " + str(korrektur_lang1))
print("95%: " + str(vec1[0, 1]))
print("95%: " + str(korrektur_lang2))
print(str(z1))
print(str(z2))
