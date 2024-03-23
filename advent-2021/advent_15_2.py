from dijkstar import Graph, find_path

a_file = open("advent_15_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()
graph = Graph()
adj_list = {}

def get_string_loc(x, y):
	return str(x) + "," + str(y)

def get_int_loc(string_loc):
	split = string_loc.split(",")
	return [int(split[0]), int(split[1])]

def fill_adj(row, col):
	original = get_string_loc(row, col)
	if original not in adj_list:
		adj_list[original] = []
	if row + 1 < len(new_matrix):
		string_loc = get_string_loc(row+1, col)
		adj_list[original].append(string_loc)
	if row - 1 >= 0:
		string_loc = get_string_loc(row-1, col)
		adj_list[original].append(string_loc)
	if col + 1 < len(new_matrix[0]):
		string_loc = get_string_loc(row, col+1) 
		adj_list[original].append(string_loc)
	if col - 1 >= 0:
		string_loc = get_string_loc(row, col-1)
		adj_list[original].append(string_loc)

def get_diag(row, col, i, length, positions):
	new_row = row
	new_column = col + length

	while new_row >= 0:
		positions[i].append([new_row, new_column])
		new_row = new_row - length
		new_column = new_column + length

def get_diag_2(row, col, i, length, positions):
	new_row = row
	new_column = col + length

	while new_column < length * 5:
		positions[i].append([new_row, new_column])
		new_row = new_row - length
		new_column = new_column + length

def get_tile_pos(row, col, length):
	positions = {}
	positions[1] = [[row, col+length], [row+length, col]]
	for i in range(2, 5):
		positions[i] = []
		positions[i].append([row + length * i, col])
		get_diag(row + length * i - length, col, i, length, positions)

	# print(positions)
	# print("after rest")
	curr_col = col + length
	for i in range(5, 9):
		positions[i] = []
		positions[i].append([row + length * 4, curr_col])
		get_diag_2(row + length * 4 - length, curr_col, i, length, positions)
		curr_col += length
	# print(positions)
	return positions

get_tile_pos(0,0,10)

def get_new_val(curr_val):
	if curr_val + 1 > 9:
		return 1
	else:
		return curr_val + 1

new_matrix = [[0] * len(contents_split) * 5 for i in range(len(contents_split[0]) * 5)]
for row in range(len(contents_split)):
	for col in range(len(contents_split[0])):
		new_matrix[row][col] = int(contents_split[row][col])
		new_positions = get_tile_pos(row, col, len(contents_split))
		curr_val = new_matrix[row][col]
		total_pos = 0
		for key, val in new_positions.items():
			total_pos += len(val)
			for pos in val:
				new_val = get_new_val(curr_val)
				new_matrix[pos[0]][pos[1]] = get_new_val(curr_val)
			curr_val = new_val
# 		print(total_pos)
# 		print(new_positions)
# print(new_matrix)

for row in range(len(new_matrix)):
	for col in range(len(new_matrix[0])):
		string_loc = get_string_loc(row, col)
		# print(string_loc)
		fill_adj(row, col)
		for adj in adj_list[string_loc]:
			adj_int_loc = get_int_loc(adj)
			val_at_adj = new_matrix[adj_int_loc[0]][adj_int_loc[1]]
			graph.add_edge(string_loc, adj, val_at_adj)

print(find_path(graph, "0,0", "499,499"))

