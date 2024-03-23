a_file = open("advent_5_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

def fill_diagonal(x1, x2, y1, y2):
	if x1 < x2:
		if y1 < y2:
			y = y1
			for x in range(x1, x2+1):
				print(str(x) + "," + str(y))
				intersections[x][y] += 1
				y += 1
			return
		else:
			y = y1
			for x in range(x1, x2+1):
				print(str(x) + "," + str(y))
				intersections[x][y] += 1
				y = y-1
			return
	else:
		if y1 < y2:
			x = x1
			for y in range(y1, y2+1):
				print(str(x) + "," + str(y))
				intersections[x][y] += 1
				x = x-1
			return
		else:
			y = y2
			for x in range(x2, x1+1):
				print(str(x) + "," + str(y))
				intersections[x][y] += 1
				y += 1
			return

intersections = [[0 for x in range(1000)] for y in range(1000)]
for line in contents_split:
	arrow_split = line.split(" -> ")
	split1 = arrow_split[0].split(",")
	x1 = int(split1[0])
	y1 = int(split1[1])
	split2 = arrow_split[1].split(",")
	x2 = int(split2[0])
	y2 = int(split2[1])

	if x1 == x2:
		list_range = range(y1, y2+1)
		if y1 > y2:
			list_range = range(y2, y1+1) 
		for y in list_range:
			intersections[x1][y] += 1
	elif y1 == y2:
		list_range = range(x1, x2+1)
		if x1 > x2:
			list_range = range(x2, x1+1)
		for x in list_range:
			intersections[x][y1] += 1
	else:
		fill_diagonal(x1, x2, y1, y2)


# for line in intersections:
# 	print(line)
count_overlap = 0
for line in intersections:
	for num in line:
		if num >=2:
			count_overlap += 1
print(count_overlap)


