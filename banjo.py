import numpy as np
import scipy
from scipy.io import wavfile
from pitches import Converter

file_path = "guitar.wav"
SAMPLE_FREQ = 26 #samples per sec

samples = 100
f = 3
x = np.arange(samples)
y1 = np.sin(2*np.pi*f * (x/samples))

def get_freq(audio, sampling_rate):
    n = len(audio)
    T = 1/sampling_rate
    yf = scipy.fft.fft(audio)
    yf = 2.0/n * np.abs(yf[:n//2])
    xf = np.linspace(int(0), int(1.0/(2.0*T)), int(n/2))
    return xf[np.where(yf == np.amax(yf))]

def stupid_get_closest_divisor(length, base_div):
    while True:
        if length % base_div == 0:
            return base_div
        base_div += 1

(rate, sig) = wavfile.read(file_path)
duration = len(sig) / rate # samples per sec
split_num = round(len(sig) / 1000)
print(split_num)
sig = sig[:len(sig)-len(sig)%1000]
print(len(sig))
sig = np.split(sig, split_num) # SPLIT AUDIO FILE INTO SMALL CHUNKS

c = Converter()
print("got here")
for chunk in sig:
    data = chunk[:,0]
    freq = get_freq(data, rate)
    print(c.pitch(freq[0]))



