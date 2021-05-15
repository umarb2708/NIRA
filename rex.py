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

#f.db.insert_login_details(f.user.get_user(),f.user.get_Host_name_IP())
f.tts.speak(eval("f."+wishme))
f.tts.speak("i am rex the robot")
f.tts.speak("please wait for initial configuration")
f.ser.ser_write("How can i help you?")
#f.tts.speak(f.ser.ser_read().decode('UTF-8'))
#t.train_rex()
f.db.check_commands(f.ser.ser_read().decode('UTF-8'))
#while 1:
    
