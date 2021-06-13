#!/usr/bin/env python3

import speech_recognition as sr
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"SPC DEBUG speech:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        #speak("Say that again Please...")
        return "None"
    return query
#print(takeCommand())
