from midiutil.MidiFile import MIDIFile
import random
import time as tiemp
from decimal import Decimal
from array import *
mf = MIDIFile(1)  
track = 0   
time = 0    
mf.addTrackName(track, time, "Music mash")
mf.addTempo(track, time, 80)
channel = 0
volume = 100
def append(pt,t,d):
    pitch = pt           # tn
    time = t             # bt start
    duration = d         # length of beat
    mf.addNote(track, channel, pitch, time, duration, volume)
pp = 67
ch = 0
rd = 200
rd = int(rd)
array= array('i', [])
print(f"max render time:{rd*9}s, {(rd*9)/60}min")
for n in range(rd):
    delay = random.randint(5, 9)
    for s in range(1):
        pp = random.randint(pp-9, pp+9)
        if pp >= 90:
            pp = 68
        if pp <= 29:
            pp = 41
        append(pp, n+0.5, delay/2)    
        array.append(pp)
    if delay >= 7:
        for p in range(1):
            ch = random.randint(56, 67)
            #ch = random.randint(ch-3, ch+3)
            if ch >= 90:
                ch = 50
            if ch <= 40:
                ch = 50
            append(ch, n, delay+6)    
    print(f"section {n} composed, current: d:{delay+2}, noteChord: {ch}, notes: {pp}")

with open(f"music_track{random.randint(10, 3000)}.mid", 'wb') as outf:
    print(mf)
    mf.writeFile(outf)
    input()
    print(array)