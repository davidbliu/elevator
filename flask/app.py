from flask import Flask
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
from checker import *
from naive import *

@app.route("/")
def home():
	return render_template('home.html')


@app.route('/visualize', methods=['GET'])
def visualize():
	challenge_file = request.args.get('challenge')
	print challenge_file
	print 'that was my challenge file'
	challenge_requests = load_requests(challenge_file)
	my_requests = [{'name':r.name, 
				 'floor1':r.floor1,
				 'floor2':r.floor2,
				 'time':r.time,
				 'direction':r.dir()} for r in challenge_requests]
	solution = get_naive_solution(challenge_requests)
	return render_template('animation.html', requests = my_requests, solution = solution)

@app.route('/challenge', methods=['GET'])
def challenge():
	return 'visiting challenge page'

@app.route('/score_challenge', methods=['POST'])
def score_challenge():
	return 'your result has been scored'


if __name__ == "__main__":
	app.run(debug=True)