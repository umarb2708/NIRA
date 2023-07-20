#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
# This modules used to log the output of modules
#==============================================================================================================
import os
from modules import modulePkg as mPkg

def createLogFile():
    try:
        os.system("rm -rf logs/module.log")
    except:
        print("Log file not present !!!")

    f=open("logs/module.log","w")
    f.write("=============HIRA Logs=============\n")
    f.close()
def writeLog(strng):
    f=open("logs/module.log","a")
    currTime=mPkg.date.getAlldateTime()
    f.write(currTime+"-->"+strng+"\n")
    f.close()




