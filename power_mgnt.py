#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
# This handles the power management request like sleep,reboot,shutdown
#==============================================================================================================
import os
import import_file as f




def shut_down(command):
    val={
            "status":0,
            "init":0,
            "pid":0,
            "tty":"0",
            "sleep":1,
            "adb":0    
            }
    say="power off requested. please wait saving all configuration."
    f.out.txt_out(say,'111')
    f.db.update_hira_info(val)
    cmd="sudo shutdown -h now"
    out=os.popen(cmd).read()[:-1]
    return 1
    
def reboot(command):
    val={
            "status":0,
            "init":0,
            "pid":0,
            "tty":"0",
            "sleep":1,
            "adb":0    
            }
    say="restart requested. please wait saving all configuration."
    f.out.txt_out(say,'111')
    f.db.update_hira_info(val)
    cmd="sudo reboot"
    out=os.popen(cmd).read()[:-1]
    return 1

def wake_sleep(command):
    sleep=0;
    say='Its a good sleep'
    out='Ready to execute'
    if 'wakeup' in command or 'wake' in command :
        sleep=0
    else:
        say='going to sleep. Bye'
        out='sleep mode activated'
        sleep=1
    val=f.db.get_hira_info()
    val["sleep"]=sleep
    f.db.update_hira_info(val)
    f.out.txt_out(say,'100')
    f.out.txt_out(out,'011')
    return 1

