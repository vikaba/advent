from functools import reduce
import statistics

content_array = []
def file_read(fname):
        with open(fname) as f:    
                for line in f:
                	content_array.append(line.strip('\n'))

file_read('advent_3_input.txt')

def part_1():
	result_bin = ""
	for j in range(len(content_array[0])):
		letters_at_idx = [x[j] for x in content_array]
		result_bin += statistics.mode(letters_at_idx)

	int_result_bin = int(result_bin, 2)
	inv_result_bin = ''.join('1' if x == '0' else '0' for x in result_bin)
	inv_result_bin = int(inv_result_bin, 2)
	print(int_result_bin)
	print(inv_result_bin)
	print(int_result_bin*inv_result_bin)

def get_mode_at_idx(idx, rating, working_list):
	letters_at_idx = [x[idx] for x in working_list]
	mode = statistics.multimode(letters_at_idx)
	if rating == "o2" and len(mode) > 1:
		return '1'
	if rating == "co2" and len(mode) > 1:
		return '0'
	if rating == "o2":
		return mode[0]
	elif rating == "co2" and mode[0] == '0':
		return '1'
	return '0'

def remove_all(working_list, idx, char_to_select):
	return list(filter(lambda x: (x[idx] == char_to_select), working_list))

def part_2():
	iter_length = len(content_array[0])
	result_array_o2 = content_array.copy()
	result_array_co2 = content_array.copy()
	for i in range(iter_length):
		if (len(result_array_o2) < 1):
			break
		mode = get_mode_at_idx(i, "o2", result_array_o2)
		result_array_o2 = remove_all(result_array_o2, i, mode)
	for i in range(iter_length):
		if (len(result_array_co2) == 1):
			break
		mode = get_mode_at_idx(i, "co2", result_array_co2)
		result_array_co2 = remove_all(result_array_co2, i, mode)
	
	o2_int = int(result_array_o2[0], 2)
	co2_int = int(result_array_co2[0], 2)
	print(o2_int)
	print(co2_int)
	print(o2_int * co2_int)
part_2()




