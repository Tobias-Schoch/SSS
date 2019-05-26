# -------------------------------------
# Task 1.2
# -------------------------------------

import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import time

def time_axis(arr):
    return np.array(range(len(arr)))/44100

# Voreinstellungen für die Aufnahme
FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 44100
NOFFRAMES = 2

# Aufnahmefunktion der Soundkarte
p = pyaudio.PyAudio()
print('running')
# Aufnahmestart
stream = p.open(format=FORMAT, channels=1, rate=SAMPLEFREQ,
                input=True, frames_per_buffer=FRAMESIZE)
data = stream.read(NOFFRAMES * FRAMESIZE)
decoded = np.fromstring(data, 'Int16') / ((2**15)/2-1)
# Aufnahmestop
stream.stop_stream()
stream.close()
p.terminate()

# Triggerfunktion lässt die Funktion erst ab Schwellenwert starten
start = np.argmax(np.abs(decoded) > 0.05) - 1024
# Berechnung des Endwerts der Aufnahme
end = start + 44100
triggered = decoded[start:end]
triggered = np.concatenate((triggered, [0]*(44100 - end - start)))
# Aufnamespektrum ausgeben in eine Numpy Datei
np.savetxt("aufgabe4/tief_5_" + str(int(time.time())) + ".npy", triggered)
