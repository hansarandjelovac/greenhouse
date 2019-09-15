#!/usr/bin/python
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import os


def merenje():

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print 'Temperatura je: {0:0.1f} C  a vlaznost vazduha je: {1:0.1f} %'.format(temperature, humidity)

    f = open("/home/pi/v1.0/temp.txt", "w")
    f.write(str(temperature))
    f.close()



while True:

    merenje()
