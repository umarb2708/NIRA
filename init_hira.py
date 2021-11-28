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
    global inpt
    #This Function for initialize PI when Start Up  or Restart
    str="-------Welcome to the world of AI Next Generation computers-----\n"
    f.out.txt_out(str,1,1,0)
    str="Hi "+f.dt.wishme()+" sir. Please wait while initial check going on"
    f.out.txt_out(str,1,1,1)
    #-----------------------All the Initialisation done here-----------------------------------------
    res=f.db.insert_login_details(f.user.login_details())#Login details to Database
    f.out.txt_out(res,1,1,0)
    f.db.del_cmd_entries() #delete recent commands table
    f.adb.connect_android()  #initialize Android
    #-----------------------------------------------------------------------------------------------
    time.sleep(10)
    str="Hi I am Hi ra . Human Intelligent Robo Assistant. Command me preceeding with hi ra"
    f.out.txt_out(str,1,1,1)

