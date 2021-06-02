#==============================================================================================================
#                                      REX The Robot
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
# Rex is a python based Humanoid robot.
#==============================================================================================================

#import Files and handles
import import_file as f
import commands as cmd
import time
import threading
import os
#Variables
commands=""
sleep=0
def txt_out(str,ser,ter,t2s):
    if ser:
        f.ser.ser_write(str)
    if ter:
        print(str)
    if t2s:
        f.tts.speak(str)
def initialize():
    #This Function for initialize PI when Start Up  or Restart
    str="-------Welcome to the world of AI Next Generation computers-----\n"
    txt_out(str,1,1,0)
    str="Hi "+f.dt.wishme()+" sir. Please wait while initial check going on"
    txt_out(str,1,1,1)
    #-----------------------All the Initialisation done here-----------------------------------------
    res=f.db.insert_login_details(f.user.login_details())#Login details to Database
    txt_out(res,1,1,0)
    f.db.del_cmd_entries();
    #-----------------------------------------------------------------------------------------------
    time.sleep(10)
    str="I am online and ready. Please command preceeding with hey rex"
    txt_out(str,1,1,1)
def exec_commands():
    global sleep
    while sleep==0:
        commands=cmd.get_commands()
        if "Hira" in commands:
            if(len(commands)<=10):#if Previous command is only wake word
                str="Hi sir."
                txt_out(str,1,1,1)
                commands=cmd.get_commands()

            x=f.db.get_commands(commands)
            commands=commands.replace("\n","")
            txt_out("cmd:"+commands+"  exec:"+x,1,1,0)
            result=eval("f."+x+"('"+commands+"')")
            res=result.replace("::OK","").replace("::FAIL","")
            txt_out(res,1,1,1)
            if "::OK" in result :
                f.db.insert_cmd_executed(commands,1)
            else :
                f.db.insert_cmd_executed(commands,0)
            if "reboot" in res:
                sleep=1
                lnx_cmd="sudo reboot"
                os.system(lnx_cmd)
            elif "shut down" in res:
                lnx_cmd="sudo shutdown -h now"
                os.system(lnx_cmd)
        else:
            txt_out(commands,1,1,1)
        



#-----------------------------------------------------------
#               MAIN LOGIC
#-----------------------------------------------------------
initialize()
exec_commands()
#thread1 = threading.Thread(target=exec_commands)
##thread2 = threading.Thread(target=handle_db_data)
#thread1.start()
##thread2.start()
