def next_move(botPosition, dirtyCell):
	# moves are according to how the grid looks on the screen
	# for example, RIGHT is +1 on the y-coordinate	
	if botPosition[0] != dirtyCell[0]:
		if botPosition[0] < dirtyCell[0]:
			print('DOWN')
		else:
			print('UP')
	elif botPosition[1] != dirtyCell[1]:
		if botPosition[1] > dirtyCell[1]:
			print('LEFT')
		else:
			print('RIGHT')
	else:
		print('CLEAN')

def find_dirty_cell():
	for i in range(5):
		gridLine = input()
		for j in range(5):
			if gridLine[j] == 'd':
				return[i, j]

# top left corner is (0,0), x increases from top do bottom and y from left to right
botPosition = [int(x) for x in input().split(' ')]

dirtyCell = find_dirty_cell()
next_move(botPosition, dirtyCell)