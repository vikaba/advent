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

# initially will reproduce at initial_val + 1
# then at initial_val + 1 + 7
# 18 - 4 = 14 / 7 = 2 + 1 = 3
# 18 - 5 = 13 / 7 = 1.xx + 1 = 2
# 18 - 2 = 16 / 7 = 2.xxx + 1 = 3
# 18 - 3 = 15/ 5 = 2.xxx + 1 = 3
# 18 - 2 = 16 / 9 = 1
# 18 - 3 = 15 / 9 = 2 
def totals(day):
	fish_list = list(fish_map.keys())
	total = 0
	for fish in fish_list:
		total_fish = total_fish_day(day, fish)
		total += fish_map[fish] * total_fish
	return total

def total_fish_day(day, fish):
	day_count = 0
	fish_list = [fish]
	while day_count < day:
		print(day_count)
		for i in range(len(fish_list)):
			if fish_list[i] != 0:
				fish_list[i] = fish_list[i] - 1
			else:
				fish_list[i] = 6
				fish_list.append(8)
		day_count += 1
	return len(fish_list)


#print(total_fish_day(18))
print(totals(256))