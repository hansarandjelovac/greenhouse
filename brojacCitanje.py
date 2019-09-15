def brojanje():

    with open("/home/pi/v1.0/obrtaji.txt","r") as o:
        vetar =  int(o.readline())
        return vetar

