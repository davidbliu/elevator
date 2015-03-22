class Committee:
	def __init__(self, name, password):
		self.name = name
		self.password = password
		print 'creating '+str(name)

	def total_score(self):
		return 10

class Score:
	def __init__(self, problem, data):
		print 'creating score'


challenges = {}
challenges['baby_elevator'] = {'problem': 'challenges/descriptions/baby_elevator.txt',
								'inputs': 'challenges/inputs/baby_elevator.txt',
								'name': 'Baby Elevator'}
challenges['like_a_gauss'] =  {'problem': 'challenges/descriptions/like_a_gauss.txt',
								'inputs': 'challenges/inputs/like_a_gauss.txt',
								'name': 'Like a Gawse'}
challenges['long_and_hard'] =  {'problem': 'challenges/descriptions/long_and_hard.txt',
								'inputs': 'challenges/inputs/long_and_hard.txt',
								'name': 'Long and Hard'}	
challenges['antsy'] =  {'problem': 'challenges/descriptions/antsy.txt',
								'inputs': 'challenges/inputs/antsy.txt',
								'name': 'Ansty'}
challenges['greenie'] =  {'problem': 'challenges/descriptions/greenie.txt',
								'inputs': 'challenges/inputs/greenie.txt',
								'name': 'Greenie'}															
challenges['hippies'] =  {'problem': 'challenges/descriptions/hippies.txt',
								'inputs': 'challenges/inputs/hippies.txt',
								'name': 'Hippies'}
challenges['real_life'] =  {'problem': 'challenges/descriptions/real_life.txt',
								'inputs': 'challenges/inputs/real_life.txt',
								'name': 'Real Life'}
challenges['amurica'] =  {'problem': 'challenges/descriptions/amurica.txt',
								'inputs': 'challenges/inputs/amurica.txt',
								'name': 'Amurica'}
challenges['hwat'] =  {'problem': 'challenges/descriptions/hwat.txt',
								'inputs': 'challenges/inputs/hwat.txt',
								'name': 'HWAT?'}
challenge_keys =['baby_elevator', 'like_a_gauss', 'long_and_hard',
				'amurica', 'antsy', 'greenie', 'hippies', 'real_life' , 'hwat']


committee_names = ['Community Service', 'Consulting', 'Finance', 'Marketing', 'Historian', 'Publications', 
	'Professional Development', 'Social', 'Internal Networking', 'Web Development']