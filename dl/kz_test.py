from checker import Elevator, Request, check_moves

requests = []

with open('sample_input.txt', 'r') as ifile:
	for line in ifile:
		splits = line.rstrip().split(' ')
		req = Request(splits[0],
				int(splits[3]),
				int(splits[9]),
				int(splits[-1]))
		requests.append(req)

elevator = Elevator()
movelist = 'iiiiiiiiiiiiiimmmsimmi'
check_moves(movelist, requests, elevator)