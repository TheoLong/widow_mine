import Adafruit_BBIO.UART as UART
import serial
import math
UART.setup("UART1")
ser = serial.Serial(port = "/dev/ttyO0",baudrate = 9600)
serial.close()
serial.open()
step=63
def moveLeft(power):
	if power==0:
		output=0
	elif power>0:
		output=(power/100)*step	
		round(output,0)
		output=64+output
	elif power<0:
		abs(power)
		output=(power/100)*step	
		round(output,0)
	else:
		output=0
		print("power input error")
	ser.write(output)

def moveRight(power):
	if power==0:
		output=192
	elif power>0:
		output=(power/100)*step	
		round(output,0)
		output=192+output
	elif power<0:
		abs(power)
		output=(power/100)*step	
		round(output,0)
		output=127+output
	else:
		output=0
		print("power input error")
	ser.write(output)



	
