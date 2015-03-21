requests = []

class Request:
	def __init__(self, name, floor1, floor2, time):
		self.name = name
		self.floor1= floor1
		self.floor2 = floor2
		self.time = time
	def dir(self):
		if self.floor2 > self.floor1:
			return 1
		else:
			return -1
	def time_in_elevator(self):
		return self.time_exited - self.time_entered

	def total_time(self):
		return self.time_exited - self.time

class Elevator:
	maxfloor = 25
	def __init__(self):
		self.pos = 0
		self.direction = 1
		self.requests = []
	def move(self):
		self.pos += self.direction
		if self.pos >= Elevator.maxfloor or self.pos < 0:
			raise Exception("floor outside bounds")
	def idle(self, time, request_pool):
		# print 'idle at '+str(self.pos)+' '+str(self.direction)+' time is '+str(time)
		# check if people have to get out of elevator
		fulfilled_requests = [r for r in self.requests if r.floor2 == self.pos]
		for r in fulfilled_requests:
			r.time_exited = time
		requests = [r for r in self.requests if r.floor2 != self.pos]
		# get new requests
		new_requests = [r for r in request_pool if r.floor1 == self.pos and r.dir() == self.direction and r.time <= time]
		for r in new_requests:
			r.time_entered = time
		self.requests = requests+new_requests
		new_request_pool = [r for r in request_pool if r not in self.requests]
		return {'fulfilled':fulfilled_requests, 'new_pool': new_request_pool}
		
### LOAD REQUESTS INTO REQUESTS LIST
with open('sample_input.txt', 'r') as ifile:
	for line in ifile:
		splits = line.rstrip().split(' ')
		req = Request(splits[0],
				int(splits[3]),
				int(splits[9]),
				int(splits[-1]))
		requests.append(req)

def load_requests(filename):
	rs = []
	with open(filename, 'r') as ifile:
		for line in ifile:
			splits = line.rstrip().split(' ')
			req = Request(splits[0],
					int(splits[3]),
					int(splits[9]),
					int(splits[-1]))
			rs.append(req)
	return rs

### check inputted move sequence to see if valid
# assume use of only one elevator

def check_moves(moves, requests, elevator):
	time = 0
	for move in moves:
		requests = make_move(move, time, elevator, requests)
		time += 1
def make_move(move, time,  elevator, requests):
	if move == 'm':
		elevator.move()
	if move == 'i':
		# check if people need to get in or out of elevator
		data = elevator.idle(time, requests)
		requests = data['new_pool']
		for f in data['fulfilled']:
			print f.name + ' got dropped off at time '+str(time)
			print '     total time: '+str(f.total_time())+' time in elevator: '+str(f.time_in_elevator())
	if move == 's':
		elevator.direction *= -1
	return requests
	




