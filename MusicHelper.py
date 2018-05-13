from LED_Controller import LED_Controller


class MusicHelper():
    def AssignToGrid(self, noteList): #pass in list with 6 elements. Each item represents where to light a specific string. -1 means to not light that string at all.

        noteList.reverse() #reverses list to make the input more intuitive to how a guitars strings are ordered
        
        string_map = [[1,12,13,24,25],
                      [2,11,14,23,26],
                      [3,10,15,22,27],
                      [4,9,16,21,28],
                      [5,8,17,20,29],
                      [6,7,18,19,30]] #2D list of all string positions
        
        LEDs_to_light = []
        
        for i in range(0, len(noteList)): #for each item in notelist
            if noteList[i] != 0: # -1 means the string is not used
                noteToAppend = string_map[i][noteList[i]-1]
                LEDs_to_light.append(noteToAppend)
                
        l = LED_Controller()
        l.pushArrToLEDS(LEDs_to_light)
        
  
'''  
AssignToGrid([3,2,0,0,0,3]) # G Maj
AssignToGrid([0,3,2,0,1,0]) # C Maj
AssignToGrid([0,0,2,2,1,0]) # A min
AssignToGrid([0,2,2,1,0,0]) #E Maj
# STRING ORDER: e A D G B E'''