from gtts import gTTS
import os
def speak(txt):
    tts = gTTS(txt)
    tts.save('hello.mp3')
    cmd="omxplayer hello.mp3"
    out=os.popen(cmd).read()[:-1]
