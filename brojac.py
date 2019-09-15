#!/usr/bin/python
from motor import motorDole, motorGore
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)         #ventilator
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)          #senzor kise
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)           #senzor vlaznosti zemlje
GPIO.setup(27,GPIO.OUT)          #pumpa za vodu
GPIO.setup(25,GPIO.OUT)          #prozor gore
GPIO.setup(8,GPIO.OUT)           #prozor dole
GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)            #prekidac gore
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)           #prekidac dole
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)           #anemometar


global obrtaji
obrtaji = 0

def brojanje(brojanje):

    global obrtaji
    obrtaji += 1



GPIO.add_event_detect(13, GPIO.RISING, callback=brojanje, bouncetime=220)

def test():
    while True:
        global obrtaji
        time.sleep(5)

        f = open("/home/pi/v1.0/obrtaji.txt", "w")
        f.write(str(obrtaji))
        f.close()

        obrtaji = 0

while True:    # PROVERI OVO

    test()
