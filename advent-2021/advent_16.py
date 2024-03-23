a_file = open("advent_16_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

def literal_val_packet(string_bin):
	curr_idx = 0
	done = False
	final_bin = ""
	while not done:
		if string_bin[curr_idx] == "1":
			final_bin += string_bin[curr_idx+1:curr_idx+5]
		else:
			final_bin += string_bin[curr_idx+1:curr_idx+5]
			done = True
		curr_idx += 5
	end_idx = curr_idx
	return int(final_bin, 2)

def literal_val_packet_end_idx(string_bin):
	curr_idx = 0
	done = False
	while not done:
		if string_bin[curr_idx] == "1":
		else:
			done = True
		curr_idx += 5
	return curr_idx

def operator_val_packet_end_idx(length_type_id, string_bin):
	if length_type_id == "0":
		subpacket_length = int(string_bin[0:15], 2)
		return subpacket_length
	else:
		num_of_subpackets = int(string_bin[0:11], 2)
		total_length = len(string_bin[11:])
		packet_lengths = total_length / num_of_subpackets
		packets = string_bin[11:]
		idx = 0
		packet_num = 1
		while packet_num <= num_of_subpackets:
			packet = packets[idx:11]
			curr_sum += version_sum(False, packet, curr_sum)
			idx += packet_lengths
			packet_num += 1

def operator_packet(length_type_id, string_bin, curr_sum):
	if length_type_id == "0":
		subpacket_length = int(string_bin[0:15], 2)
		packets = string_bin[15:]
		packet_index = 15
		curr_length = 0
		while curr_length < subpacket_length:
			packet = packets[packet_index:]
			packet_type = get_packet_type(packet)
			if packet_type == 4:
				end_idx = literal_val_packet_end_idx(packet)
			else:
				length_type_id = packet[6]
				end_idx = operator_val_packet_end_idx(length_type_id, packet[7:])
			curr_sum += version_sum(packets[packet_index:end_idx])
			curr_length += end_idx
			start_idx = end_idx


	else:
		num_of_subpackets = int(string_bin[0:11], 2)
		total_length = len(string_bin[11:])
		packet_lengths = total_length / num_of_subpackets
		packets = string_bin[11:]
		idx = 0
		packet_num = 1
		while packet_num <= num_of_subpackets:
			packet = packets[idx:11]
			curr_sum += version_sum(False, packet, curr_sum)
			idx += packet_lengths
			packet_num += 1

def get_packet_version(packet_bin):
	return int(packet_bin[0:3], 2)

def get_packet_type(packet_bin):
	return int(packet_bin[3:6], 2)
 
def version_sum(is_hex, hexa, curr_sum):
	binary = ""
	if is_hex:
		binary = bin(int(hexa, 16))[2:].zfill(len(hexa) * 4)
	else:
		binary = hexa
	string_bin = str(binary)
	version = get_packet_version(string_bin)
	type_id = get_packet_type(string_bin)
	if type_id == 4:
		literal_val = literal_val_packet(string_bin[6:])
		return curr_sum + version
	elif type_id is not None:
		length_type_id = string_bin[6]
		return curr_sum + version + operator_packet(length_type_id, string_bin[7:])
	else:
		return None

version_sum("D2FE28")



examples = ["8A004A801A8002F478",
 "620080001611562C8802118E34",
 "C0015000016115A2E0802F182340",
 "A0016C880162017C3686B18A3D4780"]