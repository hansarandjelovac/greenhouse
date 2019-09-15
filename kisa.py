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


#GPIO.output(24,1)
#GPIO.output(27,1)
#GPIO.output(8,1)
#GPIO.output(25,1)


def kisaMerenje():

    if GPIO.input(18):
        f = open("/home/pi/v1.0/kisa.txt", "w")
        f.write("1")
        f.close()
        
    else:
        f = open("/home/pi/v1.0/kisa.txt", "w")
        f.write("0")
        f.close()
        



while True:

    kisaMerenje()
    time.sleep(5)
