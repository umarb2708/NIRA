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
        if word in cmd:
            cmd.replace(wrd,"").replace("\n","")
            rcvd_cmd=cmd
            wakeup=1
            break
    return wakeup

def exec_commands(command):
    if (check_wake_word(command)):
        cmd=f.db.search_cmd(rcvd_cmd)
        
        







def exec_commands(command):
    global sleep,inpt
    while sleep==0:
        commands=f.cmd.get_input()
        if "Hira" in commands or "hey darling" in commands or "hira" in commands :
            commands.replace("Hira","").replace("hey darling","").replace("hira","")
            if(len(commands)<=4):#if Previous command is only wake word
                str="yes sir."
                f.out.txt_out(str,1,1,1)
                commands=f.cmd.get_input()#getting input
            x=f.db.search_cmd(commands)#searching DB commands
            commands=commands.replace("\n","")
            f.out.txt_out("cmd:"+commands+"  exec:"+x["cmd"],1,1,0)
            result=eval("f."+x["cmd"]+"('"+commands+"')")
            res=result.replace("::OK","").replace("::FAIL","")
            f.out.txt_out(res,1,1,1)
            if "::OK" in result :
                f.db.insert_cmd_executed(x["kw"],1)
            else :
                f.db.insert_cmd_executed(x["kw"],0)
            if "reboot" in res:
                sleep=1
                lnx_cmd="sudo reboot"
                os.system(lnx_cmd)
            elif "shut down" in res:
                lnx_cmd="sudo shutdown -h now"
                os.system(lnx_cmd)
        else:
            f.out.txt_out(commands,1,1,1)

