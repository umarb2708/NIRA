#Module for TEXT to Speech
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 130)     # setting up new voice rate
engine.setProperty('volume',1.0)

def speak(text):
    engine.say(text)
    print ("Speaking "+text)
    engine.runAndWait()

