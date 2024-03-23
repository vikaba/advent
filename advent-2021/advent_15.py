import queue
import sys

sys.setrecursionlimit(100000)

a_file = open("advent_15_sample_2.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

distances = {}
visited = set()
adj_list = {}

def get_string_loc(x, y):
	return str(x) + "," + str(y)

def get_int_loc(string_loc):
	split = string_loc.split(",")
	return [int(split[0]), int(split[1])]

def fill_adj(row, col):
	original = get_string_loc(row, col)
	if original not in adj_list:
		adj_list[original] = []
	if row + 1 < len(contents_split):
		string_loc = get_string_loc(row+1, col)
		adj_list[original].append(string_loc)
	if row - 1 >= 0:
		string_loc = get_string_loc(row-1, col)
		adj_list[original].append(string_loc)
	if col + 1 < len(contents_split[0]):
		string_loc = get_string_loc(row, col+1) 
		adj_list[original].append(string_loc)
	if col - 1 >= 0:
		string_loc = get_string_loc(row, col-1)
		adj_list[original].append(string_loc)

for row in range(len(contents_split)):
	for col in range(len(contents_split[0])):
		string_loc = get_string_loc(row, col)
		fill_adj(row, col)
		if row == 0 and col == 0:
			distances[string_loc] = 0 # int(contents_split[0][0])
		else:
			distances[string_loc] = sys.maxsize

# curr node is STRING
def dijkstra(curr_node):
	print("visited")
	print(len(visited))
	print("total")
	print(len(contents_split) * len(contents_split[0]))
	if len(visited) == len(contents_split) * len(contents_split[0]):
		print(distances)
		end_node = get_string_loc(len(contents_split)-1, len(contents_split[0])-1)
		return distances[end_node]
	print("curr node")
	print(curr_node)
	adjs = adj_list[curr_node]
	min_node_val = sys.maxsize
	min_node_loc = curr_node
	# print("ADJS")
	# print(adjs)
	for adj in adjs:
		if adj not in visited:
			print("visiting")
			print(adj)
			distance_adj = distances[adj]
			adj_node_int = get_int_loc(adj)
			print("distance to adj right now")
			print(distance_adj)
			distance_curr_node = distances[curr_node]
			weight_distance = int(contents_split[adj_node_int[0]][adj_node_int[1]])
			print("distance to curr node")
			print(distance_curr_node)
			print("edge distance")
			print(weight_distance)
			if distance_curr_node + weight_distance < distance_adj:
				distances[adj] = distance_curr_node + weight_distance
			print("distance to adj now")
			print(distances[adj])
			if distances[adj] < min_node_val:
				min_node_val = distance_adj
				min_node_loc = adj
	visited.add(curr_node)
	dijkstra(min_node_loc)

print(dijkstra("0,0"))










