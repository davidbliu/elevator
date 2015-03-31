class Request:
	def __init__(self, name, floor1, floor2, time):
		self.name = name
		self.floor1= floor1
		self.floor2 = floor2
		self.time = time
		self.time_entered = -1
		self.time_exited = -1
	def dir(self):
		if self.floor2 > self.floor1:
			return 1
		else:
			return -1
	def time_in_elevator(self):
		return self.time_exited - self.time_entered

	def total_time(self):
		return self.time_exited - self.time

	# check if request was fulfilled
	def fulfilled(self):
		if self.time_entered != -1 and self.time_exited != -1:
			return True
		return False



class Committee:
	def __init__(self, name, cid, password = 'asdf'):
		self.name = name
		self.id = cid
	def total_score(self):
		return 10

class User:
	def __init__(self, name, committee):
		self.name = name
		self.committee = committee
		self.scores = {}

class Score:
	def __init__(self, problem, data):
		print 'creating score'

class Challenge:
	def __init__(self, name, input_file, description_file, alias):
		self.name = name
		self.alias = alias
		self.input_file = 'challenges/inputs/'+input_file
		self.description_file = 'challenges/descriptions/'+description_file
	def requests(self):
		rs = []
		with open(self.input_file, 'r') as ifile:
			for line in ifile:
				splits = line.rstrip().split(' ')
				req = Request(splits[0],
						int(splits[3]),
						int(splits[9]),
						int(splits[-1]))
				rs.append(req)
		return rs

challenges = {}
challenges['baby_elevator'] = Challenge('Baby Elevator', 'baby_elevator.txt', 'baby_elevator.txt', 'baby_elevator')
challenges['like_a_gauss'] = Challenge('Like A Gauss', 'like_a_gauss.txt', 'like_a_gauss.txt', 'like_a_gauss')
challenges['long_and_hard'] = Challenge('Long and Hard', 'long_and_hard.txt', 'long_and_hard.txt', 'long_and_hard')
challenges['antsy'] = Challenge('Antsy', 'antsy.txt', 'antsy.txt', 'antsy')
challenges['greenie'] = Challenge('Greenie', 'greenie.txt', 'greenie.txt', 'greenie')
challenges['hippies'] = Challenge('Hippies', 'hippies.txt', 'hippies.txt', 'hippies')
challenges['amurica'] = Challenge('Amurica', 'amurica.txt', 'amurica.txt', 'amurica')
challenges['real_life'] = Challenge('Real Life', 'real_life.txt', 'real_life.txt', 'real_life')


challenge_keys =['baby_elevator', 'like_a_gauss', 'long_and_hard',
				'amurica', 'antsy', 'greenie', 'hippies', 'real_life']


committee_names = ['Community Service', 'Consulting', 'Finance', 'Marketing', 'Historian', 'Publications', 
	'Professional Development', 'Social', 'Internal Networking', 'Web Development']