#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
#Module Name: outputData.py
#Module description: To produce out from HIRA via terminal or serial monitor or voice output
# MODE:0->voice(by default) 1:Terminal input 2:serial monitor input
#==============================================================================================================
from gtts import gTTS
import os
from modules import modulePkg as mPkg
mode=mPkg.init.outputMode


def text2speech(st):
    tts = gTTS(st)
    tts.save('logs/hello.mp3')
    cmd="mpg321 logs/hello.mp3"
    out=os.popen(cmd).read()[:-1]   

def putOutput(st):
    if mode ==0:
        text2speech(st)
    elif mode==1:
        print(st)
