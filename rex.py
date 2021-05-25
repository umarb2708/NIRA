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

def initialize():
  #This Function for initialize PI when Start Up
  f.ser.ser_write("Welcome to the world of AI\n")
  f.ser.ser_write("Inital Checks going on. Please  wait\n")
  f.tts.speak("Hi "+f.dt.wishme()+". Please wait while initial check going on")
  f.db.insert_login_details(f.user.get_user(),f.user.get_Host_name_IP())#Login details to Database
  f.ser.ser_write("New Login Name:"+f.user.get_user()+"   IP address:"+f.user.get_Host_name_IP()+"\n")#Login details to Serial
  f.tts.speak("Welcome to the world of AI. I am rex your companion. Tell your commands preceeding with rex")


def exec_commands():
    global sleep
    while sleep==0:
        commands=cmd.get_commands()
        print("First CMD:"+commands+"   Has "+str(len(commands)))
        if "hey rex" in commands:
            if(len(commands)<=10):#if Previous command is only wake word
                f.tts.speak("Hi sir.")  
                f.ser.ser_write("Hi. Please type your command") 
                print("Hi Sir")         
                commands=cmd.get_commands()
            x=f.db.get_commands(commands)
            print (x)
            commands=commands.replace("\n","")
            result=eval("f."+x+"('"+commands+"')")
            res=result.replace("::OK","").replace("::FAIL","")
            f.ser.ser_write(res+"\n")
            f.tts.speak(res)
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



#-----------------------------------------------------------
#               MAIN LOGIC
#-----------------------------------------------------------
initialize()
thread1 = threading.Thread(target=exec_commands)
#thread2 = threading.Thread(target=handle_db_data)
thread1.start()
#thread2.start()
    
