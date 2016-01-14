import servo_drive as pwm
import math
def movePitch (pitch, pcurrent):
	step=50.0
	upper=180.0
	lower=0.0
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
	step=50.0
	upper=180.0
	lower=0.0
	if rcurrent==upper or rcurrent== lower:
		return rcurrent
	else:
		if roll>=0.1:
			rcurrent=rcurrent+step*roll
			pwm.roll(rcurrent)
			#print rcurrent
			return rcurrent
		
		elif roll<=-0.1:
			rcurrent=rcurrent-step*roll
			pwm.roll(rcurrent)
		 	return rcurrent
def grab(grab,gcurrent):
	step=50.0
	upper=180.0
	lower=0.0
	if gcurrent==upper or gcurrent== lower:
		return gcurrent
	else:
		if grab>0:
			gcurrent=gcurrent+step*grab
			pwm.gripper(gcurrent)
			return gcurrent
		elif grab<0:
			gcurrent=gcurrent-step*grab
			pwm.gripper(gcurrent)
			return gcurrent
