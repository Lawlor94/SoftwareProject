import json
import paho.mqtt.client as mqtt
import random
import time
import threading
import sys
from grovepi import *

from test import test

from Score import Score
from Music import Music
from messageParser import messageParser

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print "Connected to broker"
        
        global Connected
        Connected = True
    else:
        print "Connection failed"

def on_message(client, userdata, message):
    mp = messageParser()
    list = mp.messageParse(message.payload)
    
    song = list[0]
    difficulty = list[1]
    
    m = Music()
    thread = threading.Thread(target = m.playSong, args = (song,difficulty,))
    
    if song != "Test":
        s = Score()
        score = s.getScore(song, difficulty)
        
        mqttc.publish("score", payload=score)

    
    thread.start()
    thread.join()
    
Connected = False # Global variable
port = "13346"
broker_address = "m23.cloudmqtt.com"
user = "niutmqgn"
password = "p4WLAjJeGsLX"

mqttc = mqtt.Client("GuitarClient", clean_session=False)
mqttc.username_pw_set(user, password)
mqttc.on_connect= on_connect #attatch function
mqttc.on_message= on_message

mqttc.connect(broker_address, port, 60)
mqttc.loop_start()

while Connected != True: #wait for connection
    time.sleep(0.1)


mqttc.subscribe("instructions")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print "exiting"
    mqttc.disconnect()
    mqttc.loop_stop()
    


