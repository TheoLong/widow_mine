from control_motor import moveLeft
from control_motor import moveRight


i=0
while (i != 100):
	left,right=raw_input("command: ").split()
	left, right = [int(left), int(right)]
	moveLeft(left)
	moveRight(right)
	i=i+1
	

