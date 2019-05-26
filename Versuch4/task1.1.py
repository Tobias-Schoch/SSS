# -------------------------------------
# Task 1.1
# -------------------------------------

import pyaudio
import numpy
import matplotlib.pyplot as plt

# Voreinstellungen für die Aufnahme
FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 220
p = pyaudio.PyAudio()
print('running')

# Aufnahmestart
stream = p.open(format=FORMAT,
                channels=1,
                rate=SAMPLEFREQ,
                input=True,
                frames_per_buffer=FRAMESIZE)
data = stream.read(NOFFRAMES * FRAMESIZE)
decoded = numpy.fromstring(data, 'Int16');
# Aufnamespektrum ausgeben in eine Numpy Datei
numpy.save('aufgabe4/test.npy', decoded)

# Aufnahmestop
stream.stop_stream()
stream.close()
p.terminate()
