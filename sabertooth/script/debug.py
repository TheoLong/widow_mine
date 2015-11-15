import control_motor


left,right=raw_input("command: ").split()
i=0
while (i != 100):
	moveLeft(left)
	moveRight(right)
	left,right=raw_input("command: ").split()
	i=i+1
	

