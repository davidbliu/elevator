import random
from sets import Set
male_names = []
female_names = []
names = []
# import names 
with open('male_names.txt', 'r') as ifile:
	for name in ifile:
		male_names.append(name.split(' ')[0])
		names.append(name.split(' ')[0])
with open('female_names.txt', 'r') as ifile:
	for name in ifile:
		female_names.append(name.split(' ')[0])
		names.append(name.split(' ')[0])

input_lines = []

def generate_uniform_input(length):
	maxtime = 50
	maxfloor = 24
	times = [random.randint(0, maxtime) for x in range(length)]
	previous_names = Set()
	times.sort()
	for time in times:
		floor_1 = random.randint(0, maxfloor)
		floor_2 = random.randint(0, maxfloor)
		while floor_2 == floor_1:
			floor_2 = random.randint(0, maxfloor)
		name = random.sample(names, 1)[0]
		while name in previous_names:
			name = random.sample(names, 1)[0]
		previous_names.add(name)
		input_string = name + ' at floor '+str(floor_1)+' wants to go to floor '+str(floor_2)+' at time '+str(time)
		print input_string

generate_uniform_input(15)
