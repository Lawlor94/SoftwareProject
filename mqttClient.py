import json
import paho.mqtt.client as mqtt
import random
import time
import threading
import sys
from grovepi import *

from test import test

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
        #mp.messageParse(message.payload)
    thread = threading.Thread(target = mp.messageParse, args = (message.payload, ))
    thread.start()
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
    


