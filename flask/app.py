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
	my_requests = [{'name':r.name, 
				 'floor1':r.floor1,
				 'floor2':r.floor2,
				 'time':r.time,
				 'direction':r.dir()} for r in requests]
	print requests
	return render_template('animation.html', requests = my_requests)



if __name__ == "__main__":
    app.run()