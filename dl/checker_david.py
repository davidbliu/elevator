
inputs = []
outputs = []
# get input lines
with open('sample_input.txt', 'r') as ifile:
	for line in ifile:
		splits = line.rstrip().split(' ')
		person = {}
		person['name'] = splits[0]
		person['floor_a'] = int(splits[3])
		person['floor_b'] = int(splits[9])
		person['time'] = int(splits[-1])
		inputs.append(person)

output_lines = []
with open('sample_output.txt', 'r') as ofile:
	for line in ofile:
		output_lines.append(line)
	for i in range(0, len(output_lines)/2):
		line1 = output_lines[2*i].split(' ')
		line2 = output_lines[2*i+1].split(' ')
		state = {}
		state['start_time'] = int(line1[2])
		state['time'] = int(line2[-1])
		state['elevator'] = int(line1[5])
		state['floor'] = int(line1[-1])
		state['direction'] = line2[5].rstrip()
		outputs.append(state)


requests = inputs
elevator_states = outputs
elevator_requests = []
boards = 0
exits = 0
total_time = 0
# if people are on the right floor, let them in the elevator
def board_elevator(requests, floor, time,hang_time, direction, elevator_requests):
	global boards
	new_requests = []
	new_elevator_requests = elevator_requests
	for request in requests:
		request_direction = 'down'
		if request['floor_b'] > request['floor_a']:
			request_direction = 'up'
		if request['floor_a'] == floor and direction == request_direction and request['time']<= time+hang_time:
			request['board'] = time+hang_time
			new_elevator_requests.append(request)
			print request['name']+' boarded elevator at floor '+str(floor)+' at time '+str(time+hang_time)
			boards += 1
		else:
			new_requests.append(request)
	return new_requests, new_elevator_requests


# for all the requests that are on the right floor, get out of elevatorf
def empty_elevator(elevator_requests, floor, time):
	global exits
	global total_time
	new_elevator_requests = []
	for request in elevator_requests:
		if request['floor_b'] == floor:
			time_elapsed = time-request['time']
			total_time+=time_elapsed
			exits += 1
			print request['name'] + ' got off elevator at floor '+str(floor)+ ' at time '+str(time)
		else:
			new_elevator_requests.append(request)
	return new_elevator_requests

for i in range(0, len(elevator_states)):
	state = elevator_states[i]
	hang_time = 0
	if i < len(elevator_states)-1:
		hang_time = elevator_states[i+1]['start_time'] - state['time']
	requests, elevator_requests = board_elevator(requests, state['floor'], state['time'],hang_time, state['direction'], elevator_requests)
	elevator_requests = empty_elevator(elevator_requests, state['floor'], state['time'])

	contains = ''
	for request in elevator_requests:
		contains += request['name'] + ', '
	print 'elevator now contains '+contains
print 'boards: '+str(boards)
print 'exits: '+str(exits)
print 'average wait time '+str(float(total_time)/float(boards))+ ' seconds' 

