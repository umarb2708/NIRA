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
import os

def initialize():
    #This Function for initialize PI when Start Up  or Restart
    val={
            "status":0,
            "init":0,
            "pid":0,
            "tty":"0",
            "sleep":0,
            "adb":0    
            }

    st="-------Welcome to the world of AI Next Generation computers-----\n"
    f.out.txt_out(st,'011')
    st="Hi "+f.dt.wishme()+" sir. Please wait while initial check going on"
    f.out.txt_out(st,'100')
    #-----------------------All the Initialisation done here-----------------------------------------
    f.db.del_cmd_entries() #delete recent commands table
    f.db.del_cmd() #delete recent commands table
    cmd="rm -rf output_log.log"
    out=os.popen(cmd).read()[:-1]

    val["adb"]=f.adb.connect_android()  #initialize Android
    val["pid"]=f.user.curr_pid()
    val["tty"]=f.user.get_tty().replace("/dev/pts/","")
    val["status"]=1
    val["init"]=1
    print (val)
    
    f.db.update_hira_info(val)
    #-----------------------------------------------------------------------------------------------
    time.sleep(10)
    str="Hi I am Hi ra . Human Intelligent Robo Assistant. Command me preceeding with hi ra"
    f.out.txt_out(str,"111")

    f.db.insert_cmd_executed("initialisation","1")#insert init done to DB

