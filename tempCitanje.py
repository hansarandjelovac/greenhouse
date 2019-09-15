#!/usr/bin/python


#GOTOVO

def temperatura():

    with open("/home/pi/v1.0/temp.txt","r") as f:
        temp = float(f.readline())
        temp =  int(temp)
        return temp

