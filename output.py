import import_file as f

def txt_out(str,ser,ter,t2s):
    if ser:
        f.ser.ser_write(str)
    if ter:
        print(str)
    if t2s:
        f.tts.speak(str)

