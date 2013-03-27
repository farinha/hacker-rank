# distance measured as number of moves necessary to get there
def distance(bot, dirtyCell):
	return abs(bot[0] - dirtyCell[0]) + abs(bot[1] - dirtyCell[1])

def next_move(botPosition, dirtyCells):			
	closestDirty = []
	closestDirtyDistance = 0
	for d in dirtyCells:
		#print(repr(d))
		#print(distance(botPosition, d))
		distanceToIt = distance(botPosition, d)
		if distanceToIt == 0:
			print('CLEAN')
			return
		elif closestDirty == [] or distanceToIt < closestDirtyDistance:
			closestDirty = d
			closestDirtyDistance = distanceToIt
	
	# moves are according to how the grid looks on the screen
	# for example, RIGHT is +1 on the y-coordinate	
	if botPosition[0] != closestDirty[0]:
		if botPosition[0] < closestDirty[0]:
			print('DOWN')
		else:
			print('UP')
	else:
		if botPosition[1] > closestDirty[1]:
			print('LEFT')
		else:
			print('RIGHT')
	
# top left corner is (0,0), x increases from top do bottom and y from left to right
botPosition = [int(x) for x in input().split(' ')]
# next five lines describe the grid
dirtyCells = []
for i in range(5):
	gridLine = input()
	for j in range(5):
		if gridLine[j] == 'd':
			dirtyCells.append([i, j])

next_move(botPosition, dirtyCells)