import math
import stdaudio
import sys

def tone(hz, duration):
    n = int(44100 * duration)
    note = [0.0]*(n+1)
    for i in range(n+1):
        note[i] = math.sin(2.0 * math.pi * i * hz / 44100)
    stdaudio.playSamples(note)

if __name__ == '__main__':
    hz = float(sys.argv[1])
    duration = float(sys.argv[2])
    tone(hz, duration)
