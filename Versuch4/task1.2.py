# -------------------------------------
# Task 1.2
# -------------------------------------

import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import time

def time_axis(arr):
    return np.array(range(len(arr)))/44100

FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 44100
NOFFRAMES = 2

p = pyaudio.PyAudio()
print('running')
stream = p.open(format=FORMAT, channels=1, rate=SAMPLEFREQ,
                input=True, frames_per_buffer=FRAMESIZE)
data = stream.read(NOFFRAMES * FRAMESIZE)
decoded = np.fromstring(data, 'Int16') / ((2**15)/2-1)
stream.stop_stream()
stream.close()
p.terminate()

start = np.argmax(np.abs(decoded) > 0.05) - 1024
end = start + 44100
triggered = decoded[start:end]
triggered = np.concatenate((triggered, [0]*(44100 - end - start)))

np.savetxt("aufgabe4/tief_5_" + str(int(time.time())) + ".npy", triggered)
