inputs = []
requests = []
class Request:
	def __init__(self, name, floor1, floor2, time):
		self.name = name
		self.floor1= floor1
		self.floor2 = floor2
		self.time = time
# get input lines
with open('sample_input.txt', 'r') as ifile:
	for line in ifile:
		splits = line.rstrip().split(' ')
		inputs.append([splits[0], int(splits[3]), int(splits[9]), int(splits[-1])])
		req = Request(splits[0],
				int(splits[3]),
				int(splits[9]),
				int(splits[-1]))
		requests.append(req)

# naive scheduling algorithm: handle requests as they come in
time = 0
pos = 0
direction = 'up'
commands = ""

for req in requests:
	while time < req.time:
		commands+="i"
		time +=1 
	req_start_dir = req.floor1 - pos
	# get to starting floor of request
	if req_start_dir<0:
		req_start_dir = 'down'
	else:
		req_start_dir = 'up'
	if direction != req_start_dir:
		commands += 's'
		direction = req_start_dir
		time +=1 
	for i in range(abs(req.floor1-pos)):
		commands += 'm'
		time+=1
	# pick up person
	commands += 'i'
	time += 1

	# take person to destination
	req_dir = req.floor2-req.floor1
	if req_dir < 0:
		req_dir = 'down'
	else:
		req_dir = 'up'
	if direction != req_dir:
		direction = req_dir
		commands+= "s"
		time += 1

	for i in range(abs(req.floor2-req.floor1)):
		commands+="m"
		time += 1

	# drop off person
	commands += 'i'
	time +=1 
	pos = req.floor2

print commands
