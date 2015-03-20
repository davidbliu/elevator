from flask import Flask
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
from checker import *


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/visualize', methods=['GET'])
def visualize():
	print 'here are the requests'
	print requests
	return render_template('animation.html', requests = requests)



if __name__ == "__main__":
    app.run()