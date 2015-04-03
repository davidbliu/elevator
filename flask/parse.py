from parse_rest.datatypes import Object
import seeds
from parse_rest.connection import register

application_id = 'r1fyuEduAW4upM4ZZJsz54iHpg6o7ZT6jWw0Z7We'
client_key = 'K2mxfXT12kpvSm4p2rdRt8GU9ipUDaYTfwRsLinK'


register(application_id, client_key)


class Score(Object):
	pass

dliu = Score.Query.filter(name='David Liu')
for score in dliu:
	print score.name
	print score.score