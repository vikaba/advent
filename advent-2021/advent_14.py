from collections import Counter

a_file = open("advent_14_sample.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

template = contents_split[0]
rule_map = {}
for line in range(2, len(contents_split)):
	rule_split = contents_split[line].split(" -> ")
	rule_map[rule_split[0]] = rule_split[1]

print(rule_map)

# def repeat_pair_insertion(curr_string, curr_times, total_times):
# 	print(curr_times)
# 	if curr_times < total_times:
# 		idx = 0
# 		final_string = curr_string[0]
# 		while idx+1 < len(curr_string):
# 			pair = curr_string[idx] + curr_string[idx+1]
# 			final_string += rule_map[pair] + curr_string[idx+1]
# 			idx += 1
# 		return repeat_pair_insertion(final_string, curr_times + 1, total_times)
# 	else:
# 		return curr_string

start_pairs = {}
letter_counts = dict(Counter(template))
def start_map():
	idx = 0
	while idx+1 < len(template):
		pair = template[idx] + template[idx+1]
		if pair in start_pairs:
			start_pairs[pair] += 1
		else:
			start_pairs[pair] = 1
		
		if rule_map[pair] in letter_counts:
			letter_counts[rule_map[pair]] += 1
		else:
			letter_counts[rule_map[pair]] = 1
		idx += 1

def put_in_map(to_put, map_x, count):
	if to_put in map_x:
		map_x[to_put] += count
	else:
		map_x[to_put] = count

def repeat_pair_insertion(curr_pairs, curr_counts, curr_times, total_times):
	if curr_times == total_times:
		return curr_counts
	
	new_pair_map = {}
	for pair, count in curr_pairs.items():
		pair_match = rule_map[pair]
		pair_1 = pair[0] + pair_match
		pair_2 = pair_match + pair[1]
		put_in_map(pair_1, new_pair_map, count)
		put_in_map(pair_2, new_pair_map, count)
		put_in_map(pair_match, curr_counts, count)

	return repeat_pair_insertion(new_pair_map, curr_counts, curr_times+1, total_times)

start_map()
print(Counter(repeat_pair_insertion(start_pairs, letter_counts, 0, 10)))

