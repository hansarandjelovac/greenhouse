import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def pocetak():
    with open("brojanje.txt","r")as fajl:
        data = int(fajl.read())
        kmh = data*2.26/5 
    with open("kisaStatus.txt","r") as k:
        kisa = k.read()

    with open("pumpa.txt","r") as p:
        pumpa = p.read()

    with open("prozorStanje.txt","r") as prozor:
        prozorStanje = prozor.read()


    return ("BRZINA VETRA JE\n " + str(kmh)+"KM/h" + "<br/> <br/> <br/>STATUS PADAVINA:" +str(kisa) + "<br/> <br/> <br/> STATUS ZEMLJE: " + str(pumpa) + "<br/> <br/> <br/>:" + str(prozorStanje))


if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))

