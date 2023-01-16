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
class hiraWarning(object):
    def __init__(self, interval=20):
        self.interval = interval
        self.exeThread = threading.Thread(target=self.run, args=())
        self.exeThread.daemon = True
        self.controlThread()

    def controlThread(self):
        self.exeThread.start()


    def run(self):
        while True:
            # More statements comes here
            mPkg.mon.checkWarnings()
            time.sleep(self.interval)



mPkg.init.initHira()

warnObj = hiraWarning()
#inpThread=startInput()
print("Initialisation Completed")



#-----------------------------------------------------------
#               MAIN LOGIC
#-----------------------------------------------------------
while 1:
    mPkg.inp.insertCmd()
    mPkg.exe.startExecution()
    #time.sleep(10)
    #while mPkg.config.ExecutionInProgress == 1:
    #    time.sleep(10)
    
