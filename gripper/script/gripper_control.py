import servo_drive as pwm

def movePitch (pitch, pcurrent):
	step=50.0
	upper=180.0
	lower=0.0
	#print pitch
	if pcurrent==upper or pcurrent== lower:
		return pcurrent
	else:
		if pitch>=0.1:
			pcurrent=pcurrent+step*pitch
			print pcurrent
			pwm.pitch(pcurrent)
			return pcurrent
		elif pitch<=-0.1:
			pcurrent=pcurrent-step*pitch
			pwm.pitch(pcurrent)
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
			print rcurrent
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
