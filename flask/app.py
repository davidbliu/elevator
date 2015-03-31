from flask import Flask
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
from checker import *
from naive import *
from seeds import *


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
	return render_template('home.html', committee_names = committee_names,
										challenge_names = challenge_keys)

@app.route("/help")
def help():
	return render_template('help.html')

@app.route('/visualize', methods=['GET'])
def visualize():
	challenge = request.args.get('challenge')
	challenge = challenges[challenge]
	challenge_file = challenge.input_file
	challenge_description = read_challenge_description(challenge.description_file)
	challenge_description = challenge_description.replace('\n','<br>\n')
	challenge_name = challenge.name
	challenge_requests = load_requests(challenge_file)
	my_requests = [{'name':r.name, 
				 'floor1':r.floor1,
				 'floor2':r.floor2,
				 'time':r.time,
				 'direction':r.dir()} for r in challenge_requests]
	solution = get_naive_solution(challenge_requests)
	return render_template('animation.html', requests = my_requests,
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
	return render_template('submit_page.html', challenge = challenge)
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
	solution_stats = get_solution_stats(solution, challenge)
	return render_template('results.html', stats = solution_stats)

@app.route('/view_input', methods = ['GET'])
def view_input():
	challenge = request.args.get('challenge')
	challenge = challenges[challenge]
	lines = read_challenge_description(challenge.input_file)
	lines = lines.replace('\n','<br>\n')
	return lines

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
	host = 'localhost'
	port = 5130

	app.run(host = host, port = port, debug=True)