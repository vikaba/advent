content_array = []
def file_read(fname):
        with open(fname) as f:    
                for line in f:
                	content_array.append(line.strip('\n'))

file_read('advent_1_input.txt')

increased = 0
previous = 0
previous_to_sub = 0
# 1 2 3
# 2 3 4
# 3 4 5
for i in range(len(content_array)):
	if i+1 >= len(content_array) or i+2 >= len(content_array):
		break
	if i == 0:
		window = int(content_array[i]) + int(content_array[i+1]) + int(content_array[i+2])
		previous = window
		previous_to_sub = int(content_array[i])
		continue
	else:
		new_window = previous - previous_to_sub + int(content_array[i+2])
		if new_window > previous:
			increased += 1
	previous_to_sub = int(content_array[i])
	previous = new_window

print(increased)
