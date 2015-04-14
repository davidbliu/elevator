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



def solve(e1_requests, e2_requests):
	e1 = solve_requests(e1_requests)
	e2 = solve_requests(e2_requests)

	print 'the requests split'
	print [x.name for x in e1_requests]
	print [x.name for x in e2_requests]
	print 'the orderings'
	print e1 
	print e2 

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
	print e1_inst
	print e2_inst
	score = check_solution(challenges['baby_elevator'],[e1_inst, e2_inst])
	score = score['stats']['final_score']
	return [score, e1_inst, e2_inst]
# gets best ordering for e1 requests and e2 requests and also the score
def solve_requests(requests):


	req_copy = copy.deepcopy(requests)
	orderings = []
	# take the min. TODO loop through all possible starting values and run scan algorithm
	# curr_request = min(requests, key = lambda x: x.time)
	for req in req_copy:
		curr_request = req
		maxlength = len(req_copy)*2
		time = 0
		floor = 0
		ordering = []
		onboard = []

		curr_destination = curr_request.floor2
		floor = curr_request.floor1
		time = floor 
		time = max(curr_request.time, time)

		requests = [x for x in req_copy if x != curr_request]

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
		orderings.append(ordering)

	# print ordering
	# print 'that was ordering'

	#
	# return only the best ordering
	#
	best_ordering = []
	best_cost = sys.maxint
	for ordering in orderings:
		cost = calculate_ordering_cost(ordering, req_copy)
		if cost < best_cost:
			best_ordering = ordering 
			best_cost = cost
	return best_ordering
	# print curr_destination

def calculate_ordering_cost(ordering, requests):
	path = []
	req_map = {}
	for req in requests:
		req_map[req.name] = req

	for name in ordering:
		path.append(copy.deepcopy(req_map[name]))
	return calculate_cost(path, requests)


"""HERE is my implementation of Uniform Cost Search"""

import copy
import Queue as queue
import heapq

def cost(ordering, cost_function):
	return 0

def uniform_cost_solve(e1, e2):
	print 'solving with these requests:'
	print [x.name for x in e1]
	print [x.name for x in e2]

	e2_soln = uniform_cost_search(e2)
	e1_soln = uniform_cost_search(e1)
	print 'printing solutions'
	print e1_soln
	print e2_soln
	return 0, 0, 0


class SearchNode:

	def __init__(self, path, remaining, cost):
		self.path = path
		self.remaining = remaining
		self.cost = cost

def calculate_cost(path, requests):

	time = 0
	floor = 0
	cost = 0
	entered = set()
	exited = set()
	for req in path:
		exiting = False
		end_time = 0
		if req.name in entered:
			destination = req.floor2
			exiting = True
		else:
			entered.add(req.name)
			destination = req.floor1
			end_time = req.time
		while floor != destination or end_time>time:
			if destination>floor:
				floor += 1
			elif destination<floor:
				floor -= 1
			# increment cost by number of requests online
			requests_online = [x for x in requests if x.time<=time and x.name not in exited]
			time += 1
			# print str(time)+' end time '+str(end_time)+' floor '+str(floor)+' online '+str(len(requests_online))+' cost '+str(cost)

			cost += len(requests_online)
		if exiting:
			exited.add(req.name)
	return cost

def get_name_map(requests):
	name_map = {}
	for r in requests:
		name_map[r.name] = r
	return name_map
#
# how long would if take to finish the reset of the requests
#
def heuristic(path, requests):
	name_map = get_name_map(requests)

	cost = 0

	req_copy = copy.deepcopy(requests)
	requests = requests+req_copy
	# run a scan algorithm for the remaining requests
	onboard = []
	remaining_requests = []
	path_map = {}
	for req in path:
		if req.name not in path_map.keys():
			path_map[req.name] = 0 
		path_map[req.name] += 1
	for req in req_copy:
		if req.name not in path_map.keys():
			remaining_requests.append(req)
		else:
			if path_map[req.name] == 1:
				onboard.append(req)


	# print path_map
	# print 'onboard is '+str(onboard)
	# print 'remaining requests are '+str([x.name for x in remaining_requests])

	time = 0
	floor = 0
	cost = 0
	entered = set()
	exited = set()
	for req in path:
		exiting = False
		end_time = 0
		if req.name in entered:
			destination = req.floor2
			exiting = True
		else:
			entered.add(req.name)
			destination = req.floor1
			end_time = req.time
		while floor != destination or end_time>time:
			if destination>floor:
				floor += 1
			elif destination<floor:
				floor -= 1
			# increment cost by number of requests online
			requests_online = [x for x in requests if x.time<=time and x.name not in exited]
			time += 1
			# print str(time)+' end time '+str(end_time)+' floor '+str(floor)+' online '+str(len(requests_online))+' cost '+str(cost)

			cost += len(requests_online)
		if exiting:
			exited.add(req.name)

	ordering = []

	maxlength = len(remaining_requests)*2+len(onboard)
	# print maxlength
	# print 'that was maxlength'
	curr_request = [x for x in remaining_requests if x not in onboard][0]
	curr_destination = curr_request.floor2
	onboard.append(curr_request)
	remaining_requests = [x for x in remaining_requests if x != curr_request]
	ordering.append(curr_request)

	
	time += abs(floor-curr_request.floor1)
	floor = curr_request.floor1
	time = max(time, curr_request.time)

	# print len(remaining_requests)
	# print 'that was len'
	while len(ordering)<maxlength:
		ontheway = [x for x in remaining_requests if x.time <= time and x.floor1 == floor]
		onboard += [o for o in ontheway]
		ordering += [o for o in ontheway]
		drop = [x for x in onboard if x.floor2 == floor]
		ordering += [d for d in drop]
		onboard = [x for x in onboard if x not in drop]
		remaining_requests = [x for x in remaining_requests if x not in ontheway]
		time += 1
		if len(onboard) != 0:
			if curr_destination == floor:
				curr_request = min(onboard, lambda x: x.time)
				curr_destination = x.floor2
			elif curr_destination < floor:
				curr_destination = min([x.floor2 for x in onboard])
			elif curr_destination > floor:
				curr_destination = max([x.floor2 for x in onboard])
			if curr_destination > floor:
				floor += 1
			else:
				floor -= 1
		elif len(remaining_requests) != 0:
			curr_request = min(requests, key = lambda x: x.time)
			curr_destination = curr_request.floor2
			time = max(curr_request.time, time+abs(floor-curr_request.floor1))
			floor = curr_request.floor1
			onboard.append(curr_request)
			ordering.append(curr_request)
			remaining_requests = [x for x in remaining_requests if x not in onboard]
		else:
			break
	# print ordering

	return calculate_cost(ordering, req_copy)


import random

def uniform_cost_search(requests):
	print 'running uniform cost search on '+str([r.name for r in requests])
	req_copy = copy.deepcopy(requests)
	request_names = [req.name for req in requests]
	request_names *= 2

	requests = requests+req_copy
	print len(requests)

	search_queue = []
	# get put all next requests in queue
	for req in requests:
		path = [req]
		remaining = [x for x in requests if x not in path]
		cost = 0
		node = SearchNode(path, remaining, cost)
		# search_queue.put(node, cost)
		heapq.heappush(search_queue, (cost, node))

	found_soln = False 
	while not len(search_queue)==0 and found_soln != True:
		# pop off lowest cost from queue
		curr_node = heapq.heappop(search_queue)[1]
		print str(curr_node.cost)+' '+str(len(curr_node.path))+ ' ' + str(len(requests))

		# print str([x.name for x in curr_node.path])+' cost was '+str(curr_node.cost)
		remaining = curr_node.remaining
		if len(remaining)==0:
			found_soln = True
		else:
			# put the next level you want to explore on the queue
			# for req in remaining[0:1]:
			if (len(remaining)!=0):
				req = remaining[0]
				path = curr_node.path + [req]
				remain = [x for x in requests if x not in path]
				cost = heuristic(path, req_copy)
				node = SearchNode(path, remain, cost)
				# search_queue.put(node, -cost)
				heapq.heappush(search_queue, (cost, node))
	# print 'found solution was '+str([x.name for x in curr_node.path])
	return [x.name for x in curr_node.path]


# requests = challenges['baby_elevator'].requests()

# path = challenges['baby_elevator'].requests()[0:3]
# print 'path was '+str([x.name for x in path])
# print heuristic(path, challenges['baby_elevator'].requests())
# print calculate_cost(path, requests)

e1 = "KIM,IRWIN,KIM,ALYSON,IRWIN,ALYSON,ALYSHA,ALYSHA,DULCIE,DULCIE,ISAIAS,ISAIAS,","MOIRA,MOIRA,ERNEST,ALI,ERNEST,ALI,ANNABELL,ANNABELL"

e2 = "MOIRA,MOIRA,ALYSON,ANNABELL,ALYSON,ALYSHA,ALYSHA,ANNABELL,","KIM,ERNEST,ALI,DULCIE,ISAIAS,ALI,ERNEST,IRWIN,ISAIAS,DULCIE,KIM,IRWIN"
def test_scan(e1, e2):
	e1 = set(e1)
	e2 = set(e2)
	requests = challenges['baby_elevator'].requests()
	e1_req = [x for x in requests if x.name in e1]
	e2_req = [x for x in requests if x.name in e2]


request_set = set(requests)
subsets = []
for i in range(0, len(requests)):
	s = findsubsets(request_set, i)
	for subset in s:
		subsets.append(subset)

bestscore = sys.maxint
best_e1 = ""
best_e2 = ""
for subset in subsets[53:54]:
	e1_requests = list(subset)
	e2_requests = [x for x in request_set if x not in subset]
	if len(e1_requests)!=0 and len(e2_requests)!=0:
		# score, e1_inst, e2_inst = solve(e1_requests, e2_requests)
		score, e1_inst, e2_inst = solve(e1_requests, e2_requests)
		print score
		if score<bestscore:
			bestscore = score
			best_e1 = e1_inst
			best_e2 = e2_inst

print 'best score was '
print bestscore
print 'E1: '+best_e1
print 'E2: '+best_e2



