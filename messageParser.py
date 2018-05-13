class messageParser():
    def messageParse(self, payload):
        
        info = payload.split("@");
        song = info[0]
        difficulty = info[1]
        
        print song
        print difficulty
        
        return [song, difficulty]
        
        
