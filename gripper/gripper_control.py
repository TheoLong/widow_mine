from servo_drive import pwm as pwm

def movePitch (pitch, pcurrent)
	step=50
	upper=180
	lower=0
	if current==upper or current== lower
		return pcurrent
	else
		if pitch>=0.1:
			pcurrent=pcurrent+step*pitch
			pwm.pitch(pcurrent)
		else if pitch<=0.1:
			pcurrent=pcurrent-step*pitch
			pwm.pitch(pcurrent)
		return pcurrent
def moveRoll (roll,rcurrent)
	step=50
	upper=180
	lower=0
	if rcurrent==upper or rcurrent== lower
		return rcurrent
	else
		if roll>=0.1:
			rcurrent=rcurrent+step*roll
			pwm.roll(rcurrent)
		else if roll<=0.1:
			rcurrent=rcurrent-step*roll
			pwm.roll(rcurrent)
		return ycurrent
def grab(grab,gcurrent)
	step=50
	upper=180
	lower=0
	if gcurrent==upper or gcurrent== lower
		return gcurrent
	else
		if grab>=0.1:
			gcurrent=gcurrent+step*grab
			pwm.gripper(gcurrent)
		else if grab<=0.1:
			gcurrent=gcurrent-step*grab
			pwm.gripper(gcurrent)
		return gcurrent
