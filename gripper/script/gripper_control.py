import servo_drive as pwm
import math
def movePitch (pitch, pcurrent):
	step=5.0
	upper=190.0
	lower=40.0
	#print pcurrent
	#print pitch
	if (pcurrent == lower and pitch < 0) or (pcurrent == upper and pitch > 0) :
		return pcurrent
	else:
		if abs(pitch)>=0.1:
			temp=pcurrent+step*pitch
			if temp<=lower:
				temp=lower
			elif temp>=upper:
				temp=upper
			#print pcurrent
			pwm.pitch(temp)
			return temp
		else:
			return pcurrent
		
def moveRoll (roll,rcurrent):
	step=5.0
	upper=190
	lower=0
	if (rcurrent == lower and roll < 0) or (rcurrent == upper and roll > 0) :
		return rcurrent
	else:
		if abs(roll)>=0.1:
			temp=rcurrent+step*roll
			if temp<=lower:
				temp=lower
			elif temp>=upper:
				temp=upper
			pwm.roll(temp)
			return temp
		else:
			return rcurrent
def grab(grab,gcurrent):
	step=3.0
	upper=20
	lower=130
	print grab
	if (gcurrent == lower and grab < 0) or (gcurrent == upper and grab > 0) or (grab==0):
		return gcurrent
	else:
		temp=gcurrent+step*grab
		if temp<=lower:
			temp=lower
		elif temp>=upper:
			temp=upper
		pwm.gripper(temp)
		return temp
