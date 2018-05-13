import time

from neopixel import *

import argparse
import signal
import sys

def signal_handler(signal, frame):
    colorWipe(strip, Color(0,0,0))
    sys.exit(0)

def  opt_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
    if args.c:
        signal.signal(signal.SIGINT, signal_handler)
        
# LED Strip Configurations
LED_COUNT      = 30      # Number of LED pixels
LED_PIN        = 18      # GPIO pin connected to strip
LED_FREQ_HZ    = 800000  # LED signal freq. in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal
LED_BRIGHTNESS = 200   
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0	 # set to 1 for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB # Strip type and colour ordering

#Process Arguments
opt_parse()



#Create NeoPixel object with config above
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
# Initialize the library (must be called once before other functions)
strip.begin()

class LED_Controller():
    
    def pushArrToLEDS(self, arrOfLEDPositions):            
        color = Color(0,0,0) #default color (off)
        
        brightness = 10
        
        RED = Color(brightness,0,0)
        RG = Color(brightness/2,brightness/2,0)
        GREEN = Color(0,brightness,0)
        GB = Color(0,brightness/2,brightness/2)
        BLUE = Color(0,0,brightness)
        RB = Color(brightness/2,0,brightness/2)
        
        # Assigns each string a specific colour
        StringColor = { 0:RED,1:RG,2:GREEN,3:GB,4:BLUE,5:RB,
                          6:RB,7:BLUE,8:GB,9:GREEN,10:RG,11:RED,
                          12:RED,13:RG,14:GREEN,15:GB,16:BLUE,17:RB,
                          18:RB,19:BLUE,20:GB,21:GREEN,22:RG,23:RED,
                          24:RED,25:RG,26:GREEN,27:GB,28:BLUE,29:RB}
        
        for i in range(0,LED_COUNT): #clear LEDs
            strip.setPixelColor(i, color)
       
       
        for i in arrOfLEDPositions:
            strip.setPixelColor(i-1, StringColor[i-1])
            
        #for i in range(0,30):
            #strip.setPixelColor(i, StringColor[i])
        strip.show() #pushes changes to LED
        print "========="
    #adjusts brightness based on light sensor reading
    def countdown(self, beat):
        brightness = 10
        RED = Color(brightness, 0, 0)
        YELLOW = Color(brightness/2, brightness/2,0)
        GREEN = Color(0,brightness,0)
        
        for i in range(0,30):
            strip.setPixelColor(i, RED)
        strip.show()
        time.sleep(beat)
        for i in range(0,30):
            strip.setPixelColor(i, YELLOW)
        strip.show()
        time.sleep(beat)
        for i in range(0,30):
            strip.setPixelColor(i, GREEN)
        strip.show()
        time.sleep(beat)
        
    def testStrip(self, beat=1.5):
        brightness = 10
        
        RED = Color(brightness,0,0)
        RG = Color(brightness/2,brightness/2,0)
        GREEN = Color(0,brightness,0)
        GB = Color(0,brightness/2,brightness/2)
        BLUE = Color(0,0,brightness)
        RB = Color(brightness/2,0,brightness/2)
        
        OFF = Color(0,0,0)
        
        for i in range(0,30):
            strip.setPixelColor(i, RED)
        strip.show()
        time.sleep(beat)
        for i in range(0,30):
            strip.setPixelColor(i, RG)
        strip.show()
        time.sleep(beat)
        for i in range(0,30):
            strip.setPixelColor(i, GREEN)
        strip.show()
        time.sleep(beat)
        for i in range(0,30):
            strip.setPixelColor(i, GB)
        strip.show()
        time.sleep(beat)
        for i in range(0,30):
            strip.setPixelColor(i, BLUE)
        strip.show()
        time.sleep(beat)
        for i in range(0,30):
            strip.setPixelColor(i, RB)
        strip.show()
        time.sleep(beat)
        for i in range(0,30):
            strip.setPixelColor(i, OFF)
        strip.show()
        
            
            
            
            
            