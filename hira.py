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
import import_file as f
import time
import threading
class startExecution(object):
    def __init__(self, interval=1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            # More statements comes here
            f.cmd.start_exe()
            time.sleep(self.interval)

#Variables
init_done=0
f.init.initialize()
tr = startExecution()


#-----------------------------------------------------------
#               MAIN LOGIC
#-----------------------------------------------------------
while 1:
    f.inp.insert_cmd()
    time.sleep(1)
    
