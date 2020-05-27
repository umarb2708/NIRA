import os
def speak(st):
    os.system("gtts-cli "+st+" --output sound.mp3")
    os.system("play sound.mp3 ")
