from control_motor import moveLeft
from control_motor import moveRight

def diff_control(gas, steering):
	#if car is not moving
	if -0.03 <= gas <= 0.03:
		steering_power=steering*100
		moveLeft(-steering_power)
		moveRight(steering_power)
	#if car is moving
	else:
		if abs(steering)<=0.2:
			moveLeft(gas*100)
			moveRight(gas*100)
		elif steering>0:
			moveLeft((1-steering)*gas*100)
			moveRight(gas*100 )
		else:
			moveLeft(gas*100)
			moveRight(gas*(1+steering)*100)

