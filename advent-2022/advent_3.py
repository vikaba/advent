import string
import math

a_file = open("advent_3_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

def part_1():
	total = 0
	for line in contents_split:
		half_len = math.floor(len(line)/2)
		split_1 = line[0:half_len]
		split_2 = line[half_len:len(line)]
		same = list(set(split_1).intersection(split_2))
		same_letter = same[0]
		total += (list('0') + list(string.ascii_letters)).index(same_letter)
		return total

# print(part_1())

def part_2():
	counter = 0
	group = []
	total = 0
	for line in contents_split:
		# print(line)
		# print(counter)
		if counter < 2:
			group.append(list(line))
			counter += 1
		else:
			group.append(list(line))
			# print(group)
			same = list(set(group[0]).intersection(group[1]).intersection(group[2]))
			same_letter = same[0]
			# print(same_letter)
			total += (list('0') + list(string.ascii_letters)).index(same_letter)
			group = []
			counter = 0
	return total

print(part_2())


