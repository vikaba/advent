import itertools
import operator

food_totals = []
def file_read(fname):
        with open(fname) as f:
                curr_total = 0   
                for line in f:
                        if line == '\n':
                                food_totals.append(curr_total)
                                curr_total = 0
                        else:
                                food_item = int(line.strip('\n'))
                                curr_total += food_item

file_read('advent_1_input.txt')
food_totals.sort(reverse=True)
print(food_totals[0:3])
print(sum(food_totals[0:3]))


