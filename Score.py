class Score():
    
    
    def getScore(self, song, difficulty):
        
        score = 0
        
        if song == "Four Chords":
            score += 1000
            
        if difficulty == "Easy":
            score += 600
        elif difficulty == "Normal":
            score += 1200
        elif difficulty == "Hard":
            score += 2400
            
        return score