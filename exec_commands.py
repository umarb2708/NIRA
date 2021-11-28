#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
# This modules executes the commands recieved from various input methods
#==============================================================================================================

import import_file as f
import os

wake_word=["Hira","hira","hey hira","Hey Hira","Hi Ra","hi ra","hey darling","wakeup hira"]
rcvd_cmd="no commands"

def check_wake_word(cmd):
    wakeup=0
    global rcvd_cmd
    for wrd in wake_word:
        if wrd in cmd:
            cmd.replace(wrd,"").replace("\n","")
            rcvd_cmd=cmd
            wakeup=1
            break
    return wakeup

def exec_commands(command):
    if (check_wake_word(command)):
        cmd=f.db.search_cmd(rcvd_cmd)

        result=eval("f."+cmd["cmd"]+"('"+rcvd_cmd+"')")
        if result :
           f.out.txt_out("Command Successfull",6)
        else:
           f.out.txt_out("Internal error occured",6)


        
        
