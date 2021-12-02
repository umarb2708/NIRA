#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
# This module is intented to initialize HIRA server on startup 
#==============================================================================================================

import import_file as f
import time

def initialize():
    #This Function for initialize PI when Start Up  or Restart

    st="-------Welcome to the world of AI Next Generation computers-----\n"
    f.out.txt_out(st,4)
    st="Hi "+f.dt.wishme()+" sir. Please wait while initial check going on"
    f.out.txt_out(st,5)
    #-----------------------All the Initialisation done here-----------------------------------------
    f.db.del_cmd_entries() #delete recent commands table

    f.adb.connect_android()  #initialize Android
    
    
    #-----------------------------------------------------------------------------------------------
    time.sleep(10)
    str="Hi I am Hi ra . Human Intelligent Robo Assistant. Command me preceeding with hi ra"
    f.out.txt_out(str,1,1,1)

    f.db.insert_cmd_executed("initialisation","1")#insert init done to DB

