inputs = []

# get input lines
with open('sample_input.txt', 'r') as ifile:
	for line in ifile:
		splits = line.rstrip().split(' ')
		inputs.append([splits[0], int(splits[3]), int(splits[9]), int(splits[-1])])


# naive scheduling algorithm: handle requests as they come in
time = 0
pos = 0
for ind in range(0, len(inputs)):
	i = inputs[ind]
	floor_a = i[1]
	floor_b = i[2]
	t = i[3]
	dist_a = abs(floor_a-pos)
	direction = 'down'
	if floor_b>floor_a:
		direction = 'up'
	print 'Move elevator 1 to floor '+str(floor_a) + ' at time '+str(time) + ' going '+direction
	time = time+dist_a
	# if you have to wait
	if t>time:
		time = t

	direction = 'down'
	if ind<len(inputs)-1 and inputs[ind+1][1] > floor_b:
		direction = 'up'
	# drop off at desired floor, then set the direction to go in the next floor a
	print 'Move elevator 1 to floor '+str(floor_b) + ' at time '+str(time) + ' going '+direction
	pos = floor_b
	time = time+abs(floor_a-floor_b)
