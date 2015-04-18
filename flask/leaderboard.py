from seeds import *

VALID_COMMITTEES = set(['CO', 'CS', 'FI', 'MK', 'HT', 'PB', 'PD', 'SO', 'IN', 'WD', 'EX'])

def get_overall_leaders(scores):

	names = [x.name for x in scores]
	names = set(names)
	names = list(names)
	
	maps = get_score_maps(scores)
	name_map = maps['name_map']
	challenge_map = maps['challenge_score_map']

	leaders = []

	for name in names:
		score = 0
		all_scores = {}

		for challenge in challenge_keys:
			# score for challenge is rank in list
			if challenge in name_map[name].keys():
				my_score_this_challenge = name_map[name][challenge]
				all_scores[challenge] = my_score_this_challenge
				score += 50 - (challenge_map[challenge].index(my_score_this_challenge)/float(len(names)) * 50)
			else:
				score += 0 #len(challenge_map[challenge]
				all_scores[challenge] = 'n/a'
		leaders.append({'name':name, 'score':round(score, 2), 'committee': 'no','scores':all_scores})
	leaders = sorted(leaders, key= lambda x: -x['score'])
	return leaders

def sort_leaders_by_challenge_name(leaders, challenge_name):
	def comparator(x):
		score = x['scores'][challenge_name]
		if score == 'n/a':
			return 50
		else:
			return x['scores'][challenge_name]
	return sorted(leaders, key = comparator)

def get_score_maps(scores):
	challenge_map = {}
	name_map = {}
	for score in scores:
		ch = score.challenge
		name = score.name
		if name not in name_map.keys():
			name_map[name] = {}
		name_map[name][score.challenge] = score.score
		if ch not in challenge_map.keys():
			challenge_map[ch] = []
		challenge_map[ch].append(score.score) # save the scores for each person
	for key in challenge_map.keys():
		challenge_map[key] = sorted(challenge_map[key])
	return {'challenge_score_map': challenge_map, 'name_map':name_map}
# 
# returns data to help construct committee leaderboad
# 
def get_committee_leaderboard(scores):
	"""set participation scores"""
	pscores = Participation.Query.all()
	participation = {}
	for p in pscores:
		participation[p.committee] = p.score
	"""done using parse for participation scores"""
	committee_score_map = {}
	for committee in VALID_COMMITTEES:
		committee_score_map[committee] = {}
	for score in scores:
		committee = score.committee
		if committee in VALID_COMMITTEES:
			challenge = score.challenge
			my_scores = {}
			my_scores = committee_score_map[committee]
			if challenge not in my_scores.keys():
				my_scores[challenge] = {'scores':[]}
			my_scores[challenge]['scores'].append(score)
	# print committee_scores
	for committee in committee_score_map.keys():
		committee_scores = committee_score_map[committee]
		for challenge in committee_scores.keys():
			challenge_scores = [x.score for x in committee_scores[challenge]['scores']]
			committee_scores[challenge]['min'] = min(challenge_scores)

	maps = get_score_maps(scores)
	challenge_score_map = maps['challenge_score_map']
	completed_challenges = challenge_score_map.keys()

	committee_leaderboard = {}
	for committee in VALID_COMMITTEES:
		committee_leaderboard[committee] = {}
		# calculate score per challenge
		for challenge in challenge_score_map.keys():
			score_this_challenge = 0
			if committee in committee_score_map.keys() and challenge in committee_score_map[committee].keys():
				bestscore = committee_score_map[committee][challenge]['min']
				bestrank = challenge_score_map[challenge].index(bestscore)/float(len(challenge_score_map[challenge]))
				score_this_challenge = 50-50*bestrank
			committee_leaderboard[committee][challenge] = round(score_this_challenge,2)
		# calculate whole score
		print committee_leaderboard
		total_score = sum(committee_leaderboard[committee].values())
		total_score += participation[committee]
		committee_leaderboard[committee]['total_score'] = total_score


	ranked_committees = list(reversed(sorted(list(VALID_COMMITTEES), key = lambda x: committee_leaderboard[x]['total_score'])))
	print ranked_committees
	return {'committee_leaderboard': committee_leaderboard, 'committee_score_map': committee_score_map, 'ranked_committees': ranked_committees}



def get_num_challenges(scores):
	return len(list(set([x.challenge for x in scores])))


if __name__ == "__main__":
	from parse_rest.datatypes import Object
	from parse_rest.connection import register
	import sys
	application_id = 'r1fyuEduAW4upM4ZZJsz54iHpg6o7ZT6jWw0Z7We'
	client_key = 'K2mxfXT12kpvSm4p2rdRt8GU9ipUDaYTfwRsLinK'

	scores = Score.Query.all()
	get_committee_leaderboard(scores)


register(application_id, client_key)