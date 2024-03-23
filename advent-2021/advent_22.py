import numpy

a_file = open("advent_22_sample.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

def single_loc_in_bounds(loc):
	return loc <= 50 and loc >= -50

def loc_in_bounds(x1, x2, y1, y2, z1, z2):
	return single_loc_in_bounds(x1) and single_loc_in_bounds(x2) \
		and single_loc_in_bounds(y1) and single_loc_in_bounds(y2) \
		and single_loc_in_bounds(z1) and single_loc_in_bounds(z2)

total_on = 0
instr = 0

# whole_max_x = 0
# whole_max_y = 0
# whole_max_z = 0

# for line in contents_split:
# 	split_space = line.split(" ")
# 	switch = split_space[0]
# 	split_comma = split_space[1].split(",")
# 	split_x = split_comma[0].split("=")[1].split("..")
# 	x1 = int(split_x[0])
# 	x2 = int(split_x[1])
# 	if max(x1, x2) > whole_max_x:
# 		whole_max_x = max(x1, x2)
# 	split_y = split_comma[1].split("=")[1].split("..")
# 	y1 = int(split_y[0])
# 	y2 = int(split_y[1])
# 	if max(y1, y2) > whole_max_y:
# 		whole_max_y = max(y1, y2)
# 	split_z = split_comma[2].split("=")[1].split("..")
# 	z1 = int(split_z[0])
# 	z2 = int(split_z[1])
# 	if max(z1, z2) > whole_max_z:
# 		whole_max_z = max(z1, z2)

# print(whole_max_x)
# print(whole_max_y)
# print(whole_max_z)

# plane = numpy.zeros((whole_max_x, whole_max_y, whole_max_z))
on = set()
for line in contents_split:
	print(instr)
	split_space = line.split(" ")
	switch = split_space[0]
	split_comma = split_space[1].split(",")
	split_x = split_comma[0].split("=")[1].split("..")
	x1 = int(split_x[0])
	x2 = int(split_x[1])
	min_x = min(x1, x2)
	max_x = max(x1, x2)
	split_y = split_comma[1].split("=")[1].split("..")
	y1 = int(split_y[0])
	y2 = int(split_y[1])
	min_y = min(y1, y2)
	max_y = max(y1, y2)
	split_z = split_comma[2].split("=")[1].split("..")
	z1 = int(split_z[0])
	z2 = int(split_z[1])
	min_z = min(z1, z2)
	max_z = max(z1, z2)
	# if loc_in_bounds(x1, x2, y1, y2, z1, z2):
	for x in range(min_x, max_x + 1):
		for y in range(min_y, max_y + 1):
			for z in range(min_z, max_z + 1):
				# total += 1
				string = "(" + str(x) + "," + str(y) + "," + str(z) + ")"
				if string in on and switch == "off":
					on.remove(string)
				else:
					on.add(string)
	instr += 1

# total_on = 0
# for row in plane:
# 	for col in row:
# 		for z in col:
# 			if z:
# 				total_on += 1
print(len(list(on)))
