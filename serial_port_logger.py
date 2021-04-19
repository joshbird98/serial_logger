# Basic script to open serial port and write everything it recevies into a file

from serial import Serial
import time
from datetime import datetime
import sys
import glob
import serial

# COM_PORT = "COM5"
baudrate = 115200
logfile_path = "C:\\Users\\Josh\\Documents\\tmp\\serial_log.txt"

def main():

    serialPorts = serial_ports()
    
    if len(serialPorts) < 1:
        print("No serial ports available.")
        input("Press the Enter key to exit.")
        quit()
    
    else:
        print("Available serial ports... ")
        for i in range(len(serialPorts)):
            print(i, ": ", serialPorts[i])
        choice = -1
        while ((choice < 0) or (choice >= len(serialPorts))):
            try:
                choice = int(input("Choice: "))
            except ValueError:
                choice = -1
            
    try:
        ser = Serial(serialPorts[i], baudrate, timeout=3)
    except:
        print("%s not available." % serialPorts[i])
        input("Press the Enter key to exit.")
        quit()
    
    print("Opened %s" % serialPorts[i])
    while True:
        data = ser.readline()
        datestamp = datetime.now()
        print(datestamp)
        print(data)

        f = open(logfile_path, 'a')
        f.write(str(datestamp))
        f.write('\n')
        f.write(str(data))
        f.write('\n~~~~~\n')
        f.close()

# Returns a list of serial port names available on the system
def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
    
main()
