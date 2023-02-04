#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
#Module Name: faceRecognise.py
#Module description: To identify a person face in database
#==============================================================================================================
import time
from modules import modulePkg as mPkg
moduleLogPriority=1

def detect(command):
    if checkCamState():#Camera enabled or not
        if captureFace():#if capture success
            

    else:
        print("Cam MCU not connected. Please check")
        mPkg.out.putOutput("Sorry Camera not enabled")
    return 1
    
def checkCamState(): 
    camEn=0
    dbData=mPkg.db.SelectData('hiraSubMCU','*','WHERE id = 1')
    for x in dbData:
        if x[2] == '1':
            camEn=1
        else:
            camEn=0
    return camEn

def captureFace():
    captured=0
    subMcuVal={'hiraCam':'capture'}
    mPkg.out.putOutput("Taking Picture. Please be steady")
    print("Taking Picture")
    mPkg.db.UpdateData("hiraSubMCU",subMcuVal,"id = 2")
    time.sleep(20)
    dbData=mPkg.db.SelectData('hiraSubMCU','*','WHERE id = 2')
    for x in dbData:
        if x[2] =="SUCCESS":
            captured=1
        else :
            print("Error occured on capturing")
            captured=0
    return captured


    
