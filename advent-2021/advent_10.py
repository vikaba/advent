from collections import deque
import math

a_file = open("advent_10_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

openers = ["{", "<", "(", "["]
match_map = {"{": "}", "[": "]", "(": ")", "<": ">"}
bad_closers = []
incomplete_lines = []

def part_1():
	for line in contents_split:
		stack = deque()
		corrupted_line = False
		for char in line:
			if char in openers:
				stack.append(char)
			else:
				stack_char = stack[-1]
				if match_map[stack_char] == char:
					stack.pop()
				else:
					bad_closers.append(char)
					corrupted_line = True
					break
		if not corrupted_line:
			incomplete_lines.append(line)

	score_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
	total = 0
	for closer in bad_closers:
		total += score_map[closer]
	# print(total)

def part_2():
	incomplete_completers = []
	for line in incomplete_lines:
		stack = deque()
		for char in line:
			if char in openers:
				stack.append(char)
			else:
				stack_char = stack[-1]
				if match_map[stack_char] == char:
					stack.pop()
		closing_string = ""
		while stack:
			opener = stack.pop()
			closing_string += match_map[opener]
		incomplete_completers.append(closing_string)

	score_map = {")": 1, "]": 2, "}": 3, ">": 4}
	totals = []
	for completer in incomplete_completers:
		total = 0
		for char in completer:
			total = total * 5
			total += score_map[char]
		totals.append(total)
	# print(totals)
	sorted_totals = sorted(totals)
	middle_score = sorted_totals[math.floor(len(sorted_totals)/2)]
	print("middle score: " + str(middle_score))

part_1()
part_2()



