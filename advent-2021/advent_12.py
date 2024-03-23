from collections import Counter

a_file = open("advent_12_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

adj_map = {}
for line in contents_split:
	split = line.split("-")
	if split[0] not in adj_map:
		adj_map[split[0]] = [split[1]]
	else:
		adj_map[split[0]].append(split[1])
	if split[1] not in adj_map:
		adj_map[split[1]] = [split[0]]
	else:
		adj_map[split[1]].append(split[0])

paths = []


def rec_find_path_part_1(adj, curr_path):
	if adj == "end":
		# print("reached end")
		curr_path.append("end")
		return curr_path
	elif (adj.islower() and adj not in curr_path) or adj.isupper() and adj != "start":
		curr_path.append(adj)
		get_paths(adj, curr_path)

def can_visit_again(path, point_to_check):
	# point is not in path or is and
	# there can't already be a double in the path
	# and the count for this point should only be 1
	counts = {}
	if point_to_check not in path:
		return True
	for point in path:
		if point.islower():
			if point not in counts:
				counts[point] = 1
			else:
				counts[point] += 1
				if counts[point] == 2:
					return False
	if counts[point_to_check] < 2:
		return True
	return False

def rec_find_path_part_2(adj, curr_path):
	if adj == "end":
		# print("reached end")
		curr_path.append("end")
		return curr_path
	elif (adj != "start" and adj.islower() and can_visit_again(curr_path, adj)) or adj.isupper():
		curr_path.append(adj)
		get_paths(adj, curr_path)

def get_paths(start_with, curr_path):
	# print("start node: " + start_with)
	# print("curr_path")
	# print(curr_path)
	for adj in adj_map[start_with]:
		curr_path_copy = curr_path.copy()
		# print("looking at connection to " + adj)
		found_path = rec_find_path_part_2(adj, curr_path_copy)
		if found_path is None:
			# print("not viable path, moving on")
			continue
		# print("complete path:")
		# print(found_path)
		if found_path not in paths:
			paths.append(found_path)

for starter in adj_map["start"]:
	# print("looking at start-" + starter)
	get_paths(starter, ["start", starter])

print("ALL PATHS:")
print(len(paths))
# print(paths)
