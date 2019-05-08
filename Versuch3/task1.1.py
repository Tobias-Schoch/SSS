from TekTDS2000 import *

scope = TekTDS2000()

# Einlesen vom Channel 1 und vom Channel 2
scope.saveCsv(filename='versuch3/kleinerLautsprecher/100.csv', ch=1)
scope.saveCsv(filename='100_2.csv', ch=2)