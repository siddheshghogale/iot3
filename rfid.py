'''
import RPi.GPIO as gp
from mfrc522 import SimpleMFRC522
gp.setwarnings(False)
reader=SimpleMFRC522()
try:
	print("Place RFID card to Read")
	idd,text=reader.read()
	print(text)
finally:
	gp.cleanup()

'''
import RPi.GPIO as gp
from mfrc522 import SimpleMFRC522
gp.setwarnings(False)
reader=SimpleMFRC522()
try:
	text=input("Enter ")
	reader.write(text)
	print("Written")
finally:
	gp.cleanup()

#vcc=1,rst=22,miso=21,mosi=19,sck=23,sda=24
