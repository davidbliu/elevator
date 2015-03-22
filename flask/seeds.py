class Committee:
	def __init__(self, name):
		self.name = name
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