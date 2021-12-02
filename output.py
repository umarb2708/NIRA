import import_file as f

def txt_out(st,mode):
    #mode_b=f.conv.decimalToBinary(mode)
    
    if mode[0]=='1':
        #writing to tts
        f.tts.speak(st)
    if mode[1]=='1':
        #writing to terminal
        print(st)
    if mode[2]=='1':
        #writing to serial
        f.ser.ser_write(st)


