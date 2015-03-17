from elevator import Elevator
from control import Control

filename = 'test_input.txt'

with open(filename) as f:
	data = f.readlines()

e1 = Elevator(1,0)
e2 = Elevator(2,0)
c = Control([e1,e2])


for line in data:
	c.receive(line)


while c.hasRequests():
	c.handleRequest()


#while c.hasRequests:
