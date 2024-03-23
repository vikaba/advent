a_file = open("advent_2_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

def points_won(p1_choice, p2_choice):
	# A = rock, B = paper, C = scissors
	# X = rock (1), Y = paper (2), Z = scissors (3)
	# 0 = lost, 3 = draw, 6 = I WON!
	# X = lose, Y = draw, Z = win

	winning_opts = {"A": "Y", "B": "Z", "C": "X"}
	equal = { "A": "X", "B": "Y", "C": "Z"}
	points = { "X": 1, "Y": 2, "Z": 3}

	if equal[p1_choice] == p2_choice:
		return points[p2_choice] + 3
	elif winning_opts[p1_choice] == p2_choice:
		return points[p2_choice] + 6
	else:
		return points[p2_choice]

def points_won_2(p1_choice, p2_choice):
	# A = rock, B = paper, C = scissors
	# X = rock (1), Y = paper (2), Z = scissors (3)
	# 0 = lost, 3 = draw, 6 = I WON!
	# X = lose, Y = draw, Z = win

	winning_opts = {"A": "Y", "B": "Z", "C": "X"}
	equal = { "A": "X", "B": "Y", "C": "Z"}
	points = { "X": 1, "Y": 2, "Z": 3}
	opts = {"X", "Y", "Z"}

	if p2_choice == "Y":
		return 3 + points[equal[p1_choice]]
	elif p2_choice == "Z":
		return points[winning_opts[p1_choice]] + 6
	else:
		tie_win = {winning_opts[p1_choice], equal[p1_choice]}
		# print(tie_win)
		# print(opts)
		diff = opts - tie_win
		# print(diff)
		losing = diff.pop()
		return points[losing]

total = 0
for line in contents_split:
	round_split = line.split(" ")
	p1_choice = round_split[0]
	p2_choice = round_split[1]
	total += points_won_2(p1_choice, p2_choice)
	# print(points_won_2(p1_choice, p2_choice))

print(total)
