a_file = open("advent_6_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

initial = list(map(lambda x: int(x), contents_split[0].split(",")))
print(initial)

# 3: 2, 4: 1, 1: 1, 2:1
# 2: 2, 3: 1, 4:0
def by_digits(day):
	digit_map = []
	for i in range(0, 9):
		digit_map.append(0)
	for num in initial:
		digit_map[num] += 1
	day_count = 0
	while day_count < day:
		# print("day: " + str(day_count))
		copy_digits = digit_map.copy()
		# print(digit_map)
		for i, digit in enumerate(digit_map):
			if i == 8:
				digit_map[8] = copy_digits[0]
			elif i == 6:
				digit_map[6] = copy_digits[0] + copy_digits[7]
			else:
				digit_map[i] = copy_digits[i+1]
		day_count += 1
		total = 0
	for key in digit_map:
		total += key
	print(total)

by_digits(256)

# def total_by_digit(fish_list):
# 	fish_map = {}
# 	for fish in fish_list:
# 		if fish in fish_map:
# 			fish_map[fish] += 1
# 		else:
# 			fish_map[fish] = 1

# 	final = ""
# 	for i in range(0, 9):
# 		if i in fish_map:
# 			final += str(fish_map[i]) + " "
# 		else:
# 			final += "0 "
# 	return final

# def total_fish_day(day):
# 	fish_list = initial
# 	day_count = 0
# 	while day_count < day:
# 		#print("day: " + str(day_count))
# 		#print(fish_list)
# 		for i in range(len(fish_list)):
# 			if fish_list[i] != 0:
# 				fish_list[i] = fish_list[i] - 1
# 			else:
# 				fish_list[i] = 6
# 				fish_list.append(8)
# 		day_count += 1
# 		print(total_by_digit(fish_list))
# 	return len(fish_list)

# print(total_fish_day(18))
#print(total_fish_day(256))