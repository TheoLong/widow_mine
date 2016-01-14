import servo_drive as pwm

def movePitch (pitch, pcurrent):
	step=50
	upper=180
	lower=0
	if pcurrent==upper or pcurrent== lower:
		return pcurrent
	else:
		if pitch>=0.1:
			pcurrent=pcurrent+step*pitch
			pwm.pitch(pcurrent)
		elif pitch<=-0.1:
			pcurrent=pcurrent-step*pitch
			pwm.pitch(pcurrent)
		return pcurrent
def moveRoll (roll,rcurrent):
	step=50
	upper=180
	lower=0
	if rcurrent==upper or rcurrent== lower:
		return rcurrent
	else:
		if roll>=0.1:
			rcurrent=rcurrent+step*roll
			pwm.roll(rcurrent)
		elif roll<=-0.1:
			rcurrent=rcurrent-step*roll
			pwm.roll(rcurrent)
		return ycurrent
def grab(grab,gcurrent):
	step=50
	upper=180
	lower=0
	if gcurrent==upper or gcurrent== lower:
		return gcurrent
	else:
		if grab>0:
			gcurrent=gcurrent+step*grab
			pwm.gripper(gcurrent)
		elif grab<0:
			gcurrent=gcurrent-step*grab
			pwm.gripper(gcurrent)
		return gcurrent
