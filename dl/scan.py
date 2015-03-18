class Elevator:

	def __init__(self):
		self.requests = []
		self.floor = 0
		self.direction = 'UP'

class NaiveElevator:
	

class Request:
	
	def __init__(self, start_floor, end_floor, time, name):
		self.start_floor = start_floor
		self.end_floor = end_floor
		self.time = time
		self.name = name

class ElevatorSystem:

	def __init__(self):
		self.elevators = [Elevator()]


	def naive_algorithm(self, request_stream):
		""" YOUR CODE HERE """



		current_requests = []
		finished_requests = []
		elevator = self.elevators[0]
		print 'Printing results of naive algorithm'
		
		time = 0
		while len(finished_requests) < len(request_stream):
			# see if any new requests have come in at this time
			for request in request_stream:
				if request.time == time:
					current_requests.append(request)
			# handle the current requests
			time += 1


	def scan_algorithm(self):
		""" YOUR CODE HERE """

def import_data(request_file):
	requests = []
	with open(request_file, 'r') as ifile:
		for line in ifile:
			splits = line.rstrip().split(' ')
			name = splits[0]
			start_floor = int(splits[3])
			end_floor = int(splits[9])
			time = int(splits[-1])
			request = Request(start_floor, end_floor, time, name)
			requests.append(request)
	return requests

requests = import_data('sample_input.txt')
elevator_system = ElevatorSystem()
elevator_system.naive_algorithm(requests)
