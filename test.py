import json
import paho.mqtt.client as mqtt
import random
import time
import threading
import sys

class test:
    def test(self):
        port = "13346"
        broker_address = "m23.cloudmqtt.com"
        user = "niutmqgn"
        password = "p4WLAjJeGsLX"

        mqttc = mqtt.Client("GuitarClient", clean_session=False)
        mqttc.username_pw_set(user, password)
        mqttc.connect(broker_address, port, 60)
        mqttc.loop_start()
        
        
    
        t = time.time()
        toPublish = "Published at: "+str(t)
        mqttc.publish("test", payload=toPublish)