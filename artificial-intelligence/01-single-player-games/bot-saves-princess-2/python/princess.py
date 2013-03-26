gridSize = int(input())

# mario position given in the second line
# position is 'row column' which translates to 'y x' coordinates
marioPosition = [int(x) for x in input().split(' ')]
marioY, marioX = marioPosition

princessX, princessY = 0, 0
# read grid and determine the position of princess
princessFound = False
for i in range(gridSize):
	labyrinthLine = input()
	for j in range(gridSize):
		if labyrinthLine[j] == 'p':
			princessX = j
			princessY = i
			princessFound = True
			break
	if princessFound:
		break

# make the next move
if marioY != princessY:
	if marioY < princessY: # because we start with (0,0) at the top, flip the vertical move
		print('DOWN')
		marioY += 1
	else:
		print('UP')
		marioY -= 1			
elif marioX != princessX:
	if marioX > princessX:
		print('LEFT')
		marioX -= 1
	else:
		print('RIGHT')
		marioX += 1