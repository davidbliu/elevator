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
	return render_template('home.html', committee_names = committee_names)

@app.route("/help")
def help():
	return render_template('help.html')

@app.route('/visualize', methods=['GET'])
def visualize():
	challenge = request.args.get('challenge')
	challenge = challenges[challenge]
	challenge_file = challenge['inputs']
	challenge_description = read_challenge_description(challenge['problem'])
	challenge_description = challenge_description.replace('\n','<br>\n')
	challenge_name = challenge['name']
	challenge_requests = load_requests(challenge_file)
	my_requests = [{'name':r.name, 
				 'floor1':r.floor1,
				 'floor2':r.floor2,
				 'time':r.time,
				 'direction':r.dir()} for r in challenge_requests]
	solution = get_naive_solution(challenge_requests)
	print challenge_description
	return render_template('animation.html', requests = my_requests,
											 solution = solution,
											 description = challenge_description,
											 challenge_name = challenge_name,
											 challenges = challenges,
											 challenge_keys = challenge_keys)

@app.route('/challenge', methods=['GET'])
def challenge():
	return 'visiting challenge page'

@app.route('/score_challenge', methods=['POST'])
def score_challenge():
	return 'your result has been scored'


if __name__ == "__main__":
	app.run(debug=True)