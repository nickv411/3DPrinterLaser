import serial
import time
from datetime import datetime

# https://all3dp.com/2/3d-printer-g-code-commands-list-tutorial/
# http://nebarnix.com/img2gco/
"""
    https://all3dp.com/2/3d-printer-g-code-commands-list-tutorial/
    http://nebarnix.com/img2gco/ 
        - Use Scan rate of 250
        - Remove top and bottom of gcode in order to use this reader.
"""


def command(ser, command):
    start_time = datetime.now()
    ser.write(str.encode(command))

    while True:
        line = ser.readline()
        print(str(start_time) + " : " + str(line.decode()))
        time.sleep(0.004)
        if line == b'ok\n':
            break


def file_reader(file):
    '''
    Parse data from the file and add all strings that start with "k" to a list and return it.
    '''
    my_list = []
    with open(file, 'r', encoding="utf=8") as my_file:
        for word in my_file.read().split("\n"):
            #print(word)
            if not word.__contains__(";") and not word is "":
                my_list.append(word)
    return my_list


def file_executor(cmd_list):
    """
    Runs through list of string commands, adds new line and sends to serial port
    :param cmd_list: list of string commands without \n char or \r\n
    :return: nothing
    """
    for cmd in cmd_list:
        new_cmd = cmd + "\r\n"
        command(ser, new_cmd)


ser = serial.Serial('COM3', 115200)
#time.sleep(2)
#command(ser, "G28\r\n")  # Autohome

command(ser, "G0 X65 Y11 Z25 F3000\r\n")  # Move to start for laser
"""
#command(ser, "M106 255\r\n")  # Turn on laser
"""
#command(ser, "G1 X120 Y75 F250\r\n")  # Move laser
"""command(ser, "M107\r\n")  # Shut off laser"""
try:
    file_executor(file_reader("output.gcode"))
except KeyboardInterrupt:
#file_reader("test.gcode")
    command(ser, "M107\r\n")
