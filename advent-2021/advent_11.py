a_file = open("advent_11_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()
energy_map = map(list, contents_split)
energy_map = [[int(i) for i in sublist] for sublist in energy_map]

def check_and_recur(row, col, flashed_locs):
	if [row, col] not in flashed_locs and energy_map[row][col] > 9:
		flashed_locs.append([row, col])
		flash_adj(row, col, flashed_locs)

def flash_adj(row, col, flashed_locs):
	if row + 1 < len(energy_map):
		energy_map[row+1][col] += 1
		check_and_recur(row+1, col, flashed_locs)
	if row - 1 >= 0:
		energy_map[row-1][col] += 1
		check_and_recur(row-1, col, flashed_locs)
	if col + 1 < len(energy_map[0]):
		energy_map[row][col+1] += 1
		check_and_recur(row, col+1, flashed_locs)
	if col - 1 >= 0:
		energy_map[row][col-1] += 1
		check_and_recur(row, col-1, flashed_locs)
	if row + 1 < len(energy_map) and col + 1 < len(energy_map[0]):
		energy_map[row+1][col+1] += 1
		check_and_recur(row+1, col+1, flashed_locs)
	if row + 1 < len(energy_map) and col - 1 >= 0:
		energy_map[row+1][col-1] += 1
		check_and_recur(row+1, col-1, flashed_locs)
	if row - 1 >= 0 and col - 1 >= 0:
		energy_map[row-1][col-1] += 1
		check_and_recur(row-1, col-1, flashed_locs)
	if row - 1 >= 0 and col + 1 < len(energy_map[0]):
		energy_map[row-1][col+1] += 1
		check_and_recur(row-1, col+1, flashed_locs)

def reset_to_0(locs_to_reset):
	for loc in locs_to_reset:
		energy_map[loc[0]][loc[1]] = 0

def print_matrix():
	for line in energy_map:
		print(line)

def flashes_at_step(step):
	curr_step = 0
	flashes = 0
	while curr_step < step:
		over_9 = []
		for row in range(len(energy_map)):
			for col in range(len(energy_map[0])):
				energy_map[row][col] += 1
				if energy_map[row][col] > 9:
					over_9.append([row, col])
		copy_over_9 = over_9.copy()
		for flash in copy_over_9:
			flash_adj(flash[0], flash[1], over_9)
		flashes += len(over_9)
		reset_to_0(over_9)
		curr_step += 1
	print(flashes)

def flashes_until_sync():
	curr_step = 0
	flashes = 0
	while True:
		#print_matrix()
		over_9 = []
		for row in range(len(energy_map)):
			for col in range(len(energy_map[0])):
				energy_map[row][col] += 1
				if energy_map[row][col] > 9:
					over_9.append([row, col])
		copy_over_9 = over_9.copy()
		for flash in copy_over_9:
			flash_adj(flash[0], flash[1], over_9)
		flashes += len(over_9)
		reset_to_0(over_9)

		if len(over_9) == len(energy_map) * len(energy_map[0]):
			print("ALL FLASHING")
			print(curr_step+1)
			break
		curr_step += 1

flashes_at_step(100)
flashes_until_sync()