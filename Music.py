import time
from MusicHelper import MusicHelper
from LED_Controller import LED_Controller

#AssignToGrid([3,2,0,0,0,3]) # G Maj
#AssignToGrid([0,3,2,0,1,0]) # C Maj
#AssignToGrid([0,0,2,2,1,0]) # A min
#AssignToGrid([0,2,2,1,0,0]) # E Maj
#AssignToGrid([0,0,0,2,3,2]) # D Maj
# e A D G B E


class Music():
    def playSong(self, song, difficulty):
        
        
        
        beat = 1.5
        
        if difficulty == "Easy":
            beat = 1.5
        elif difficulty == "Normal":
            beat = 1.0
        elif difficulty == "Hard":
            beat = 0.5
            
        
        l = LED_Controller()
        
        if song != "Test":
            l.countdown(beat)
        else:
            l.testStrip(beat)
        
        if song == "Four Chords":
            self.fourChords(beat)
        
        
    
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
        
        m.AssignToGrid([0,0,0,0,0,0])

