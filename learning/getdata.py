#from mido import MidiFile
from mido import *
import mido
import array
import re
import numpy as np
data = []
dur = []
songs = ["furelise.mid", "jules_mad_world.mid", "minute in g.mid", "duet1.mid"]
for song in songs:
    print(song)

    mid = mido.MidiFile(song)
    cl = ""
    ct = ""
    for msg in mid.play():
        #print(msg)
        cl = str(msg)
        ct = str(msg)
        if 'note' in cl:
            cl=(cl.split("note=",1)[1])
            #print(int(cl[0:3]))
            data.append(int(cl[0:3]))    
            ct=(ct.split("time=",1)[1])
            print(float(ct[0:6])*10)
            dur.append(float(ct[0:4])*10)    
    

data = np.array(data)  
data = data.reshape(-1, 1)
print(data)   
dur = np.array(dur)  
dur = dur.reshape(-1, 1)
print(dur)        
np.savetxt('song-data.txt', data)
np.savetxt('song-duration-data.txt', dur)
