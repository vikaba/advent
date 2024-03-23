a_file = open("advent_13_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

folds = []
paper = intersections = [[" " for x in range(2000)] for y in range(2000)]
for line in contents_split:
	if len(line) != 0 and line[0] != "f":
		split = line.split(",")
		col = int(split[0])
		row = int(split[1])
		paper[row][col] = "m"
	elif len(line) != 0 and line[0] == "f":
		split = line.split("=")
		fold = [split[0][-1], int(split[1])]
		folds.append(fold)

def get_y_transform_coord(x, y, mirror_line):
	x_diff = x - mirror_line
	new_x = mirror_line - x_diff
	return [new_x, y]

def get_x_transform_coord(x, y, mirror_line):
	y_diff = mirror_line - y
	new_y = mirror_line + y_diff
	return [x, new_y]

def fold_once(fold):
	fold_dir = fold[0]
	fold_coord = fold[1]
	if fold_dir == "y":
		for x in range(fold_coord+1, len(paper)):
			for y in range(len(paper[0])):
				if paper[x][y] == "m":
					new_coord = get_y_transform_coord(x, y, fold_coord)
					paper[new_coord[0]][new_coord[1]] = "m"
					paper[x][y] = " "
		return paper[0:fold_coord]
	else:
		for x in range(len(paper)):
			for y in range(fold_coord):
				if paper[x][y] == "m":
					new_coord = get_x_transform_coord(x, y, fold_coord)
					paper[new_coord[0]][new_coord[1]] = "m"
					paper[x][y] = " "
		for line in range(len(paper)):
			paper[line] = paper[line][fold_coord+1:]
		return paper


def remove_empty_padding():
	biggest_y = 0
	smallest_y = 1203812
	for line in range(len(paper)):
		for col in range(len(paper[0])):
			if paper[line][col] != " " and col > biggest_y:
				biggest_y = col
			elif paper[line][col] != " " and col < smallest_y:
				smallest_y = col

	for line in range(len(paper)):
		paper[line] = paper[line][smallest_y:biggest_y+1]

def count_marked():
	count = 0
	for line in paper:
		print(line)
		for point in line:
			if point == "m":
				count += 1
	print(count)

for fold in folds:
	paper = fold_once(fold)

remove_empty_padding()
count_marked()
