a_file = open("advent_25_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()
cucs = map(list, contents_split)
cucs = [[i for i in sublist] for sublist in cucs]

def get_herds():
	east = []
	south = []
	for row in range(len(cucs)):
		for col in range(len(cucs[0])):
			if cucs[row][col] == "v":
				south.append([row, col])
			elif cucs[row][col] == ">":
				east.append([row, col])

	return east, south

def get_adj(x, y, herd_type):
	if herd_type == "east":
		if y+1 >= len(cucs[0]):
			return x, 0
		else:
			return x, y+1
	else:
		if x+1 >= len(cucs):
			return 0, y
		else:
			return x+1, y

def get_adjs(x, y, herd_type):
	if herd_type == "east":
		adj_x, adj_y = get_adj(x, y, "east") 
	else:
		adj_x, adj_y = get_adj(x, y, "south")

	if cucs[adj_x][adj_y] == ".":
		# cucs[adj_x][adj_y] = cucs[x][y]
		# cucs[x][y] = "."
		return adj_x, adj_y, True
	else:
		return x, y, False

def move_all(adjs):
	for adj in adjs:
		adj_x, adj_y, move = adj[0]
		x, y = adj[1]
		if move:
			cucs[adj_x][adj_y] = cucs[x][y]
			cucs[x][y] = "."

def pretty_print():
	for line in cucs:
		print(line)

def print_loc(x, y):
	print("(" + str(x) + "," + str(y) + ")")

def part_1():
	east_herd, south_herd = get_herds()
	step = 0
	while True:
		# print("step: " + str(step))
		# print("east")
		# print(east_herd)
		# print("south")
		# print(south_herd)
		# pretty_print()
		moves = 0

		new_east_herd = []
		adjs = []
		for herd in east_herd:
			curr_x = herd[0]
			curr_y = herd[1]
			adj_x, adj_y, move = get_adjs(curr_x, curr_y, "east")
			adjs.append([[adj_x, adj_y, move], [curr_x, curr_y]])

			# print("old")
			# print_loc(curr_x, curr_y)
			# print("new")
			# print_loc(adj_x, adj_y)
			if move:
				moves += 1
			new_east_herd.append([adj_x, adj_y])
		move_all(adjs)
		east_herd = new_east_herd

		new_south_herd = []
		adjs = []
		for herd in south_herd:
			curr_x = herd[0]
			curr_y = herd[1]
			adj_x, adj_y, move = get_adjs(curr_x, curr_y, "south")
			adjs.append([[adj_x, adj_y, move], [curr_x, curr_y]])

			# print("old")
			# print_loc(curr_x, curr_y)
			# print("new")
			# print_loc(adj_x, adj_y)
			if move:
				moves += 1
			new_south_herd.append([adj_x, adj_y])
		move_all(adjs)
		south_herd = new_south_herd
		
		step += 1
		if moves == 0:
			print(step)
			break

part_1()

