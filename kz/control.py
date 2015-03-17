

class Control(object):

	def __init__(self, elevators):
		self.elevators = elevators
		self.floors = 49
		self.requests = []
		#requests = (name, t, start, dest)

		self.time = 0

	def hasRequests(self):
		return len(self.requests) > 0

	def receive(self, inp):
		inp = inp.split()
		#print inp
		name = inp[0]
		time = int(inp[12])
		start = int(inp[3])
		dest = int(inp[9])

		req = [name,time,start,dest]
		self.requests.append(req)

	def handleRequest(self):
		request = self.requests.pop(0)
		#print request
		elv = self.elevators[0]
		dest = request[3]
		start = request[2]

		print("At time %d move elevator %d to floor %d" % (self.time, elv.num, start))
		print("Elevator at floor %d going %s" % (start, elv.state))
		self.time += abs(start - elv.floor)


		#Waiting for request to be made
		if self.time < request[1]:
			self.time = request[1]




		
		elv.move(dest)

		print("At time %d move elevator %d to floor %d" % (self.time, elv.num, elv.floor))
		print("Elevator at floor %d going %s" % (elv.floor, elv.state))
		self.time += abs(dest - start)





