import statistics

a_file = open("advent_8_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

def part_1():
	lengths = [2, 3, 4, 7]
	count = 0
	for line in contents_split:
		del_split = line.split(" | ")[1].split(" ")
		for word in del_split:
			stripped = word.strip()
			print(stripped)
			if len(stripped) in lengths:
				count += 1
	print(count)

side_map = {}
# can figure out 1, 4, 7, 8
# have top, middle, bottom, right sides
final_map = {}

def get_word_of_len(length, words):
	for word in words:
		if len(word) == length:
			return list(word)

def get_not_easy_letters(words):
	lengths = [2,3,4]
	result = []
	for word in words:
		if len(word) not in lengths:
			result += list(word)
	result.remove(side_map["top"])
	return result

# FIRST METHOD
def get_top(words):
	one = final_map[1]
	seven = final_map[7]
	top = list(set(seven) - set(one))[0]
	side_map["top"] = top

# SECOND METHOD
def get_bottom(words):
	one = final_map[1]
	seven = final_map[7]
	four = final_map[4]
	not_easy_mode = statistics.mode(get_not_easy_letters(words))
	side_map["bottom"] = not_easy_mode

# THIRD METHOD
def get_middle(words):
	one = final_map[1]
	bottom = list(side_map["bottom"])
	top = list(side_map["top"])
	almost_three = one + bottom + top
	length_fives = []
	middle = ""
	three = ""
	for word in words:
		if len(word) == 5:
			letters = list(word)
			if len(list(set(letters) - set(almost_three))) == 1:
				three = word
				middle = list(set(letters) - set(almost_three))[0]
				break
	side_map["middle"] = middle
	final_map[3] = list(three)

# FOURTH METHOD
left_sides = []
def get_left_sides(words):
	eight = final_map[8]
	one = final_map[1]
	bottom = list(side_map["bottom"])
	top = list(side_map["top"])
	middle = list(side_map["middle"])
	left_sides = list(set(eight) - set(one + bottom + top + middle))
	side_map["left-sides"] = left_sides
	final_map[0] = left_sides + top + bottom + one

# FIFTH METHOD
def get_right_side(words):
	bottom = list(side_map["bottom"])
	top = list(side_map["top"])
	middle = list(side_map["middle"])
	almost_six = bottom + top + middle + side_map["left-sides"]
	bottom_right = ""
	for word in words:
		if len(word) == 6:
			letters = list(word)
			if len(list(set(letters) - set(almost_six))) == 1:
				bottom_right = list(set(letters) - set(almost_six))[0]
				break
	side_map["bottom-right"] = bottom_right
	top_right = list(set(final_map[1]) - set(list(bottom_right)))[0]
	side_map["top-right"] = top_right
	final_map[6] = [bottom_right] + middle + top + bottom + side_map["left-sides"]

# have bottom, top, middle, top-right, bottom-right, need to get left sides
# SIXTH METHOD
def get_left_sides_final(words):
	one = final_map[1]
	bottom = list(side_map["bottom"])
	top = list(side_map["top"])
	middle = list(side_map["middle"])
	almost_nine = one + bottom + top + middle
	top_left = ""
	for word in words:
		if len(word) == 6:
			letters = list(word)
			if len(list(set(letters) - set(almost_nine))) == 1:
				top_left = list(set(letters) - set(almost_nine))[0]
				break
	side_map["top-left"] = top_left
	bottom_left = list(set(side_map["left-sides"]) - set(list(top_left)))[0]
	side_map["bottom-left"] = bottom_left
	final_map[9] = [top_left] + bottom + top + middle + final_map[1]
	final_map[2] = [bottom_left, side_map["top-right"]] + bottom + top + middle
	final_map[5] = [top_left, side_map["bottom-right"]] + bottom + top + middle

def get_digit_from_letters(word):
	word_letters = list(word)
	# print(word_letters)
	if len(word_letters) == 2:
		return 1
	elif len(word_letters) == 3:
		return 7
	elif len(word_letters) == 4:
		return 4
	elif len(word_letters) == 7:
		return 8
	for digit, letters in final_map.items():
		# print(digit)
		# print(letters)
		if len(letters) == len(word_letters) and len(list(set(letters) - set(word_letters))) == 0:
			return digit

def part_2():
	final_sum = 0
	for line in contents_split:
		del_split = line.split(" | ")
		patterns = list(map(lambda x: x.strip(), del_split[0].split(" ")))
		output = list(map(lambda x: x.strip(), del_split[1].split(" ")))
		final_map[1] = get_word_of_len(2, patterns)
		final_map[4] = get_word_of_len(4, patterns)
		final_map[7] = get_word_of_len(3, patterns)
		final_map[8] = get_word_of_len(7, patterns)
		get_top(patterns)
		get_bottom(patterns)
		get_middle(patterns)
		get_left_sides(patterns)
		get_right_side(patterns)
		get_left_sides_final(patterns)
		# print("final map")
		# print(final_map)
		# print("side_map")
		# print(side_map)

		result_num = ""
		for word in output:
			result_num += str(get_digit_from_letters(word))
		print(result_num)
		final_sum += int(result_num)
	print(final_sum)
part_2()




