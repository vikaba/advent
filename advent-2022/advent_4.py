a_file = open("advent_4_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

count = 0
for line in contents_split:
	split_pairs = line.split(",")
	elf_1 = split_pairs[0]
	elf_2 = split_pairs[1]
	e1_split = elf_1.split("-")
	e2_split = elf_2.split("-")
	e1_1 = int(e1_split[0])
	e1_2 = int(e1_split[1])
	e2_1 = int(e2_split[0])
	e2_2 = int(e2_split[1])

	# if (e1_1 <= e2_1 and e1_2 >= e2_2) or (e2_1 <= e1_1 and e1_2 <= e2_2):
	# 	count += 1

	if (e1_1 <= e2_1 and e1_2 <= e2_2 and e2_1 <= e1_2) \
		or (e2_1 <= e1_1 and e2_2 <= e1_2 and e1_1 <= e2_2) \
		or ((e1_1 <= e2_1 and e1_2 >= e2_2) or (e2_1 <= e1_1 and e1_2 <= e2_2)):
		count += 1
		# print(line)

	# e1_1 <= e2_1 and e1_2 <= e2_2
	# e2_1 <= e1_1 and e2_2 <= e1_2

print(count)
# 5 .. 7
#      7 ... 9

# 2 ..... 8
#   3...7

# 2 ..... 6
#    4 .......8

#    4 .......8
# 2 ..... 6


# 2 ... 4
#          6 ... 8


# 2 .......... 8
#    3 ......7 
