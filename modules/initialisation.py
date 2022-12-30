#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
# This modules used for initialisation of HIRA at startup
#==============================================================================================================

from modules import modulePkg as mPkg
#To print the output of each module status according to priority
log_en=0    #0:disable 1:enable
log_priority=1 #1:high 2:medium 3:low (low will print all high,medium,low, medium will print all medium and high, high will print only high)
#To define input/output mode
inputMode=0 #0:Terminal 1:speech 2:serial com
outputMode=1 #0:TTS 1:terminal 2:serial com

#Enabling some features
adb_en=0 # Enable ADB 0:disable 1:enable
serialCom_en=0 #Enable Serial communication 0:disable 1:enable





if log_en==1:
    mPkg.logs.createLogFile()
    
        



