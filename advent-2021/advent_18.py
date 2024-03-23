import ast
import math

a_file = open("advent_18_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

def find_split(expr, idxs):
	if not isinstance(expr, list):
		if expr >= 10:
			# print(idxs)
			# print([math.floor(int(expr)/2), math.ceil(int(expr)/2)])
			return {"final": [math.floor(expr/2), math.ceil(expr/2)], "idxs": idxs}
		else:
			return
	else:
		for inner in range(len(expr)):
			final = find_split(expr[inner], idxs + [inner])
			if final:
				return final

def amend_list(idxs, exprs, insert_elem, add, left):
	if len(idxs) > 1:
		curr_idx = idxs.pop(0)
		amend_list(idxs, exprs[curr_idx], insert_elem, add, left)
	elif len(idxs) == 1:
		curr_idx = idxs.pop(0)
		# print(exprs[curr_idx])
		# print("insert elem")
		# print(insert_elem)
		if isinstance(exprs[curr_idx], list) and not add:
			# print("1")
			exprs[curr_idx] = insert_elem
		elif not isinstance(exprs[curr_idx], list):
			# print("2")
			if add:
				exprs[curr_idx] += insert_elem
			else:
				exprs[curr_idx] = insert_elem
		elif isinstance(exprs[curr_idx], list) and add:
			# print("3")
			if left:
				if add:
					exprs[curr_idx][1] += insert_elem
				else:
					exprs[curr_idx][1] = insert_elem
			else: 
				if add:
					exprs[curr_idx][0] += insert_elem
				else:
					exprs[curr_idx][0] = insert_elem
		return

def check_if_int_list(pair):
	return not isinstance(pair[0], list) and not isinstance(pair[1], list)

def find_explode(expr, level, idxs, nums):
	if not isinstance(expr, list):
		nums.append({"num": expr, "idxs": idxs})
		# print(nums)
	elif isinstance(expr, list) and check_if_int_list(expr) and level == 4:
		# print("found")
		# print(idxs)
		nums.append({"found": expr, "idxs": idxs})
	else:
		for inner in range(len(expr)):
			# print("inner")
			# print(expr[inner])
			find_explode(expr[inner], level + 1, idxs + [inner], nums)
		return nums


# find_explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], 0, [], [])

# def recurse_print(expr, level):
# 	if not isinstance(expr, list):
# 		return
# 	else:
# 		for inner in expr:
# 			print("level:")
# 			print(level)
# 			print("inner:")
# 			print(inner)
# 			recurse_print(inner, level + 1) 

# recurse_print([[[[0,7],4],[7,[[8,4],9]]],[1,1]], 0)

def get_explode_found(explode_result):
	for idx in range(len(explode_result)):
		if "found" in explode_result[idx]:
			return idx
	return "none"

def calc_magnitude(expr):
	if not isinstance(expr, list):
		return expr
	elif isinstance(expr, list) and check_if_int_list(expr):
		return expr[0] * 3 + expr[1] * 2
	else:
		return 3 * calc_magnitude(expr[0]) + 2 * calc_magnitude(expr[1])


def part_1():
	curr_list = ast.literal_eval(contents_split[0])
	for line in range(1, len(contents_split)):
		list_expr = ast.literal_eval(contents_split[line])
		curr_list = [curr_list]
		curr_list.append(list_expr)
		# print("added")
		# print(curr_list)


		explode_result = find_explode(curr_list, 0, [], [])
		explode_found_obj_idx = get_explode_found(explode_result)
		split_result = find_split(curr_list, [])
		while explode_found_obj_idx != "none" or split_result:
			if explode_found_obj_idx != "none":
				# print("exploded")
				# print(explode_result)
				# print("exploded which")
				explode_found_obj = explode_result[explode_found_obj_idx]
				# print(explode_found_obj)
				explode_found_obj_val = explode_found_obj["found"].copy()
				if explode_found_obj_idx > 0:
					previous = explode_result[explode_found_obj_idx-1]
					# print("previous")
					# print(previous)
					amend_list(previous['idxs'], curr_list, explode_found_obj_val[0], True, True)
				if explode_found_obj_idx < len(explode_result)-1:
					# print("next one")
					next_one = explode_result[explode_found_obj_idx+1]
					# print(next_one)
					amend_list(next_one['idxs'], curr_list, explode_found_obj_val[1], True, False)
					# print(curr_list)
				amend_list(explode_found_obj['idxs'], curr_list, 0, False, False)
				# print(curr_list)
			elif split_result:
				# print("split")
				amend_list(split_result["idxs"], curr_list, split_result["final"], False, False)
				# print(curr_list)

			explode_result = find_explode(curr_list, 0, [], [])
			explode_found_obj_idx = get_explode_found(explode_result)
			split_result = find_split(curr_list, [])

	print(curr_list)
	print(calc_magnitude(curr_list))

def part_2():
	max_mag = 0
	for line in range(len(contents_split)):
		curr_list = ast.literal_eval(contents_split[line])
		for line_2 in range(len(contents_split)):
			if line != line_2:
				curr_list = ast.literal_eval(contents_split[line])
				list_expr = ast.literal_eval(contents_split[line_2])
				curr_list = [curr_list]
				curr_list.append(list_expr)
				# print("added")
				# print(curr_list)


				explode_result = find_explode(curr_list, 0, [], [])
				explode_found_obj_idx = get_explode_found(explode_result)
				split_result = find_split(curr_list, [])
				while explode_found_obj_idx != "none" or split_result:
					if explode_found_obj_idx != "none":
						# print("exploded")
						# print(explode_result)
						# print("exploded which")
						explode_found_obj = explode_result[explode_found_obj_idx]
						# print(explode_found_obj)
						explode_found_obj_val = explode_found_obj["found"].copy()
						if explode_found_obj_idx > 0:
							previous = explode_result[explode_found_obj_idx-1]
							# print("previous")
							# print(previous)
							amend_list(previous['idxs'], curr_list, explode_found_obj_val[0], True, True)
						if explode_found_obj_idx < len(explode_result)-1:
							# print("next one")
							next_one = explode_result[explode_found_obj_idx+1]
							# print(next_one)
							amend_list(next_one['idxs'], curr_list, explode_found_obj_val[1], True, False)
							# print(curr_list)
						amend_list(explode_found_obj['idxs'], curr_list, 0, False, False)
						# print(curr_list)
					elif split_result:
						# print("split")
						amend_list(split_result["idxs"], curr_list, split_result["final"], False, False)
						# print(curr_list)

					explode_result = find_explode(curr_list, 0, [], [])
					explode_found_obj_idx = get_explode_found(explode_result)
					split_result = find_split(curr_list, [])

				magnitude = calc_magnitude(curr_list)
				if magnitude > max_mag:
					max_mag = magnitude

	print(max_mag)

part_2()







