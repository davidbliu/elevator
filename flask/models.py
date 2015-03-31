
class Contestant:

	def __init__(self, name, committee):
		print 'hello'
		self.scores = {}

	def get_score(self):
		return 10

class Committee:

	def __init__(self, name, cid, password = 'asdf'):
		print 'hello'
		self.name = name
		self.id = cid
		self.password = password

	def get_score(self):
		return 10
	def get_members(self):
		return []

class Score:

	def __init__(self):
		print 'initializing a score'