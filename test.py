from math import log2, pow


class Converter:
    A4 = 440
    C0 = A4*pow(2, -4.75)
    NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
    def __init__(self):
        pass

    def pitch(self, freq):
        h = round(12*log2(freq/self.C0))
        octave = h // 12
        n = h % 12
        return self.NOTES[n] + str(octave)

    def freq(self, name):
        if name[1] == '#':
            octave = int(name[2:])
            steps = self.NOTES.index(name[0:2].upper())
        else:
            octave = int(name[1])
            steps = self.NOTES.index(name[0].upper())
        return (self.C0*(2**octave))*(2**(steps/12))

c = Converter()
p = c.pitch(530.26052104)
print(p)

