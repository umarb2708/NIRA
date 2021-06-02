from gtts import gTTS
import os
def speak(txt):
    tts = gTTS(txt)
    tts.save('hello.mp3')
    os.system("omxplayer hello.mp3")
