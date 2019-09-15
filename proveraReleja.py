import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)         #ventilator
GPIO.setup(27,GPIO.OUT)          #pumpa za vodu
GPIO.setup(25,GPIO.OUT)          #prozor gore
GPIO.setup(8,GPIO.OUT)           #prozor dole 
GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)            #prekidac gore
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)           #prekidac dole


while True:



    if GPIO.input(8):

        print ("PROZOR DOLE ISKLJUCEN")

    else:

        print ("PROZOR DOLE UKLJUCEN")

    if GPIO.input(25):

        print ("PROZOR GORE ISKLJUCEN")


    else:

        print ("PROZOR GORE UKLJUCEN")



    if GPIO.input(24):

        print ("VENTILATOR ISKLJUCEN")


    else:

        print ("VENTILATOR UKLJUCEN")

    if GPIO.input(27):

        print ("PUMPA ISKLJUCEN")
        


    else:

        print ("PUMPA UKLJUCEN")
        



    if GPIO.input(6):

        print ("PROZOR JE OTVOREN")


    else:

        print ("PROZOR NIJE OTVOREN")


    if GPIO.input(12):

        print ("PROZOR JE ZATVOREN")
        print ("------------------------------------")
        time.sleep(1)

    else:

        print ("PROZOR NIJE ZATVOREN")

        print ("------------------------------------")
        time.sleep(1)
