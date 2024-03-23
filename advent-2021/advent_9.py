a_file = open("advent_9_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()
height_map = map(list, contents_split)
int_height_map = [[int(i) for i in sublist] for sublist in height_map]

def check_below(row, col):
	if row+1 < len(int_height_map):
		if int_height_map[row][col] < int_height_map[row+1][col]:
			return True
		else:
			return False
	else:
		return True

def check_above(row, col):
	if row-1 >= 0:
		if int_height_map[row][col] < int_height_map[row-1][col]:
			return True
		else:
			return False
	else:
		return True


def check_right(row, col):
	if col+1 < len(int_height_map[0]):
		if int_height_map[row][col] < int_height_map[row][col+1]:
			return True
		else:
			return False
	else:
		return True


def check_left(row, col):
	if col-1 >= 0:
		if int_height_map[row][col] < int_height_map[row][col-1]:
			return True
		else:
			return False
	else:
		return True

nums = []
locations = []
def part_1():
	for row in range(len(int_height_map)):
		for col in range(len(int_height_map[0])):
			if check_left(row, col) and check_right(row, col) and check_above(row, col) and check_below(row, col):
				nums.append(int_height_map[row][col])
				locations.append([row, col])

	final_sum = 0
	for num in nums:
		final_sum += num + 1
	# print(nums)
	# print(final_sum)

part_1()

basin_locs = {}
def calculate_basins(row, col, loc_name):
	if col-1 >= 0 and int_height_map[row][col-1] != 9 and [row, col-1] not in basin_locs[loc_name]:
		basin_locs[loc_name].append([row, col-1])
		calculate_basins(row, col-1, loc_name)
	if col+1 < len(int_height_map[0]) and int_height_map[row][col+1] != 9 and [row, col+1] not in basin_locs[loc_name]:
		basin_locs[loc_name].append([row, col+1])
		calculate_basins(row, col+1, loc_name)
	if row-1 >= 0 and int_height_map[row-1][col] != 9 and [row-1, col] not in basin_locs[loc_name]:
		basin_locs[loc_name].append([row-1, col])
		calculate_basins(row-1, col, loc_name)
	if row+1 < len(int_height_map) and int_height_map[row+1][col] != 9 and [row+1, col] not in basin_locs[loc_name]:
		basin_locs[loc_name].append([row+1, col])
		calculate_basins(row+1, col, loc_name)

def print_basins():
	lengths = []
	for origin,basins in basin_locs.items():
		lengths.append(len(basins))
	sorted_lengths = sorted(lengths, reverse=True)
	print(sorted_lengths)
	product = sorted_lengths[0] * sorted_lengths[1] * sorted_lengths[2]
	print(product)
		# print("new one")
		# for basin in basins:
		# 	print(str(int_height_map[basin[0]][basin[1]]))

def part_2():
	for location in locations:
		loc_name = str(location[0]) + "-" + str(location[1])
		basin_locs[loc_name] = [location]
		calculate_basins(location[0], location[1], loc_name)
	print_basins()

part_2()


