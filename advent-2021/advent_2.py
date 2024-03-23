content_array = []
def file_read(fname):
        with open(fname) as f:    
                for line in f:
                	content_array.append(line.strip('\n'))

file_read('advent_2_input.txt')

def no_aim():
	horizontal = 0
	depth = 0

	for instr in content_array:
		split = instr.split()
		direction = split[0]
		amount = int(split[1])
		if direction == "forward":
			horizontal += amount
		elif direction == "up":
			depth = depth - amount
		elif direction == "down":
			depth += amount

	print(horizontal * depth)

def with_aim():
	horizontal = 0
	depth = 0
	aim = 0

	for instr in content_array:
		split = instr.split()
		direction = split[0]
		amount = int(split[1])
		if direction == "forward":
			horizontal += amount
			depth += aim * amount
		elif direction == "up":
			aim = aim - amount
		elif direction == "down":
			aim += amount

	print(horizontal * depth)

with_aim()

