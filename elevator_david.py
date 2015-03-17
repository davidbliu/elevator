inputs = []

# get input lines
with open('sample_input.txt', 'r') as ifile:
	for line in ifile:
		splits = line.rstrip().split(' ')
		inputs.append([splits[0], int(splits[3]), int(splits[9]), int(splits[-1])])


# naive scheduling algorithm: handle requests as they come in
time = 0
pos = 0
for i in inputs:
	floor_a = i[1]
	floor_b = i[2]
	t = i[3]
	dist_a = abs(floor_a-pos)
	print 'Move elevator 1 to floor '+str(floor_a) + ' at time '+str(time)
	time = time+dist_a
	# if you have to wait
	if t>time:
		time = t
	print 'Move elevator 1 to floor '+str(floor_b) + ' at time '+str(time)
	pos = floor_b
	time = time+abs(floor_a-floor_b)
