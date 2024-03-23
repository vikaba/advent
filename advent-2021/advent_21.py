from itertools import cycle
from functools import cache

example = "Player 1 starting position: 4 \n Player 2 starting position: 8"
actual = "Player 1 starting position: 10 \n Player 2 starting position: 9"
player1_pos = 0
player2_pos = 0

def parse_player_start(string):
	global player1_pos, player2_pos
	split = string.splitlines()
	player1_pos = int(split[0].split(":")[1].strip())
	player2_pos = int(split[1].split(":")[1].strip())

parse_player_start(example)

player_pos_map = {"p1": player1_pos, "p2": player2_pos}
player_score_map = {"p1": 0, "p2": 0}

def has_won():
	if player_score_map["p1"] >= 1000:
		return "p1"
	elif player_score_map["p2"] >= 1000:
		return "p2"
	else:
		return False

def change_position(player, roll_sum):
	new_pos = player_pos_map[player] + roll_sum
	if new_pos > 10:
		new_pos = new_pos % 10
		if new_pos == 0:
			new_pos = 10
	# print("curr pos: " + str(player_pos_map[player]))
	# print("new pos: " + str(new_pos))
	player_pos_map[player] = new_pos
	player_score_map[player] += new_pos
	# print("new score: " + str(player_score_map[player]))

dice = cycle(list(range(1, 101)))
def play_game():
	curr_player = "p1"
	rolls = 0
	while True:
		# print(curr_player)
		winner = has_won()
		if winner:
			print("winner: " + winner)
			print("score: " + str(player_score_map[winner]))
			loser = "p2"
			if winner == "p2":
				loser = "p1"
			print("loser: " + loser)
			print("score: " + str(player_score_map[loser]))
			print("rolls: " + str(rolls))
			print(player_score_map[loser] * rolls)
			break
		n1 = next(dice)
		# print(n1)
		n2 = next(dice)
		n3 = next(dice)
		curr_roll = n1 + n2 + n3
		# print("roll: " + str(curr_roll))
		change_position(curr_player, curr_roll)
		if curr_player == "p1":
			curr_player = "p2"
		else:
			curr_player = "p1"
		rolls += 3

#play_game()

p1_wins = 0
p2_wins = 0

class Game_State:
  def __init__(self, p1_pos, p2_pos, p1_score=0, p2_score=0, roll=0):
  	self.p1_score = p1_score
  	self.p2_score = p2_score
  	self.p1_pos = p1_pos
  	self.p2_pos = p2_pos
  	self.winner = False
  	self.state1 = None
  	self.state2 = None
  	self.state3 = None
  	self.state4 = None
  	self.state5 = None
  	self.state6 = None
  	self.state7 = None
  	self.state8 = None
  	self.state9 = None
  	self.roll = roll

  @cache
  def get_new_pos(self, curr_pos, roll_sum):
  	new_pos = curr_pos + roll_sum
  	if new_pos > 10:
  		new_pos = new_pos % 10
  		if new_pos == 0:
  			new_pos = 10
  	return new_pos
  
  @cache
  def state_won(self, node):
  	global p1_wins
  	global p2_wins
  	if node.p1_score >= 21:
  		node.winner = "p1"
  		p1_wins += 1
  		return True
  	elif node.p2_score >= 21:
  		node.winner = "p2"
  		p2_wins += 1
  		return True
  	return False

  @cache
  def add_new_states(self):
  		# if self.winner:
  		# 	return []
	  	self.state1 = Game_State(self.get_new_pos(self.p1_pos, 1), self.get_new_pos(self.p2_pos, 1), self.p1_score, self.p2_score, self.roll+1)
	  	self.state2 = Game_State(self.get_new_pos(self.p1_pos, 1), self.get_new_pos(self.p2_pos, 2), self.p1_score, self.p2_score, self.roll+1)
	  	self.state3 = Game_State(self.get_new_pos(self.p1_pos, 1), self.get_new_pos(self.p2_pos, 3), self.p1_score, self.p2_score, self.roll+1)
	  	self.state4 = Game_State(self.get_new_pos(self.p1_pos, 2), self.get_new_pos(self.p2_pos, 1), self.p1_score, self.p2_score, self.roll+1)
	  	self.state5 = Game_State(self.get_new_pos(self.p1_pos, 2), self.get_new_pos(self.p2_pos, 2), self.p1_score, self.p2_score, self.roll+1)
	  	self.state6 = Game_State(self.get_new_pos(self.p1_pos, 2), self.get_new_pos(self.p2_pos, 3), self.p1_score, self.p2_score, self.roll+1)
	  	self.state7 = Game_State(self.get_new_pos(self.p1_pos, 3), self.get_new_pos(self.p2_pos, 1), self.p1_score, self.p2_score, self.roll+1)
	  	self.state8 = Game_State(self.get_new_pos(self.p1_pos, 3), self.get_new_pos(self.p2_pos, 2), self.p1_score, self.p2_score, self.roll+1)
	  	self.state9 = Game_State(self.get_new_pos(self.p1_pos, 3), self.get_new_pos(self.p2_pos, 3), self.p1_score, self.p2_score, self.roll+1)
	  	# print(self.roll)
	  	print("p1 wins: " + str(p1_wins))
	  	print("p2_wins: " + str(p2_wins))
	  	# print("mod")
	  	# print((self.roll+1) % 3)
	  	if (self.roll+1) % 3 == 0:
	  		self.state1.p1_score += self.state1.p1_pos
	  		self.state1.p2_score += self.state1.p2_pos
	  		if not self.state_won(self.state1):
	  			self.state1.add_new_states()

	  		self.state2.p1_score += self.state2.p1_pos
	  		self.state2.p2_score += self.state2.p2_pos
	  		if not self.state_won(self.state2):
	  			self.state2.add_new_states()

	  		self.state3.p1_score += self.state3.p1_pos
	  		self.state3.p2_score += self.state3.p2_pos
	  		if not self.state_won(self.state3):
	  			self.state3.add_new_states()

	  		self.state4.p1_score += self.state4.p1_pos
	  		self.state4.p2_score += self.state4.p2_pos
	  		if not self.state_won(self.state4):
	  			self.state4.add_new_states()

	  		self.state5.p1_score += self.state5.p1_pos
	  		self.state5.p2_score += self.state5.p2_pos
	  		if not self.state_won(self.state5):
	  			self.state5.add_new_states()

	  		self.state6.p1_score += self.state6.p1_pos
	  		self.state6.p2_score += self.state6.p2_pos
	  		if not self.state_won(self.state6):
	  			self.state6.add_new_states()

	  		self.state7.p1_score += self.state7.p1_pos
	  		self.state7.p2_score += self.state7.p2_pos
	  		if not self.state_won(self.state7):
	  			self.state7.add_new_states()

	  		self.state8.p1_score += self.state8.p1_pos
	  		self.state8.p2_score += self.state8.p2_pos
	  		if not self.state_won(self.state8):
	  			self.state8.add_new_states()

	  		self.state9.p1_score += self.state9.p1_pos
	  		self.state9.p2_score += self.state9.p2_pos
	  		if not self.state_won(self.state9):
	  			self.state9.add_new_states()
	  	else:
	  		self.state1.add_new_states()
	  		self.state2.add_new_states()
	  		self.state3.add_new_states()
	  		self.state4.add_new_states()
	  		self.state5.add_new_states()
	  		self.state6.add_new_states()
	  		self.state7.add_new_states()
	  		self.state8.add_new_states()
	  		self.state9.add_new_states()


def play_game_2():
	state = Game_State(player1_pos, player2_pos)
	new_states = state.add_new_states()
	# while len(new_states) != 0:
	# 	# print(new_states)
	# 	new_new_states = []
	# 	for new_state in new_states:
	# 		result = new_state.add_new_states()
	# 		new_new_states += result
	# 	new_states = new_new_states
	print("p1 wins: " + str(p1_wins))
	print("p2_wins: " + str(p2_wins))

play_game_2()
# print(p1_wins)
# print(p2_wins)


