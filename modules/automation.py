#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
#Module Name: automaton.py
#Module description:Smart Home module to control device function such as on/off, speed, colour, brightness
#==============================================================================================================

import tinytuya # Library to controll tuya device
from modules import modulePkg as mPkg

bulb_list=["bulb","light"]
lamp_list=["lamp","led","L E D", "LED"]
fan_list=["fan","FAN","F A N"]
clr_list=["red","blue","green"]
roomList=["master bedroom","second bedroom","third bedroom","office room","kitchen","stair case"]
floorList=["ground","first","top"]

clr_param={
        "red":0,
        "green":1,
        "blue":2
        }


def turnON(command):
    DevAction={
            "id":0,
            "status":0
            }
    devDet=findDev(command)
    DevAction["id"]=devDet["id"]
    DevAction["status"]=1
    mPkg.db.UpdateData("home_automation",DevAction,"id = "+str(DevAction["id"]))

    if devDet["isTuya"] == '1' :
        mPkg.tuya.ControlTuya('192.168.15.150',1,4,100,77.5)
    return 1

def turnOFF(command):
    DevAction={
            "id":0,
            "status":0
            }
    devDet=findDev(command)
    DevAction["id"]=devDet["id"]
    DevAction["status"]=0
    mPkg.db.UpdateData("home_automation",DevAction,"id = "+str(DevAction["id"]))
    if devDet["isTuya"] == '1' :
        mPkg.tuya.ControlTuya('192.168.15.150',0,4,100,77.5) 
    return 1

def changeColour(command):
    DevAction={
            "id":0,
            "param":0
            }
    devDet=findDev(command)
    devDet["param"]=getColour(command);
    DevAction["id"]=devDet["id"]
    DevAction["param"]=devDet["param"]
    mPkg.db.UpdateData("home_automation",DevAction,"id = "+str(DevAction["id"]))
    return 1

def adjustBrightness(command):
    DevAction={
            "id":0,
            "brightness":0
            }
    devDet=findDev(command)
    devDet["brightness"]=getBrightness(command);
    DevAction["id"]=devDet["id"]
    DevAction["brightness"]=devDet["brightness"]
    mPkg.db.UpdateData("home_automation",DevAction,"id = "+str(DevAction["id"]))    

def getColour(command):
    clr=4
    for x in clr_list:
        if x in command:
            clr=int(clr_list.index(x))
    #if no info about room given in command
    if clr == 4:
        mPkg.out.putOutput("Which colour")
        clr=int(mPkg.inp.getInput("colour"))

    return clr
def getBrightness(command):
    bright=100
    x=command.split("brightness")
    if len(x[1]) < 3:
        mPkg.out.putOutput("what percentage")
        x[1]=mPkg.inp.getInput("percentage")
        #if x[1] == 'full' # to be define
    bright=mPkg.parser.toInt(x[1])
    return bright

def findDev(command):
    devDetails={
            "id"        :0,
            "room"      :"master bedroom",
            "floor"     :"first",
            "component" :"no",
            "isTuya"    :0,
            "TuyaIP"    :"",
            "status"    :0,
            "param"     :0,
            "brightness":100

            }
    devDetails["component"]=findComponent(command)
    roomFloor=findRoomFloor(command)
    devDetails["room"]=roomFloor[0]
    devDetails["floor"]=roomFloor[1]
    #devDetails["id"]=fetchDevID(devDetails)
    fetchDevID(devDetails)

            
    return devDetails




def findComponent(command):
    component=""
    for dev in bulb_list:
        if dev in command and component == "" :
            component="light"
            break
    for dev in fan_list:
        if dev in command and component == "" :
            component="fan"
            break
    for dev in lamp_list:
        if dev in command and component == "" :
            component="night lamp"
            break

    return component

def findRoomFloor(command):
    roomData=["",""]
    # check available rooms in command
    for rm in roomList:
        if rm in command:
            print("room found")
            roomData[0]=rm
            break
    # check available floor in command
    for floor in floorList:
        if floor in command:
            print("floor found")
            roomData[1]=floor
            break
    #if no info about room given in command
    print ("room Data 0:"+str(roomData[0]))
    if roomData[0] == "":
        mPkg.out.putOutput("Which room")
        roomData[0]=mPkg.inp.getInput("room")
        #if room input is current room
        if "current room" in roomData[0]:
            #TBD get room and floor details from 
            #current position of HIRA
            #For debug enabling default value
            roomData[0]="third bedroom"
            roomData[1]="first"
    #if no floor information
    print ("room Data 1:"+str(roomData[1]))
    if roomData[1] == "":
        mPkg.out.putOutput("Which floor")
        roomData[0]=mPkg.inp.getInput("floor")
    return roomData

def fetchDevID(devDetails):
    Devid=0
    sqlCondition="WHERE component = '"+devDetails["component"]+"' AND room = '"+devDetails["room"]+"' AND floor = '"+devDetails["floor"]+"'"  
    rows=mPkg.db.SelectData("home_automation","id,isTuya,TuyaIP,status,param,brightness",sqlCondition)
    for x in rows:
        devDetails["id"]=x[0]
        devDetails["isTuya"]=x[1]
        devDetails["TuyaIP"]=x[2]
        devDetails["status"]=x[3]
        devDetails["param"]=x[4]
        devDetails["brightness"]=x[5]

    return Devid

   

