import cv2

# ------------------------------ Aufgabe1.1 ------------------------------ #

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 200)
cap.set(11, 32)
cap.set(12, 32)
cap.set(14, 20)
cap.set(15, -4)
cap.set(17, 10000)

while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", gray)
    for x in range(1, 11):
        cv2.imwrite("data/bild" + str(x) + ".png", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break;

# cv2.imwrite("data/bild.png", frame)

print("frame width: " + str(cap.get(3)))
print("frame height: " + str(cap.get(4)))
print("--------------------------------")
print("brightness: " + str(cap.get(10)))
print("contrast: " + str(cap.get(11)))
print("saturation: " + str(cap.get(12)))
print("--------------------------------")
print("gain: " + str(cap.get(14)))
print("exposure: " + str(cap.get(15)))
print("--------------------------------")
print("white balance: " + str(cap.get(17)))

cap.release()
cv2.destroyAllWindows()
