import redlab as rl

print("-------einzelneWerte-------------------------")
print("16BitValue:" + str(rl.cbAIn(0, 0, 1)))
print("VoltageValue:" + str(rl.cbVIn(0, 0, 1)))
print("-------Messreihe-------------------------")
print("Messreihe:" + str(rl.cbAInScan(0, 0, 0, 300, 8000, 1)))
print("Messreihe:" + str(rl.cbVInScan(0, 0, 0, 300, 8000, 1)))
print("Samplerate:" + str(rl.cbInScanRate(0, 0, 0, 8000)))
print("Nyquist:" + str(rl.cbInScanRate(0, 0, 0, 8000) / 2))
print("-------Ausgabe-------------------------")
