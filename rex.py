# REX Main Module
#Designed and Developed By UMAR B
import os
import sys
import pyttsx3



#Text to Speech Initialisation
engine = pyttsx3.init()
#voices = engine.getProperty('voices')
##engine.setProperty('voice',voices[0].id)
#print("TTS initialisation complete with voice ID:"+voices[1].id)

def speak(audio):
    engine.say(audio)
    print("speaking:"+audio)
    engine.runAndWait()

#--------------------------------------------------------------
#                     Main code Starts Here
#--------------------------------------------------------------
speak("Hi Umar. Good Night")

