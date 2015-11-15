import control_motor


left,right=raw_input("command: ").split()
while (isinstance(left,int) and isinstance(right,int)):
	moveLeft(left)
	moveRight(right)
	left,right=raw_input("command: ").split()
	

