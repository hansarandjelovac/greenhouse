
#!/usr/bin/python
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
GPIO.setup(6,GPIO.IN)            #prekidac gore
GPIO.setup(12,GPIO.IN)           #prekidac dole
GPIO.setup(13,GPIO.IN)           #anemometar


GPIO.output(24,1)
GPIO.output(27,1)
GPIO.output(8,1)
GPIO.output(25,1)

