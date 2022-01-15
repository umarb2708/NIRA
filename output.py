import import_file as f
log_f=open('/home/pi/HIRA/output_log.log','w')

def txt_out(st,mode):
    #mode_b=f.conv.decimalToBinary(mode)
    
    if mode[0]=='1':
        #writing to tts
        f.tts.speak(st)
    if mode[1]=='1':
        #writing to terminal
        log_f.write(st)

    if mode[2]=='1':
        #writing to serial
        f.ser.ser_write(st)


