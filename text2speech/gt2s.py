#!/usr/bin/python
def speak(st,voice,OS):
    tts = voice(st)
    tts.save('file.mp3')
    OS.system("play file.mp3")
