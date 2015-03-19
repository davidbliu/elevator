import random

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
# generate input
time = 0
for i in range(10):
	floor_1 = random.randint(0, 50)
	floor_2 = random.randint(0, 50)
	name = random.sample(names, 1)[0]
	time = time + random.randint(0, 25)
	input_string = name + ' at floor '+str(floor_1)+' wants to go to floor '+str(floor_2)+' at time '+str(time)
	print input_string

