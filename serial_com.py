import serial
from time import sleep

ser = serial.Serial ("/dev/ttyS0", 9600)

def ser_write(data):
    ser.write(data.encode())

def ser_read():
    return ser.readline()
