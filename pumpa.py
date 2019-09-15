#!/usr/bin/python

#GOTOVO

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
GPIO.setup(13,GPIO.IN)           #anemometar


def ukljucivanjePumpe():
    
    if GPIO.input(17):
        print("zemlja je suva")
        GPIO.output(27,0)
        f = open("/home/pi/v1.0/pumpa.txt", "w")
        f.write("Zemlja je suva")
        f.close()
    
    else:
        print("zemlja je vlazna")
        GPIO.output(27,1)
        f = open("/home/pi/v1.0/pumpa.txt", "w")
        f.write("Zemlja je vlazna")
        f.close()


while True:

    ukljucivanjePumpe()
    time.sleep(1)
