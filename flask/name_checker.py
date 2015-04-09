from seeds import *
from random import shuffle
import random
import itertools
class SolutionRequest:
	pass

def check_solution(challenge, solution):

	challenge_requests = challenge.requests()
	req_dict = {}
	for req in challenge_requests:
		req_dict[req.name] = req

	e1_solution = [x for x in solution[0].split(',') if x != '']
	e2_solution = [x for x in solution[1].split(',') if x != '']
	if not is_valid_solution(e1_solution, challenge_requests) and is_valid_solution(e2_solution, challenge_requests):
		# print 'not a valid solution'
		return False
	e1_finished_requests, e1_people_list = check_elevator(e1_solution, req_dict)
	e2_finished_requests, e2_people_list = check_elevator(e2_solution, req_dict)
	total_finished_requests = []
	for req in e1_finished_requests:
		req.elevator = 'elevator1'
		total_finished_requests.append(req)
	for req in e2_finished_requests:
		req.elevator = 'elevator2'
		total_finished_requests.append(req)
	if not len(total_finished_requests) == len(challenge_requests):
		# print 'not all the requests were finished'
		return False
	else:
		# print 'all the requests were finished, generating statistics'
		stats = get_stats(total_finished_requests)
		# print 'you are being judged on average total time'
		# print sum(stats['total_times'])/float(len(stats['total_times']))
		stats['final_score'] = stats['avg_total_time']

		#
		# set final score based on problem
		#
		if challenge.alias == "hurry":
			stats['final_score'] = max([x.time_exited for x in total_finished_requests])
		if challenge.alias == "sweaty":
			stats['final_score'] = sum(stats['elevator_times'])/float(len(stats['elevator_times']))
		if challenge.alias == 'amurica':
			penalty = 0
			print 'handling america'
			for people_list in [e1_people_list, e2_people_list]:
				for num_people in people_list:
					if num_people[0]>3:
						# penalize score 
						penalty += 2*num_people[1]
			stats['final_score'] = stats['final_score'] + penalty
		return {'stats':stats, 'requests':total_finished_requests}



def is_valid_solution(solution, requests):
	request_names = set([x.name for x in requests])
	for x in solution:
		if x not in request_names:
			return False
	return True
def get_stats(finished_requests):
	stats = {}
	wait_times = [(x.time_entered-x.time_requested) for x in finished_requests]
	elevator_times = [(x.time_exited-x.time_entered) for x in finished_requests]
	total_times = [(x.time_exited-x.time_requested) for x in finished_requests]
	stats['wait_times'] = wait_times
	stats['total_times'] = total_times
	stats['elevator_times'] = elevator_times
	stats['avg_total_time'] = sum(total_times)/float(len(total_times))
	stats['avg_wait_time'] = sum(wait_times)/float(len(wait_times))
	stats['avg_elevator_time'] = sum(elevator_times)/float(len(elevator_times))
	stats['max_total_time'] = max(total_times)
	stats['max_wait_time'] = max(wait_times)
	stats['max_elevator_time'] = max(elevator_times)
 	return stats

def check_elevator(solution_names, req_dict):
	entered = {}	
	floor = 0
	time = 0
	num_people = 0
	num_people_list = []
	times_list = []
	def move_to_floor(newfloor, req_time, floor, time):
		elapsed_time = abs(newfloor-floor)
		floor = newfloor 
		time+=elapsed_time
		time = max(time, req_time)
		return floor, time

	finished_requests = []
	for name in solution_names:
		req = req_dict[name]
		if name in entered.keys():
			# first drop this person off
			sol_req = entered[name]
			floor, time = move_to_floor(req.floor2, req.time, floor, time)
			# then update their time exited and put their request in finished
			sol_req.time_exited = time
			finished_requests.append(sol_req)
			num_people-=1
			# print name+ ' is exiting the elevator at time '+str(time)
		else:
			# first pick this person up
			floor, time = move_to_floor(req.floor1, req.time, floor, time)
			# pick this person up and create a sol req
			sol_req = SolutionRequest()
			sol_req.time_entered = time
			sol_req.name = name
			sol_req.time_requested = req.time
			entered[name] = sol_req
			num_people+=1
		num_people_list.append(num_people)
		times_list.append(time)
			# print name+ ' is entering the elevator at time '+str(time)
	ppl_list = []
	for i in range(0, len(num_people_list)):
		if i<len(num_people_list)-1:
			ppl_list.append([num_people_list[i], times_list[i+1]])
		else:
			ppl_list.append([num_people_list[i], time])
	return finished_requests, ppl_list

if __name__ == "__main__":
	names = [x.name for x in challenges['baby_elevator'].requests()]
	names = names

	namestring = ''
	for name in names:
		namestring += name + ','
	soln = check_solution(challenges['baby_elevator'], [namestring[:-1], ''])





