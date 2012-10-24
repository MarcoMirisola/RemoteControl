f = open("data.txt", "r")
text = f.read()

import serial 
import string
#arduino=serial.Serial('/dev/ttyACM0')
arduino=serial.Serial('/dev/tty.usbmodemfd121')

prova=text.split(',')

arduino.write(prova[0])
print prova[0]


#ma anche text[] che da la posizione 
# Scrive un file.

