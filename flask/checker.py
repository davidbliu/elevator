from seeds import *

class Elevator:
	maxfloor = 25
	def __init__(self, name = "1"):
		self.name = name
		self.pos = 0
		self.direction = 1
		self.requests = []
		self.fulfilled_requests = []
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
			r.elevator = self.name
		self.requests = requests+new_requests
		new_request_pool = [r for r in request_pool if r not in self.requests]
		self.fulfilled_requests += fulfilled_requests
		return {'fulfilled':fulfilled_requests, 'new_pool': new_request_pool}

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

 

def test_solution(solution, challenge):
	print 'testing your solution'
	challenge_requests = challenge.requests()
	e1_instructions = solution[0]
	e2_instructions = solution[1]
	e1_instructions = 'iimmmmmmmmmmmmmmmmmmmmmmmmsimmmmmmmmmmmmmmismmmimmmmmmmmmismmmmmmmmmmmmmmmmmmsimmmmmmmismimmmmmmismmmmmmmmmmmmmsimmmmmmmmmmmmmmmmi'
	e2_instructions = 'iiiiiiiiiiiiiiiiiiiiimmmmimmmmmmmmmmmmmmmmismmmmmmmmmmmmmmmmmmmsimmmmmmmmmmmimmmmmmmmsimmmmmimmmmmmmmmmmsimmmmmmmmmmmmmismmmmmmmmmmsimmmmmmmmmi'
	max_time = max(len(e1_instructions), len(e2_instructions))
	e1 = Elevator('1')
	e2 = Elevator('2')
	check_moves(e1_instructions, challenge_requests, e1)
	# remove handled requests
	remaining_requests = [r for r in challenge_requests if not r.fulfilled()]
	check_moves(e2_instructions, remaining_requests, e2)

	print 'here are some lengths you should know'
	for req in challenge_requests:
		outstring = req.name+' spent '
		outstring += str(req.time_in_elevator())
		outstring += ' waited '+str(req.total_time())
		outstring += ' in '+str(req.elevator)
		print outstring
	return e1.fulfilled_requests+e2.fulfilled_requests




	




