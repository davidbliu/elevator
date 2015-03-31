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
		# for f in data['fulfilled']:
		# 	print f.name + ' got dropped off at time '+str(time)
		# 	print '     total time: '+str(f.total_time())+' time in elevator: '+str(f.time_in_elevator())
	if move == 's':
		elevator.direction *= -1
	return requests

def check_solution(moves, requests, elevators):
	assert len(moves)==len(elevators)
	time = 0
	for i in range(max(len(moves[1]), len(moves[0]))):
		# allow each elevator to move once
		for i in range(0, len(moves)):
			movelist = moves[i]
			elevator = elevators[i]
			if time < len(movelist):
				move = movelist[time]
				requests = make_move(move, time, elevator, requests)
		time += 1
def test_solution(solution, challenge):
	challenge_requests = challenge.requests()
	e1_instructions = solution[0]
	e2_instructions = solution[1]
	e1_instructions = 'iimmmmmmmmmmmmmmmmmmmmmmmmsimmmmmmmmmmmmmmismmmimmmmmmmmmismmmmmmmmmmmmmmmmmmsimmmmmmmismimmmmmmismmmmmmmmmmmmmsimmmmmmmmmmmmmmmmi'
	e2_instructions = 'iiiiiiiiiiiiiiiiiiiiimmmmimmmmmmmmmmmmmmmmismmmmmmmmmmmmmmmmmmmsimmmmmmmmmmmimmmmmmmmsimmmmmimmmmmmmmmmmsimmmmmmmmmmmmmismmmmmmmmmmsimmmmmmmmmi'
	e1 = Elevator('1')
	e2 = Elevator('2')
	moves = [e1_instructions, e2_instructions]
	elevators = [e1, e2]
	check_solution(moves, challenge_requests, elevators)

	# print 'here are some lengths you should know'
	# for req in challenge_requests:
	# 	outstring = req.name+' spent '
	# 	outstring += str(req.time_in_elevator())
	# 	outstring += ' waited '+str(req.total_time())
	# 	outstring += ' in '+str(req.elevator)
	# 	print outstring
	return e1.fulfilled_requests+e2.fulfilled_requests

def get_solution_stats(solution, challenge):
	fulfilled_requests = test_solution(solution, challenge)
	length = len(fulfilled_requests)
	wait_times_for_elevator = [(x.total_time()-x.time_in_elevator()) for x in fulfilled_requests]
	avg_wait_time_for_elevator = sum(wait_times_for_elevator)/float(length)
	max_wait_time_for_elevator = max(wait_times_for_elevator)
	min_wait_time_for_elevator = min(wait_times_for_elevator)

	total_times = [x.total_time() for x in fulfilled_requests]
	avg_total_time = sum(total_times)/float(length)
	max_total_time = max(total_times)
	min_total_time = min(total_times)

	elevator_times = [x.time_in_elevator() for x in fulfilled_requests]
	avg_elevator_time = sum(elevator_times)/float(length)
	max_elevator_time = max(elevator_times)
	min_elevator_time = min(elevator_times)

	stats = {}

	stats['avg_elevator_time'] = avg_elevator_time
	stats['max_elevator_time'] = max_elevator_time
	stats['min_elevator_time'] = min_elevator_time

	stats['avg_total_time'] = avg_total_time
	stats['max_total_time'] = max_total_time
	stats['min_total_time'] = min_total_time

	stats['avg_wait_time_for_elevator'] = avg_wait_time_for_elevator
	stats['max_wait_time_for_elevator'] = max_wait_time_for_elevator
	stats['min_wait_time_for_elevator'] = min_wait_time_for_elevator

	print 'here are some stats:'
	print ''

	print '    average wait time '+str(avg_wait_time_for_elevator)
	print '    max wait time '+str(max_wait_time_for_elevator)
	print '    min wait time '+str(min_wait_time_for_elevator) 
	print ''

	print '    average total time '+str(avg_total_time)
	print '    max total time '+str(max_total_time)
	print '    min total time '+str(min_total_time)
	print ''

	print '    average elevator time '+str(avg_elevator_time)
	print '    max elevator time '+str(max_elevator_time)
	print '    min elevator time '+str(min_elevator_time)
	print ''

	return stats

if __name__ == "__main__":
	results = get_solution_stats([1,1], challenges['baby_elevator'])
	print results


	




