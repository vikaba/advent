a_file = open("advent_6_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

initial = list(map(lambda x: int(x), contents_split[0].split(",")))
fish_map = {}
for fish in initial:
	if fish in fish_map:
		fish_map[fish] += 1
	else:
		fish_map[fish] = 1
print(fish_map)

# def totals(day):
# 	fish_list = initial#[3]#list(fish_map.keys())
# 	total = 0
# 	for fish in fish_list:
# 		print("fish: " + str(fish))
# 		total_fish = total_fish_day(day, fish)
# 		total += total_fish # * fish_map[fish]
# 	return total

# def total_by_digit(fish_list):
# 	fish_map = {}
# 	for fish in fish_list:
# 		if fish in fish_map:
# 			fish_map[fish] += 1
# 		else:
# 			fish_map[fish] = 1

# 	final = ""
# 	for key, count in fish_map:
# 		final += count + " "
# 	return final

# def total_fish_day(day, fish):
# 	day_count = 0
# 	fish_list = [fish]
# 	while day_count < day:
# 		#print("day " + str(day_count))
# 		for i in range(len(fish_list)):
# 			if fish_list[i] != 0:
# 				fish_list[i] = fish_list[i] - 1
# 			else:
# 				fish_list[i] = 6
# 				fish_list.append(8)
# 		day_count += 1
# 		print(total_by_digit(fish_list)) 
# 	#return len(fish_list)

# print(totals(80))