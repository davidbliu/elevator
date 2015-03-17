class Elevator(object):

	def __init__(self, num, floor):
		self.num = num
		self.floor = floor
		self.state = "up"



	def move(self, dest):
		if self.floor > dest:
			self.state = "down"
		else:
			self.state = "up"
		self.floor = dest