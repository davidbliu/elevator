
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
		state['time'] = int(line1[2])
		state['elevator'] = int(line1[5])
		state['end'] = int(line1[-1])
		state['direction'] = line2[5].rstrip()
		outputs.append(state)


requests = inputs
elevator_states = outputs

elevator_requests = []

# if people are on the right floor, let them in the elevator
def board_elevator(requests, floor, time, direction):


# for all the requests that are on the right floor, get out of elevatorf
def empty_elevator(elevator_requests, floor):

for state in elevator_states:
	print ''


