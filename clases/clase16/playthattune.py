import math
import stdio # this is new!
import stdaudio

SPS = 44100
CONCERT_A = 440.0
NOTES_ON_SCALE = 12.0

while not stdio.isEmpty():
    pitch = stdio.readInt()
    duration = stdio.readFloat()
    hz = CONCERT_A * (2.0 ** (pitch / NOTES_ON_SCALE))
    n = int(SPS * duration)
    note = [0.0]*(n+1)
    for i in range(n+1):
        note[i] = math.sin(2.0 * math.pi * i * hz / SPS)
    stdaudio.playSamples(note)

stdaudio.wait()
