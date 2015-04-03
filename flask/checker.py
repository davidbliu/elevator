from seeds import *
import random
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
			r.fulfilled = True
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

def moves_are_valid(moves):
	floor = 0
	direction = 1
	for move in moves:
		if move == 'm':
			floor += direction
		if move == 's':
			direction *= -1
		if floor < 0 or floor > Elevator.maxfloor:
			return False
	return True

def make_move(move, time,  elevator, requests):
	if move == 'm':
		elevator.move()
	if move == 'i':
		# check if people need to get in or out of elevator
		data = elevator.idle(time, requests)
		requests = data['new_pool']
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
	for request in requests:
		print request.time_entered
		print request.time_exited
		print '......'
		if request.time_exited == -1:
			request.time_exited = time
		if request.time_entered == -1:
			request.time_entered = time
	for elevator in elevators:
		for request in elevator.requests:
			print request.time_entered
			print request.time_exited
			print '......'
			if request.time_exited == -1:
				request.time_exited = time
			if request.time_entered == -1:
				request.time_entered = time
#
# returns fulfilled requests
#
def test_solution(solution, challenge):
	challenge_requests = challenge.requests()
	e1_instructions = solution[0]
	e2_instructions = solution[1]
	e1 = Elevator('1')
	e2 = Elevator('2')

	# e1_instructions = 'iimmmmmmmmmmmmmmmmmmmmmmmmsimmmmmmmmmmmmmmismmmimmmmmmmmmismmmmmmmmmmmmmmmmmmsimmmmmmmismimmmmmmismmmmmmmmmmmmmsimmmmmmmmmmmmmmmmi'
	# e2_instructions = 'iiiiiiiiiiiiiiiiiiiiimmmmimmmmmmmmmmmmmmmmismmmmmmmmmmmmmmmmmmmsimmmmmmmmmmmimmmmmmmmsimmmmmimmmmmmmmmmmsimmmmmmmmmmmmmismmmmmmmmmmsimmmmmmmmmi'
	if(not moves_are_valid(e1_instructions) or not moves_are_valid(e2_instructions)):
		print 'moves are not valid' 
	else:
	
		moves = [e1_instructions, e2_instructions]
		elevators = [e1, e2]
		check_solution(moves, challenge_requests, elevators)

	# return e1.fulfilled_requests+e2.fulfilled_requests
	return challenge_requests

def get_solution_stats(solution, challenge):

	if(not moves_are_valid(solution[0]) and moves_are_valid(solution[1])):
		stats = {'error_with_solution_bounds':'your solution went out of bounds! :('}
		return {'requests':challenge.requests(), 'stats':stats}
	challenge_requests = challenge.requests()
	challenge_requests = test_solution(solution, challenge)
	fulfilled_requests = [x for x in challenge_requests if x.fulfilled]
	unfulfilled = [x for x in challenge_requests if x not in fulfilled_requests]


	length = len(fulfilled_requests)
	if length == 0:
		stats =  {'error_with_requests':'no requests were fulfilled'}
		return {'requests':challenge_requests, 'stats':stats}
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
	stats['num_challenge_requests'] = len(challenge_requests)
	stats['num_requests_fulfilled'] = length
	stats['percent_requests_fulfilled'] = length/float(len(challenge_requests))
	stats['completed'] = (length==len(challenge_requests))

	stats['avg_elevator_time'] = avg_elevator_time
	stats['max_elevator_time'] = max_elevator_time
	stats['min_elevator_time'] = min_elevator_time

	stats['avg_total_time'] = avg_total_time
	stats['max_total_time'] = max_total_time
	stats['min_total_time'] = min_total_time

	stats['avg_wait_time_for_elevator'] = avg_wait_time_for_elevator
	stats['max_wait_time_for_elevator'] = max_wait_time_for_elevator
	stats['min_wait_time_for_elevator'] = min_wait_time_for_elevator
	

	return {'requests':challenge_requests, 'stats':stats}


def get_solution_score(solution, challenge):
	return random.randint(0, 500)

if __name__ == "__main__":
	results = get_solution_stats([1,1], challenges['baby_elevator'])
	print results


	




