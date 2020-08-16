import librosa
from librosa import display
import matplotlib.pyplot as plt
import numpy as np
import scipy

file_path = "cmaj.wav"

samples = 100
f = 3
x = np.arange(samples)
y1 = np.sin(2*np.pi*f * (x/samples))

def fft_plot(audio, sampling_rate):
    n = len(audio)
    T = 1/sampling_rate
    yf = scipy.fft(audio)
    # yf = 2.0/n * np.abs(yf[:n//2])
    xf = np.linspace(int(0), int(1.0/(2.0*T)), int(n/2))
    print(xf)
    fig, ax = plt.subplots()
    ax.plot(xf, 2.0/n * np.abs(yf[:n//2]))
    plt.grid()
    plt.xlabel("freq")
    plt.ylabel("mag")
    return plt.show()
    return yf

yf = fft_plot(y1, samples)
print(yf)
