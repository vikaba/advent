import copy

a_file = open("advent_20_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

img_alg = contents_split[0]
original_input_image = contents_split[2:]

def string_to_int(row_string):
	final_string = ""
	for char in row_string:
		if char == '.':
			final_string += "0"
		else:
			final_string += "1"
	return int(final_string, 2)

def out_of_bounds(x, y, image):
	return x < 0 or y < 0 or x >= len(image) or y >= len(image[0])

def get_surrounding_string(x, y, image, even):
	row_string = ""
	for row in range(x-1, x+2):
		for col in range(y-1, y+2):
			if out_of_bounds(row, col, image):
				if even:
					row_string += "."
				else:
					row_string += "#"
			else:
				row_string += image[row][col]
	return row_string

def pretty_print(image):
	for line in image:
		print(line)

def part_1(input_image, even):
	lit_count = 0
	for i in range(4):
		if even:
			input_image.insert(0, ["." for i in range(len(input_image[0]))])
			input_image.append(["." for i in range(len(input_image[0]))])
		else:
			input_image.insert(0, ["#" for i in range(len(input_image[0]))])
			input_image.append(["#" for i in range(len(input_image[0]))])
	for line in input_image:
		for i in range(4):
			if even:
				line.append(".")
				line.insert(0, ".")
			else:
				line.append("#")
				line.insert(0, "#")
	output_image = copy.deepcopy(input_image)
	for row in range(len(input_image)):
		for col in range(len(input_image[0])):
			sur_string = get_surrounding_string(row, col, input_image, even)
			index = string_to_int(sur_string)
			img_alg_string = img_alg[index]
			if img_alg_string == "#":
				lit_count += 1
			output_image[row][col] = img_alg_string
	print(lit_count)
	return output_image

original_input_image = list(map(lambda n: list(n), original_input_image))
even = True
process_1 = part_1(original_input_image, even)
another = part_1(process_1, not even)
even = True
step = 3
while step <= 50:
	# print("step: " + str(step))
	another = part_1(another, even)
	even = not even
	step += 1

