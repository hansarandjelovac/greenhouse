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
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)           #anemometar 

#iskljucujem sve releje na pocetku programa

GPIO.output(24,1)
GPIO.output(27,1)
GPIO.output(8,1)
GPIO.output(25,1)



def motorDole():

    if GPIO.input(12):
        #print("!!!!! prozor je ZATVOREN !!!!!")
        GPIO.output(8,1)
        #time.sleep(0.2)
        f = open("/home/pi/v1.0/prozorStanje.txt", "w")
        f.write("Prozor je ZATVOREN")
        f.close()



    else: 

        GPIO.output(8,0)
        GPIO.output(25,1)
        print("zatvaram prozor")
        #time.sleep(0.2)



def motorGore():

    if GPIO.input(6):
        #print("!!!!!!prozor je OTVOREN !!!!!!")
        GPIO.output(25,1)
        #time.sleep(0.2)
        f = open("/home/pi/v1.0/prozorStanje.txt", "w")
        f.write("Prozor je OTVOREN")
        f.close()

    else:

        GPIO.output(25,0)
        GPIO.output(8,1)
        print("otvaram prozor")
        #time.sleep(0.2)



#while True:

 #   motorGore()
 #   time.sleep(0.5)
#
