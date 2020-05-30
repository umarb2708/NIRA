import time
def speak(st,py_voice):
    engine=py_voice.init()
    rate = engine.getProperty('rate')
    engine.setProperty('gender', 'female')
    engine.setProperty('voice', 'greek')
    engine.setProperty('rate', rate-20)
    engine.setProperty('age', 10)
    engine.say(st) 
#    engine.say("Thank you, Geeksforgeeks") 
    engine.runAndWait()
    time.sleep(1)

