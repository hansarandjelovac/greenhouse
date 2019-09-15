def kisaProvera():

    with open("/home/pi/v1.0/kisa.txt","r") as k:
        kisa = int(k.readline())
        
        if kisa == 1:
            f = open("/home/pi/v1.0/kisaStatus.txt", "w")
            f.write("Kisa pada")
            f.close()
 
            return True

        else:
            f = open("/home/pi/v1.0/kisaStatus.txt", "w")
            f.write("Kisa ne pada")
            f.close()
            return False


