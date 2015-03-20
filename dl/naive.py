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
commands = []

for req in requests:
	while time < req.time:
		commands.append('i')
		time +=1 
	req_dir = req.floor2-req.floor1
	if req_dir < 0:
		req_dir = 'down'
	else:
		req_dir = 'up'
	if direction != req_dir:
		commands.append('s')
		time += 1
	for i in range(abs(req.floor2-req.floor1)):
		commands.append('m')
		time += 1

print commands
