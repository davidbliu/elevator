
from parse_rest.datatypes import Object
from parse_rest.connection import register
import sys
application_id = 'r1fyuEduAW4upM4ZZJsz54iHpg6o7ZT6jWw0Z7We'
client_key = 'K2mxfXT12kpvSm4p2rdRt8GU9ipUDaYTfwRsLinK'


register(application_id, client_key)


class Score(Object):
	pass

scores = Score.Query.all()

args = sys.argv[1]

badnames = set(args.split(','))
for score in scores:
	if score.name in badnames:
		print 'deleting score '+str(score.name)
		# score.delete()
		print score.solution
