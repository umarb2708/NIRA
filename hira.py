#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
# Rex is a python based Humanoid robot.
#==============================================================================================================

#import Files and handles
import import_file as f
import time
import threading
import os
#Variables
commands=""
sleep=0
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
def exec_commands():
    global sleep,inpt
    while sleep==0:
        commands=f.cmd.get_input()
        if "Hira" in commands or "hey darling" in commands or "hira" in commands :
            commands.replace("Hira","").replace("hey darling","").replace("hira","")
            if(len(commands)<=4):#if Previous command is only wake word
                str="yes sir."
                f.out.txt_out(str,1,1,1)
                #commands=cmd.get_voice_cmd()
                commands=f.cmd.get_input()
            x=f.db.search_cmd(commands)
            commands=commands.replace("\n","")
            f.out.txt_out("cmd:"+commands+"  exec:"+x,1,1,0)
            result=eval("f."+x+"('"+commands+"')")
            res=result.replace("::OK","").replace("::FAIL","")
            f.out.txt_out(res,1,1,1)
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
            f.out.txt_out(commands,1,1,1)
        



#-----------------------------------------------------------
#               MAIN LOGIC
#-----------------------------------------------------------
initialize()
exec_commands()
#thread1 = threading.Thread(target=exec_commands)
##thread2 = threading.Thread(target=handle_db_data)
#thread1.start()
##thread2.start()
