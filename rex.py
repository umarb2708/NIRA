#==============================================================================================================
#                                      REX The Robot
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
# Rex is a python based Humanoid robot.
#==============================================================================================================
import import_file as f
import train_rex as t
wishme="dt.wishme()"

f.db.insert_login_details(f.user.get_user(),f.user.get_Host_name_IP())
f.tts.speak(eval("f."+wishme))
f.tts.speak("i am rex the robot")
f.tts.speak("please wait for initial configuration")
#t.train_rex()

#while 1:
    
