gridSize = int(input())

princessX, princessY, marioX, marioY = 0, 0, 0, 0

# read input and determine the position of princess and mario
for i in range(gridSize):
	labyrinthLine = input()
	for j in range(gridSize):
		if labyrinthLine[j] == 'p':
			princessX = j
			princessY = i
		elif labyrinthLine[j] == 'm':
			marioX = j
			marioY = i

# make the moves
while marioY != princessY:
	if marioY < princessY: # because we start with (0,0) at the top, flip the vertical move
		print('DOWN')
		marioY += 1
	else:
		print('UP')
		marioY -= 1
			
while marioX != princessX:
	if marioX > princessX:
		print('LEFT')
		marioX -= 1
	else:
		print('RIGHT')
		marioX += 1