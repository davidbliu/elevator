from flask import Flask
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
# from checker import *
from naive import *
from seeds import *
# from name_checker import *
import name_checker as checker
import random

def read_challenge_description(filename):
	try:
		description = ''
		with open(filename, 'r') as f:
			for line in f:
				description += line
		return description
	except:
		return 'no description'
		
@app.route("/")
def home():
	scores = Score.Query.all()
	names = [x.name for x in scores]
	names = set(names)
	names = list(names)
	challenge_map = {}
	name_map = {}
	for score in scores:
		ch = score.challenge
		name = score.name
		if name not in name_map.keys():
			name_map[name] = {}
		name_map[name][score.challenge] = score.score
		if ch not in challenge_map.keys():
			challenge_map[ch] = []
		challenge_map[ch].append(score.score)
	for key in challenge_map.keys():
		challenge_map[key] = sorted(challenge_map[key])

	leaders = []

	for name in names:
		score = 0
		all_scores = [x for x in scores if x.name == name]
		for challenge in challenge_map.keys():
			# score for challenge is rank in list
			if challenge in name_map[name].keys():
				my_score_this_challenge = name_map[name][challenge]
				score += challenge_map[challenge].index(my_score_this_challenge)/float(len(names)) * 50
			else:
				score += 50 #len(challenge_map[challenge])
		leaders.append({'name':name, 'score':score, 'committee': 'no','scores':all_scores})
	leaders = sorted(leaders, key= lambda x: x['score'])
	return render_template('home.html', committee_names = committee_names,
										challenge_names = challenge_keys, challenges = challenges,
										scores = scores, leaders=leaders, leaderlen = len(leaders))

@app.route("/help")
def help():
	return render_template('help.html', challenges = challenges, challenge_names = challenge_keys)

@app.route('/visualize', methods=['GET'])
def visualize():
	challenge = request.args.get('challenge')
	challenge = challenges[challenge]
	challenge_file = challenge.input_file
	challenge_description = read_challenge_description(challenge.description_file)
	challenge_description = challenge_description.replace('\n','<br>\n')
	challenge_name = challenge.name
	challenge_requests = challenge.requests()
	my_requests = [{'name':r.name, 
				 'floor1':r.floor1,
				 'floor2':r.floor2,
				 'time':r.time,
				 'direction':r.dir()} for r in challenge_requests]
	solution = get_naive_solution(challenge_requests)
	return render_template('challenge.html', requests = my_requests,
											challenge = challenge,
											 solution = solution,
											 description = challenge_description,
											 challenge_name = challenge_name,
											 challenges = challenges,
											 challenge_keys = challenge_keys)
@app.route('/submit_page', methods=['GET'])
def submit_page():
	challenge = request.args.get('challenge')
	challenge = challenges[challenge]
	naive_solution = get_naive_solution(challenge.requests())
	return render_template('submit_page.html', challenge = challenge,
												naive_solution  = naive_solution)
@app.route('/submit', methods=['POST'])
def submit():
	challenge = request.args.get('challenge')
	challenge = challenges[challenge]
	elevator_1_instructions = request.form['elevator1']
	elevator_2_instructions = request.form['elevator2']
	#
	# grade these instructions
	#
	solution = [elevator_1_instructions, elevator_2_instructions]
	# challenge_requests = challenge.requests()
	# check_moves(elevator_1_instructions, challenge_requests, Elevator())
	
	soln_stats = get_solution_stats(solution, challenge)
	solution_stats = soln_stats['stats']
	solution_requests = soln_stats['requests']
	return render_template('results.html', stats = solution_stats, requests = solution_requests)


"""no longer works, only for the mmsi shit"""
@app.route('/results', methods=['GET'])
def results():
	challenge = request.args.get('challenge')
	challenge = challenges[challenge]
	elevator_1_instructions = request.args.get('elevator1')
	elevator_2_instructions = request.args.get('elevator2')
	#
	# grade these instructions
	#
	solution = [elevator_1_instructions, elevator_2_instructions]
	# challenge_requests = challenge.requests()
	# check_moves(elevator_1_instructions, challenge_requests, Elevator())
	
	soln_stats = get_solution_stats(solution, challenge)
	solution_stats = soln_stats['stats']
	solution_requests = soln_stats['requests']

	# save this persons score
	name = request.args.get('name')
	password = request.args.get('password')
	past_scores = Score.Query.filter(name = name)
	if len(past_scores)!=0:
		score = past_scores[0]
		if score.pw != password:
			return 'Wrong password entered!'
	past_scores = Score.Query.filter(name=name, challenge=challenge.alias)
	if len(past_scores)!=0:
		score = past_scores[0]
		score.score = random.randint(0, 500)
	else:
		score = Score(name=name, 
					  committee='Historians', 
					  score = random.randint(0, 500),
					  challenge = challenge.alias,
					  pw = password)

	score.save()
	return render_template('results.html', challenge = challenge,
		stats = solution_stats, requests = solution_requests)

"""da real deal scoring for namelist"""
@app.route('/challenge_results', methods=['GET'])
def challenge_results():
	challenge = request.args.get('challenge')
	challenge = challenges[challenge]
	elevator_1_instructions = request.args.get('elevator1')
	elevator_2_instructions = request.args.get('elevator2')
	solution = [elevator_1_instructions, elevator_2_instructions]


	

	soln = checker.check_solution(challenge, solution)
	
	if soln == False:
		return "Solution Incomplete, please try again!"
	stats = soln['stats']
	requests = soln['requests']


	"""SAVE THE SCORE"""
	name = request.args.get('name')
	password = request.args.get('password')
	past_scores = Score.Query.filter(name = name)
	if len(past_scores)!=0:
		score = past_scores[0]
		if score.pw != password:
			return 'Wrong password entered!'
	past_scores = Score.Query.filter(name=name, challenge=challenge.alias)
	if len(past_scores)!=0:
		score = past_scores[0]
		score.score = stats['final_score']
	else:
		score = Score(name=name, 
					  committee='Historians', 
					  score = stats['final_score'],
					  challenge = challenge.alias,
					  pw = password)
	score.solution = solution


	score.save()

	return render_template('challenge_results.html', stats = stats, 
											challenge = challenge,
											requests=requests)




@app.route('/view_input', methods = ['GET'])
def view_input():
	challenge = request.args.get('challenge')
	challenge = challenges[challenge]
	lines = read_challenge_description(challenge.input_file)
	lines = lines.replace('\n','<br>\n')
	return lines

@app.route('/timeline', methods = ['GET'])
def timeline():
	challenge = 'long_and_hard'
	challenge = challenges[challenge]
	requests = challenge.requests()

	solution = get_naive_solution(requests)
	soln_stats = get_solution_stats(solution, challenge)
	requests = soln_stats['requests']

	return render_template('timeline.html', requests = requests)


@app.route('/challenge', methods=['GET'])
def challenge():
	return 'visiting challenge page'

"""
@app.route('/score_challenge', methods=['GET'])
def score_challenge():
	# challenge = request.args.get('challenge')
	challenge = 'baby_elevator'
	challenge = challenges[challenge]
	solution = get_naive_solution(challenge.requests())
	results = test_solution(solution, challenge)
	return 'your result has been scored'
"""


if __name__ == "__main__":
	host = '0.0.0.0'
	port = 5130

	app.run(host = host, port = port, debug=True)
