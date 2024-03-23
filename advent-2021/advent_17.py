def in_target(x, y, target_x1, target_x2, target_y1, target_y2):
	min_x = min(target_x1, target_x2)
	max_x = max(target_x1, target_x2)
	min_y = min(target_y1, target_y2)
	max_y = max(target_y1, target_y2) 
	if x > max_x or y < min_y:
		return "oob"
	elif min_x <= x <= max_x and min_y <= y <= max_y:
		return "in target"
	else:
		return "go"

def get_highest_y(x_vel, y_vel, target_x1, target_x2, target_y1, target_y2):
	x_pos = 0
	y_pos = 0
	x_velocity = x_vel
	y_velocity = y_vel
	y_max = -100000
	done = "go"
	while done == "go":
		done = in_target(x_pos, y_pos, target_x1, target_x2, target_y1, target_y2)
		x_pos += x_velocity
		y_pos += y_velocity
		if y_pos > y_max:
			y_max = y_pos
		if x_velocity < 0:
			x_velocity +=1
		elif x_velocity > 0:
			x_velocity = x_velocity - 1
		y_velocity = y_velocity - 1
	
	if done == "in target":
		return y_max
	else:
		return "no"

def try_many_velocities(target_x1, target_x2, target_y1, target_y2):
	curr_max = 0
	highest_y = 0
	total = 0
	for vel_x in range(300):
		# print(vel_x)
		for vel_y in range(-112, 1000):
			highest_y = get_highest_y(vel_x, vel_y, target_x1, target_x2, target_y1, target_y2)
			if highest_y != "no":
				total += 1
				if highest_y > curr_max:
					curr_max = highest_ys
	print("highest y: " + str(curr_max))
	print("total valid: " + str(total))

sample = "target area: x=20..30, y=-10..-5"
actual_input = "target area: x=156..202, y=-110..-69"
#try_many_velocities(20, 30, -10, -5)
try_many_velocities(156, 202, -110, -69)