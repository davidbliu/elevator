from seeds import *
from random import shuffle
import random
import itertools
from name_checker import *
import sys
challenge = challenges['baby_elevator']
requests = challenge.requests()


def findsubsets(S,m):
    return set(itertools.combinations(S, m))


request_set = set(requests)
subsets = []
for i in range(0, len(requests)):
	s = findsubsets(request_set, i)
	for subset in s:
		subsets.append(subset)


def solve(e1_requests, e2_requests):
	e1 = solve_requests(e1_requests)
	e2 = solve_requests(e2_requests)

	# print e1 
	# print e2 

	# print 'checking this solution'
	e1_inst = ""
	e2_inst = ""
	for e in e1:
		e1_inst += e+','
	for e in e2:
		e2_inst += e+','

	e1_inst = e1_inst[:len(e1_inst)-1]
	e2_inst = e2_inst[:len(e2_inst)-1]
	score = check_solution(challenges['baby_elevator'],[e1_inst, e2_inst])
	score = score['stats']['final_score']
	return [score, e1_inst, e2_inst]
# gets best ordering for e1 requests and e2 requests and also the score
def solve_requests(requests):
	# print 'solving requests'
	# print [x.name for x in requests]


	maxlength = len(requests)*2
	time = 0
	floor = 0
	ordering = []
	onboard = []

	curr_request = min(requests, key = lambda x: x.time)
	curr_destination = curr_request.floor2
	floor = curr_request.floor1
	time = floor 
	time = max(curr_request.time, time)

	requests = [x for x in requests if x != curr_request]

	onboard.append(curr_request)
	ordering.append(curr_request.name)

	while(len(ordering)<maxlength):
		# see who you can pick up on the way
		ontheway = [x for x in requests if x.time <= time and x.floor1 == floor]
		for o in ontheway:
			onboard.append(o)
			ordering.append(o.name)
		# see who you can drop off
		drop = [x for x in onboard if x.floor2 == floor]
		for d in drop:
			ordering.append(d.name)
		onboard = [x for x in onboard if x not in drop]
		# update requests
		requests = [x for x in requests if x not in ontheway]

		# update time and position
		time += 1
		if len(onboard)!=0:
			if curr_destination == floor:
				curr_request = min(onboard, key = lambda x: x.time)
				curr_destination = x.floor2
			elif curr_destination<floor:
				curr_destination = min([x.floor2 for x in onboard])
			elif curr_destination>floor:
				curr_destination = max([x.floor2 for x in onboard])

			# move in direction of curr_destination
			if curr_destination>floor:
				floor+=1
			else:
				floor-=1
		elif len(requests) !=0:
			# pick up the next person
			curr_request = min(requests, key = lambda x: x.time)
			curr_destination = curr_request.floor2
			time = max(curr_request.time, time + abs(floor - curr_request.floor1))
			floor = curr_request.floor1
			onboard.append(curr_request)
			ordering.append(curr_request.name)
			requests = [x for x in requests if x not in onboard]
		else:
			break
		

	# print ordering
	# print 'that was ordering'
	return ordering
	# print curr_destination


bestscore = sys.maxint
best_e1 = ""
best_e2 = ""
for subset in subsets:
	e1_requests = list(subset)
	e2_requests = [x for x in request_set if x not in subset]
	if len(e1_requests)!=0 and len(e2_requests)!=0:
		score, e1_inst, e2_inst = solve(e1_requests, e2_requests)
		print score
		if score<bestscore:
			bestscore = score
			best_e1 = e1_inst
			best_e2 = e2_inst

print 'best score was '
print bestscore
print best_e1
print '\n'
print best_e2

