from seeds import *
from random import shuffle
import random
import itertools
from name_checker import *
import sys
import copy
challenge = challenges['baby_elevator']
requests = challenge.requests()


def findsubsets(S,m):
    return set(itertools.combinations(S, m))



def solve(challenge, e1_requests, e2_requests):

	if challenge.alias == 'speedy':
		e1 = solve_requests(e1_requests)
		e2 = solve_requests(e2_requests, speed = 2)
	else:
		e1 = solve_requests(e1_requests)
		e2 = solve_requests(e2_requests)
	
	e1 = [x.name for x in e1]
	e2 = [x.name for x in e2]

	# print 'checking this solution'

	e1_inst = ""
	for e in e1:
		e1_inst += e+','
	e1_inst = e1_inst[:len(e1_inst)-1]
	e2_inst = ""
	for e in e2:
		e2_inst += e+','

	e1_inst = e1_inst[:len(e1_inst)]
	e2_inst = e2_inst[:len(e2_inst)]

	score = check_solution(challenge,[e1_inst, e2_inst])
	score = score['stats']['final_score']
	return [score, e1_inst, e2_inst]

def solve_requests(requests, speed = 1):

	# take the min. TODO loop through all possible starting values and run scan algorithm
	# curr_request = min(requests, key = lambda x: x.time)
	curr_request = min(requests, key = lambda x: x.time)
	maxlength = len(requests)*2
	time = 0
	floor = 0
	ordering = []
	onboard = []

	curr_destination = curr_request.floor2
	floor = curr_request.floor1
	time = floor*speed
	time = max(curr_request.time, time)

	onboard.append(curr_request)
	ordering.append(curr_request)
	requests = [x for x in requests if x not in onboard]

	
	

	while(len(ordering)<maxlength):
		# see who you can pick up on the way
		ontheway = [x for x in requests if x.time <= time and x.floor1 == floor]
		onboard += ontheway
		ordering += ontheway

		# see who you can drop off
		drop = [x for x in onboard if x.floor2 == floor]
		ordering += drop
		onboard = [x for x in onboard if x not in drop]
		# update requests
		requests = [x for x in requests if x not in ontheway]

		# update time and position
		time += speed
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
			ordering.append(curr_request)
			requests = [x for x in requests if x not in onboard]
		else:
			break
	return ordering


def test_scan(e1, e2):
	e1 = set(e1.split(','))
	e2 = set(e2.split(','))
	requests = challenges['baby_elevator'].requests()
	e1_req = [x for x in requests if x.name in e1]
	e2_req = [x for x in requests if x.name in e2]
	soln = solve(e1_req, e2_req)
	print soln 
# e1 = "KIM,IRWIN,KIM,ALYSON,IRWIN,ALYSON,ALYSHA,ALYSHA,DULCIE,DULCIE,ISAIAS,ISAIAS" 
# e2 = "MOIRA,MOIRA,ERNEST,ALI,ERNEST,ALI,ANNABELL,ANNABELL"
# test_scan(e1, e2)

# print 'analyzing 17.1 soln'
# e1 = 'ERNEST,ALI,ALI,ERNEST,ALYSHA,ALYSHA,DULCIE,ISAIAS,ISAIAS,DULCIE'
# e2 = 'KIM,IRWIN,KIM,ALYSON,IRWIN,MOIRA,ANNABELL,ALYSON,MOIRA,ANNABELL'
# test_scan(e1, e2)
	# print ordering
	# print 'that was ordering'

	#
	# return only the best ordering
	#

def brute_force_subsets(challenge, requests):
	request_set = set(requests)
	subsets = []
	for i in range(0, len(requests)):
		s = findsubsets(request_set, i)
		for subset in s:
			subsets.append(subset)

	bestscore = sys.maxint
	best_e1 = ""
	best_e2 = ""
	for subset in subsets:
		e1_requests = list(subset)
		e2_requests = [x for x in request_set if x not in subset]
		if len(e1_requests)!=0 and len(e2_requests)!=0:
			# score, e1_inst, e2_inst = solve(e1_requests, e2_requests)
			score, e1_inst, e2_inst = solve(challenge, e1_requests, e2_requests)
			
			if score<bestscore:
				print score
				bestscore = score
				best_e1 = e1_inst
				best_e2 = e2_inst
				print e1_inst
				print e2_inst

	print 'best score was '
	print bestscore
	print 'E1: '+best_e1
	print 'E2: '+best_e2
requests = challenges['mama'].requests()
brute_force_subsets(challenges['mama'], requests)
