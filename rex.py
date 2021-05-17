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
import train_rex as t
import commands as cmd
#Variables
commands=""
sleep=0


#Initial Setup
f.ser.ser_write("Welcome to the world of AI\n")
f.ser.ser_write("Inital Checks going on. Please  wait\n")
f.tts.speak("Hi "+f.dt.wishme()+". Please wait while initial check going on")
#t.train_rex()#for Testing purpose

f.db.insert_login_details(f.user.get_user(),f.user.get_Host_name_IP())#Login details to Database
f.ser.ser_write("New Login Name:"+f.user.get_user()+"   IP address:"+f.user.get_Host_name_IP()+"\n")#Login details to Serial
f.tts.speak("Welcome to the world of AI. I am rex your companion. Tell your commands preceeding with rex")

while !sleep:
    commands=cmd.get_commands()
    if "rex" in commands:
        x=f.db.get_commands(commands)
        print (x)
        commands=commands.replace("\n","")
        res=eval("f."+x+"('"+commands+"')")
        print (res)
