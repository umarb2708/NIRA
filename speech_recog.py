#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
to=20
# obtain audio from the microphone
r = sr.Recognizer()
def recog_speech(to):
    command=""
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source,timeout=to)
    # recognize speech using Sphinx
    try:
        #print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        command=r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + command)
    except sr.WaitTimeoutError:
        print("Timeout Happened")
        command="couldnt catch you. Tell once more"
    except sr.UnknownValueError:
        print("Hira could not understand audio")
        command="I didnot understand that. Tell once more "
    except sr.RequestError as e:
        print("Recognisaton error; {0}".format(e))
        command="I detected an error in speech recognisation"


