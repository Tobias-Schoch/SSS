import numpy as np
import cv2

# -------- dead -------- #

# Values for dark x & y
rheingut = 4
brauhaus = 11
burgersaal = 14
palmensaal = 10
hus = 17
schweizer = 7
schanzle = 5
yoga = 4
scho = 6
fisch = 7
weber = 9
pent = 1

xrheingut = 506
xbrauhaus = 935
xburgersaal = 835
xpalmensaal = 429
xhus = 730
xschweizer = 240
xschanzle = 304
xyoga = 413
xscho = 590
xfisch = 155
xweber = 703
xpent = 405


yrheingut = 162
ybrauhaus = 338
yburgersaal = 555
ypalmensaal = 656
yhus = 761
yschweizer = 451
yschanzle = 66
yyoga = 385
yscho = 356
yfisch = 215
yweber = 78
ypent = 249

faktor = 20
faktor2 = 45

r, g, b = 128, 0, 0
r1, g1, b1 = 142, 123, 228

alpha = 0.5

# Bild einlesen
image = cv2.imread("data/map.png")
overlay = image.copy()

vec = [rheingut, brauhaus, burgersaal, palmensaal, hus, schweizer, schanzle, yoga, scho, fisch, weber, pent]
vecx = [xrheingut, xbrauhaus, xburgersaal, xpalmensaal, xhus, xschweizer, xschanzle, xyoga, xscho, xfisch, xweber, xpent]
vecy = [yrheingut, ybrauhaus, yburgersaal, ypalmensaal, yhus, yschweizer, yschanzle, yyoga, yscho, yfisch, yweber, ypent]

for x in range(12):
    if (vec[x] == 1):
        cv2.circle(image, (vecx[x], vecy[x]), vec[x] * faktor2, (r, g, b), -1)

    if (vec[x] != 1):
        cv2.circle(image, (vecx[x], vecy[x]), vec[x] * faktor, (r1, g1, b1), -1)

cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)
# Bild anzeigen und exportieren
cv2.imshow('image', image)
cv2.imwrite("zzz.png", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
