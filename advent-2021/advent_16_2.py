a_file = open("advent_16_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

def huge_method(is_hex, hexa, curr_sum, looping):
	total_sum = curr_sum
	binary = ""
	if is_hex:
		binary = bin(int(hexa, 16))[2:].zfill(len(hexa) * 4)
	else:
		binary = hexa
	string_bin = str(binary)
	version = get_packet_version(string_bin)

	type_id = get_packet_type(string_bin)
	if type_id == 4:
		packet = string_bin[6:]
		curr_idx = 0
		done = False
		#final_bin = ""
		while not done:
			if packet[curr_idx] == "1":
				#final_bin += string_bin[curr_idx+1:curr_idx+5]
			else:
				#final_bin += string_bin[curr_idx+1:curr_idx+5]
				done = True
			curr_idx += 5
		end_idx = curr_idx
		return [curr_sum+version, end_idx]
	else:
		length_type_id = string_bin[6]
		if length_type_id == "0":
			subpacket_length = int(string_bin[7:22], 2)
			packets = string_bin[22:22+subpacket_length]

		else:
