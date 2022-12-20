#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
# HIRA is a python based Humanoid robot. This robot will do all kind of human activities and also can be used 
# as a assistant instead of all other available AI in the market.
#==============================================================================================================

#import Files and handles
import time
import threading
from modules import modulePkg as mPkg
def StartExecution():
    print("Starting Execution at "+str(mPkg.date.get_time()))

def getInput():
    print("Time is "+str(mPkg.date.get_time()))
    if (mPkg.date.get_hour()>15):
        print("Good Afternoon yaaar")
    elif(mPkg.date.get_hour()<15):
        print("Arey its morning")


startExe=threading.Thread(target=StartExecution(), args=())
getInp=threading.Thread(target=getInput(), args=())
startExe.start
getInp.start


#-----------------------------------------------------------
#               MAIN LOGIC
#-----------------------------------------------------------
while 0:
    f.inp.insert_cmd()
    time.sleep(1)
    
