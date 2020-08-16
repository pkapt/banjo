import numpy as np
import scipy
from scipy.io import wavfile

file_path = "cmaj.wav"
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

yf = get_freq(y1, samples)
print(yf)

(rate, sig) = wavfile.read(file_path)
duration = len(sig) / rate # samples per sec
print(duration)

split_num = stupid_get_closest_divisor( len(sig), duration * SAMPLE_FREQ )
print(split_num)
sig = np.split(sig, split_num)

