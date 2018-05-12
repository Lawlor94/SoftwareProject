from Music import Music
from LED_Controller import LED_Controller

class messageParser():
    def messageParse(self, payload):
        m = Music()
        l = LED_Controller()
        if int(payload) == 1:
            
            beat = 0.75
            
            l.countdown(beat)
            while True:
                m.fourChords(beat)