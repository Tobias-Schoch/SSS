import numpy as np

data = 0
data2 = 0
faktor1 = 1
faktor2 = 1.96

data = np.genfromtxt('data/DinA4Breit.csv', delimiter=",", skip_header=1000, skip_footer=499,
                     usecols=(4))
data2 = np.genfromtxt('data/DinA4Lang.csv', delimiter=",", skip_header=1000, skip_footer=499,
                      usecols=(4))

stde1 = np.std(data2) / np.sqrt(1000)

a1 = np.log(29.7) / np.log(np.mean(data2))
b1 = np.log(29.7) - (a1 * np.log(np.mean(data2)))
z1 = (np.exp(b1) * a1 * np.mean(data2) ** (a1 - 1))

korrektur_lang = (np.mean(data2) + faktor2 * stde1) - np.mean(data2)
deltaya65 = z1 * stde1
deltaya96 = z1 * korrektur_lang

y = np.exp(b1) * np.power(np.mean(data2), a1)

print(y)
print("29.7 cm", deltaya65, "cm 68%")
print("29.7 cm", deltaya96, "cm 95%")



stde2 = np.std(data) / np.sqrt(1000)
a2 = np.log(21) / np.log(np.mean(data))
b2 = np.log(21) - (a2 * np.log(np.mean(data)))
z2 = (np.exp(b2) * a2 * np.mean(data) ** (a2 - 1))

korrektur_breit = (np.mean(data) + faktor2 * stde2) - np.mean(data)
deltayb65 = z2 * stde2
deltayb96 = z2 * korrektur_breit

print("21 cm", deltayb65, "cm 68%")
print("21 cm", deltayb96, "cm 95%")
print("623,7 cm^2", (deltaya65 + deltayb65), "cm bei 68%")
print("623,7 cm^2", (deltaya96 + deltayb96), "cm bei 95%")
