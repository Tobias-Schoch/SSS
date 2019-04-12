import numpy as np

data = 0
data2 = 0
faktor1 = 1
faktor2 = 1.96

data = np.genfromtxt('data/DinA4Breit.csv', delimiter=",", skip_header=1000, skip_footer=499,
                     usecols=(4))
data2 = np.genfromtxt('data/DinA4Lang.csv', delimiter=",", skip_header=1000, skip_footer=499,
                      usecols=(4))


stdaritl = np.std(data2) / np.sqrt(1000)
stdaritb = np.std(data) / np.sqrt(1000)



a = np.log(29.7)/np.log(np.mean(data2))
b = np.log(29.7)-(a*np.log(np.mean(data2)))
a1 = np.log(21)/np.log(np.mean(data))
b1 = np.log(21)-(a*np.log(np.mean(data)))


korrektur_lang = (np.mean(data2) + faktor2 * stdaritl) - np.mean(data2)
korrektur_breit = (np.mean(data) + faktor2 * stdaritb) - np.mean(data)
z1 = (np.exp(b)*a*np.mean(data2)**(a-1))
z2 = (np.exp(b)*a*np.mean(data)**(a-1))
deltay65 = z1 * stdaritl
deltay96 = z1 * korrektur_lang
deltayb65 = z2 * stdaritb
deltayb96 = z2 * korrektur_breit


print("29.7 cm", deltay65, "cm 68%")
print("29.7 cm", deltay96, "cm 95%")
print("21 cm", deltayb65, "cm 68%")
print("21 cm", deltayb96, "cm 95%")
print("623,7 cm^2", (deltay65+deltayb65), "cm bei 68%")
print("623,7 cm^2", (deltay96+deltayb96), "cm bei 95%")
