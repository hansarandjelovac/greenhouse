#!/usr/bin/python
import sys
import os
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
from motor import motorGore, motorDole
from kisaCitanje import kisaProvera                 #var true ili false
from brojacCitanje import brojanje           # var vetar
from tempCitanje import temperatura          #var temp
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
# GPIO 4 senzor temperature i vlaznosti vazduha
#iskljucujem sve releje na pocetku programa
GPIO.output(24,1)
GPIO.output(27,1)
GPIO.output(8,1)
GPIO.output(25,1)


while True:

    if kisaProvera() == False and brojanje() <5 and temperatura() >20:

       motorGore()


    else:

       motorDole()

    
