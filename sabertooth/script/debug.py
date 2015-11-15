from control_motor import moveLeft
from control_motor import moveRight


left,right=raw_input("command: ").split()
left, right = [int(left), int(right)]
i=0
while (i != 100):
	moveLeft(left)
	moveRight(right)
	left,right=raw_input("command: ").split()
	i=i+1
	

