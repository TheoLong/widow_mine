from control_motor import moveLeft
from control_motor import moveRight

def diff_control(gas, steering):
	#if car is not moving
	if -0.03 <= gas <= 0.03:
		steering_power=steering*100
		moveLeft(steering_power)
		moveRight(-steering_power)
	#if car is moving
	else:
		if steering>=0:
		moveLeft(gas)
		moveRight(steering*gas)
		else
		moveLeft(gas*abs(steering))
		moveRight(gas)

