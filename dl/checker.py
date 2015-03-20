requests = []

class Request:
	def __init__(self, name, floor1, floor2, time):
		self.name = name
		self.floor1= floor1
		self.floor2 = floor2
		self.time = time

class Elevator:
	maxfloor = 25
	def __init__(self):
		self.pos = 0
		self.direction = 1
		self.requests = []
	def move(self):
		self.pos += self.direction
		if pos >= maxfloor or pos < 0:
			raise Exception("floor outside bounds")
	def idle(self):
		# check if people have to get out of elevator
		for request in self.requests:
			

### LOAD REQUESTS INTO REQUESTS LIST
with open('sample_input.txt', 'r') as ifile:
	for line in ifile:
		splits = line.rstrip().split(' ')
		inputs.append([splits[0], int(splits[3]), int(splits[9]), int(splits[-1])])
		req = Request(splits[0],
				int(splits[3]),
				int(splits[9]),
				int(splits[-1]))
		requests.append(req)

### check inputted move sequence to see if valid
# assume use of only one elevator
def check_moves(moves, requests):
	time = 0
	for move in moves:
		make_move(move, elevator, request)
def make_move(move, elevator, requests):
	if move == 'm':
		elevator.move()
	if move == 'i':
		# check if people need to get in or out of elevator
	if move == 's':
		elevator.direction *= -1
	time += 1