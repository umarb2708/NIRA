
#!/usr/bin/python
import sys
import os as OS
from gtts import gTTS as voice#google text to speech
import speech_recognition as sr #voice redognisation
from time import sleep as slp #for delay
from ina219 import INA219 as bat_module#battery status
from Adafruit_CharLCD import Adafruit_CharLCD#lcd display
import pyttsx3 as py_voice #ofline voice

sys.path.append('text2speech')
sys.path.append('voice_recognize')
sys.path.append('alert_system')

import gt2s
import voice_command
import low_battery
import pyt2s

lcd = Adafruit_CharLCD(rs=21, en=20, d4=16, d5=12, d6=7, d7=8,
                       cols=16, lines=2)


class bat_status:
    def __init__(self):
        initialized=0
        self.v=0
        self.i=0
        self.p=0

obj1=bat_status()
#for gtts
gt2s.speak(st,voice,OS)
pyt2syy.speak(st,py_voice)
#for speech recognissation
global voice
voice=voice_command.get_audio(sr)
print voice

#for battery low alert
low_battery.get_battery_status(slp,bat_module,obj1)
lcd.clear()
lcd.message('{0:0.1f}V {1:0.1f}mA'.format(obj1.v, obj1.i))
lcd.message('\n{0:0.1f} Watts'.format(obj1.p/1000))
