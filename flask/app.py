from flask import Flask
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
from checker import *
from naive import *

challenges = {}
challenges['baby_elevator'] = {'problem': 'challenges/baby_elevator.txt',
								'inputs': 'inputs/baby_elevator.txt',
								'name': 'Baby Elevator'}
challenges['like_a_gauss'] =  {'problem': 'challenges/like_a_gauss.txt',
								'inputs': 'inputs/like_a_gauss.txt',
								'name': 'Like a Gawse'}
challenges['long_and_hard'] =  {'problem': 'challenges/long_and_hard.txt',
								'inputs': 'inputs/long_and_hard.txt',
								'name': 'Long and Hard'}	
challenges['antsy'] =  {'problem': 'challenges/antsy.txt',
								'inputs': 'inputs/antsy.txt',
								'name': 'Ansty'}
challenges['greenie'] =  {'problem': 'challenges/greenie.txt',
								'inputs': 'inputs/greenie.txt',
								'name': 'Greenie'}															
challenges['hippies'] =  {'problem': 'challenges/hippies.txt',
								'inputs': 'inputs/hippies.txt',
								'name': 'Hippies'}
challenges['real_life'] =  {'problem': 'challenges/real_life.txt',
								'inputs': 'inputs/real_life.txt',
								'name': 'Real Life'}
challenges['hwat'] =  {'problem': 'challenges/hwat.txt',
								'inputs': 'inputs/hwat.txt',
								'name': 'HWAT?'}
challenge_keys =['baby_elevator', 'like_a_gauss', 'long_and_hard',
				'antsy', 'greenie', 'hippies', 'real_life' , 'hwat']


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
	return render_template('home.html')


@app.route('/visualize', methods=['GET'])
def visualize():
	challenge = request.args.get('challenge')
	challenge = challenges[challenge]
	challenge_file = challenge['inputs']
	challenge_description = read_challenge_description(challenge['problem'])
	challenge_name = challenge['name']
	challenge_requests = load_requests(challenge_file)
	my_requests = [{'name':r.name, 
				 'floor1':r.floor1,
				 'floor2':r.floor2,
				 'time':r.time,
				 'direction':r.dir()} for r in challenge_requests]
	solution = get_naive_solution(challenge_requests)
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