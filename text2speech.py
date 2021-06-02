#Module for TEXT to Speech
import pyttsx3
import sys
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)     # setting up new voice rate
engine.setProperty('volume',1.0)
engine.setProperty('age', 20)
def check_voices():
    voices = engine.getProperty('voices')
    for voice in voices:
        engine.setProperty('voice', voice.id)
        print ("VOICE:"+voice.id)
        engine.say('I am rex')
    engine.runAndWait()
def speak(text):
    engine.say(text)
    print ("Speaking :"+text)
    engine.runAndWait()



speak(sys.argv[1])
