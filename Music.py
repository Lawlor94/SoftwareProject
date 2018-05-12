import time
from MusicHelper import MusicHelper

#AssignToGrid([3,2,0,0,0,3]) # G Maj
#AssignToGrid([0,3,2,0,1,0]) # C Maj
#AssignToGrid([0,0,2,2,1,0]) # A min
#AssignToGrid([0,2,2,1,0,0]) # E Maj
#AssignToGrid([0,0,0,2,3,2]) # D Maj
# e A D G B E


class Music():
    def fourChords(self, beat):
        m = MusicHelper()
        t = time.time()
        
           
        m.AssignToGrid([3,2,0,0,0,3])
        print time.time() - t
        print "G"
        time.sleep(beat)

        m.AssignToGrid([0,0,0,2,3,2])
        print time.time() - t
        print "D"
        time.sleep(beat)
        
        m.AssignToGrid([0,0,2,2,1,0])
        print time.time() - t
        print "a"
        time.sleep(beat)

        m.AssignToGrid([0,2,2,1,0,0])
        print time.time() - t
        print "E"
        time.sleep(beat)

