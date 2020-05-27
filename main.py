
#!/usr/bin/python
import sys
import os as OS
from gtts import gTTS as voice
import speech_recognition as sr
sys.path.append('text2speech')
sys.path.append('voice_recognize')
import gt2s
import voice_command
#for gtts
gt2s.speak(st,voice,OS)
#for speech recognissation
global voice
voice=voice_command.get_audio(sr)
print voice
