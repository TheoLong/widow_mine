import Adafruit_BBIO.UART as UART
import serial
import math
UART.setup("UART1")
ser = serial.Serial(port = "/dev/ttyO0",baudrate = 9600)
ser.close()
ser.open()
step=63
def moveLeft(power):
	if power==0:
		output=64
	elif power>0:
		output=(power/100)*step
		print("percentage: ")
		print(power/100)
		print("step: ")
		print (step)
		output=round(output,0)
		print("round:" )
		print(output)
		output=int(output)
		output=64+output
	elif power<0:
		abs(power)
		output=(power/100)*step	
		output=round(output,0)
		output=int(output)
	else:
		output=0
		print("power input error")
	print(output)
	ser.write(chr(output))

def moveRight(power):
	if power==0:
		output=192
	elif power>0:
		output=(power/100)*step	
		output=round(output,0)
		output=int(output)
		output=192+output
	elif power<0:
		abs(power)
		output=(power/100)*step	
		output=round(output,0)
		output=int(output)
		output=127+output
	else:
		output=0
		print("power input error")
	print (output)
	ser.write(chr(output))



	
