import import_file as f

def txt_out(st,mode):
    mode_b=f.conv.decimalToBinary(mode)

    if mode_b[0]=='1':
        #writing to tts
        f.tts.speak(st)
    if mode_b[1]=='1':
        #writing to serial
        f.ser.ser_write(st)
    if mode_b[2]=='1':
        #writing to terminal
        print(st)


