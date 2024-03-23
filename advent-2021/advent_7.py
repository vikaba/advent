import statistics

a_file = open("advent_7_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

initial = list(map(lambda x: int(x), contents_split[0].split(",")))
min_pos = min(initial)
max_pos = max(initial)

def calc_fuel_part2(init_pos, dest_pos):
	diff = abs(dest_pos - init_pos)
	# for i in range(diff+1):
	# 	total_fuel += i
	# use consecutive num sum formula instead (n/2)(n+1)
	total_fuel = diff * (diff+1) / 2
	return total_fuel

def calc_fuel_part1(init_pos, dest_pos):
	# can also take diff with median instead of all these positions
	# since that's the num directly in the middle
	diff = abs(dest_pos - init_pos)
	return diff

min_fuel = 0
first = True
for potential_pos in range(min_pos, max_pos+1):
	fuel_sum = 0
	for actual_pos in initial:
		fuel_sum += calc_fuel_part2(actual_pos, potential_pos)

	if first:
		min_fuel = fuel_sum
		first = False
	else:
		if fuel_sum < min_fuel:
			min_fuel = fuel_sum
	fuel_sum = 0

print(min_fuel)
