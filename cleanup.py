
from parse_rest.datatypes import Object
from parse_rest.connection import register
import sys
application_id = 'r1fyuEduAW4upM4ZZJsz54iHpg6o7ZT6jWw0Z7We'
client_key = 'K2mxfXT12kpvSm4p2rdRt8GU9ipUDaYTfwRsLinK'


register(application_id, client_key)


class Score(Object):
	pass


def cleanup_names(bad_names):
	scores = Score.Query.all()

	args = sys.argv[1]

	badnames = set(args.split(','))
	for score in scores:
		if score.name in bad_names:
			print 'deleting score '+str(score.name)
			score.delete()

def cleanup_committees():
	scores = Score.Query.all()
	for score in scores:
		name = score.name
		bracks = name.split('[')
		try:
			committee = bracks[1].split(']')[0]
			if committee != score.committee:
				print 'setting '+score.name+"'s committee to "+committee
				score.committee = committee
				score.save()
		except:
			print name+' is uncategorized'

if __name__=="__main__":
	
	# cleanup_committees()

	bad_names = ['Ian', 'asdf', 'ok', 'K', 'incredi_tester', 'poop', 'test', 'testes', 'Marketing', 'Poop', 'whee', 'fa']
	cleanup_names(bad_names)
	cleanup_committees()
	# cleanup_names(bad_names)
	# cleanup_committees()