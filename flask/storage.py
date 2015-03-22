import pickle
from checker import *
from seeds import *

#
# stores all data. this includes
#
def store_all():
	print 'storing all data'
	committees = []
	for i in committee_names:
		c = Committee(i, 'a')
		committees.append(c)
	print 'storing your data'
	pickle.dump(committees, open('save.p', 'wb'))

#
# loads all data. this includes
# 
def load_all():
	print 'loading all data'
	committees = pickle.load(open('save.p', 'rb'))
	print [c.name for c in committees]

print 'storing all da bullshiet'
# store_all()
load_all()