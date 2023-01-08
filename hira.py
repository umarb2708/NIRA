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
count=0

class startExecution(object):
    def __init__(self, interval=1):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        global count
        while True:
            # More statements comes here
            mPkg.exe.startExecution()
            time.sleep(self.interval)

mPkg.init.initHira()
tr = startExecution()
print("Initialisation Completed")



#-----------------------------------------------------------
#               MAIN LOGIC
#-----------------------------------------------------------
while 1:
    mPkg.inp.insertCmd()
    time.sleep(10)
    
