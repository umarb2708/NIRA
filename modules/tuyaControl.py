import tinytuya
import time
import random
from modules import modulePkg as mPkg

debugModule=0

#tinytuya.set_debug(True)  # use tinytuya.set_debug(True,False) for non-ANSI color terminal

def connectDevice(tuyaDevID,tuyaIP , tuyaLocalKey, tuyaVersion):
    dev = tinytuya.BulbDevice(tuyaDevID,tuyaIP , tuyaLocalKey)
    dev.set_version(tuyaVersion)
    return dev;
# Show status of device
def checkStatus(dev):
    status = dev.status()
    return status 
def setColour(colour,dev):
    if colour == 0:
        dev.set_colour(255, 0, 0)
    elif colour == 1:
        dev.set_colour(0, 255, 0)
    elif colour == 2:
        dev.set_colour(0, 0, 255)
    else:
        dev.set_white(1000, 778)



def setBrightness(brightness,dev):
    dev.set_brightness_percentage(brightness)

def setClrTemp(colourtemp,dev):
    dev.set_colourtemp_percentage(colourtemp)

def turnON(dev):
    #dev.set_white(1000, 778)
    dev.turn_on()

def turnOFF(dev):
    dev.turn_off()

def fetchTuyaDev(tuyaIP):
    devData={}
    sqlCondition="WHERE tuyaIP='"+tuyaIP+"'"
    rows=mPkg.db.SelectData("tuya_details","*",sqlCondition)
    for x in rows:
        devData["id"]=x[0]
        devData["tuyaIP"]=x[1]
        devData["devID"]=x[2]
        devData["devKey"]=x[3]
        devData["devVersion"]=x[4]
    print(devData)
    return devData


def ControlTuya(tuyaIP,turnOn,colour,brightness,clrTemp):
    retVal=""
    devData=fetchTuyaDev(tuyaIP)
    d=connectDevice(devData["devID"],devData["tuyaIP"],devData["devKey"],devData["devVersion"])
    st=checkStatus(d)
    if 'Error' in st.keys():
        retVal=0
    elif turnOn==1 :
        setColour(colour,d)
        setBrightness(brightness,d)
        setClrTemp(clrTemp,d)
        turnON(d)
    else:
        turnOFF(d)

        


if debugModule==1:
    ControlTuya('192.168.15.150',1,'white','100.00','77.8')


    
## Show status of device
#data = d.status()
#print('\nCurrent Status of Bulb: %r' % data)
#
## Set to full brightness warm white
#print('\nWarm White Test')
#d.set_white()
#time.sleep(1)
#
## Power Control Test
#print('\nPower Control Test')
#print('    Turn off lamp')
#d.turn_off()
#time.sleep(1)
#print('    Turn on lamp')
#d.turn_on()
#time.sleep(1)
#
## Random Color Test
#print('\nRandom Color Test')
#for x in range(10):
#    r = random.randint(0, 255)
#    g = random.randint(0, 255)
#    b = random.randint(0, 255)
#    print('    RGB (%d,%d,%d)' % (r, g, b))
#    d.set_colour(r, g, b)
#    time.sleep(1)
#
#d.turn_off()
