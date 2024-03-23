a_file = open("advent_4_input.txt")
file_contents = a_file.read()
contents_split = file_contents.splitlines()

count = 0
called_nums = []
boards = []
curr_board = []
for line in contents_split:
	if count == 0:
		called_nums = line.split(",")
		count += 1
		continue
	elif line != '':
		curr_board.append(list(filter(lambda x: (x != ''), line.split(" "))))
	elif count != 1:
		boards.append(curr_board)
		curr_board = []
	count += 1
boards.append(curr_board)

def mark_on_board(num, board):
	# print(num)
	rows = []
	columns = []
	for row in range(len(board)):
		for column in range(len(board[0])):
			if board[row][column] == num:
				board[row][column] = 'X'
				rows.append(row)
				columns.append(column)
	# print_board_pretty(board)
	return [rows, columns]

def check_row(row, board):
	# print(board[row])
	# print(len(set(board[row])))
	# print(board[row][0])
	if len(set(board[row])) == 1 and board[row][0] == 'X':
		#print(True)
		return True

def check_vertical(column, board):
	for row in range(len(board)):
		if board[row][column] != 'X':
			return False
	return True

def print_board_pretty(board):
	for row in board:
		print(row)

def sum_unmarked(board):
	total = 0
	for row in board:
		for num in row:
			if num != 'X':
				total += int(num)
	return total


def sum_unmarked(board):
	total = 0
	for row in board:
		for num in row:
			if num != 'X':
				total += int(num)
	return total

winning_board = []
winning_num = 0
for num in called_nums:
	if len(winning_board) < len(boards):
		for board in boards:
			if board[0][0] != 'W':
				rows_cols = mark_on_board(num, board)
				for row in rows_cols[0]:
					if check_row(row, board):
						winning_board.append(board)
						if len(winning_board) < len(boards):
							board[0][0] = 'W'
						winning_num = num
						break
				if board[0][0] != 'W':
					for col in rows_cols[1]:
						if check_vertical(col, board):
							winning_num = num
							winning_board.append(board)
							if len(winning_board) < len(boards):
								board[0][0] = 'W'
							break

print(winning_num)
winning_sum = sum_unmarked(winning_board[-1])
print(winning_sum)
#print(winning_num * winning_sum)

