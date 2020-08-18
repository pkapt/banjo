import numpy as np
import scipy
from scipy.io import wavfile
from pitches import Converter
from pytablature.tab import Tab, Note
from pytablature.tab.const import *
from math import floor

file_path = "cmaj.wav"
SAMPLE_FREQ = 26 #samples per sec

def get_freq(audio, sampling_rate):
    n = len(audio)
    T = 1/sampling_rate
    yf = scipy.fft.fft(audio)
    yf = 2.0/n * np.abs(yf[:n//2])
    xf = np.linspace(int(0), int(1.0/(2.0*T)), int(n/2))
    return xf[np.where(yf == np.amax(yf))]

'''
split the audio file into a bunch of chunks
'''
(rate, sig) = wavfile.read(file_path)
duration = len(sig) / rate # samples per sec
split_num = floor(len(sig) / 1000)
sig = sig[:len(sig)-len(sig)%1000]
sig = np.split(sig, split_num) # SPLIT AUDIO FILE INTO SMALL CHUNKS

'''
get the strongest frequency associated with each chunk 
and convert the frequencies to notes
'''
c = Converter()
note_chunks = []
for chunk in sig:
    data = chunk[:,0]
    freq = get_freq(data, rate)
    if floor(freq[0]) != 0:
        note_chunks.append(c.pitch(freq[0]))

'''
group all the similar consecutive chunks into notes
'''
notes = []
last_chunk = note_chunks[0]
for current_chunk in note_chunks:
    if current_chunk != last_chunk:
        notes.append(last_chunk)
    last_chunk = current_chunk

'''
convert the notes into a tab
'''
notes = [Note(note, duration=QUARTER) for note in notes]

tab = Tab(notes)
tab.generate()


