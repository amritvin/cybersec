import json
# import sys
import time
# import os
from pymongo import MongoClient
from twython import Twython

api_key = {
	'api_key': 'U7XdUDn1e1IHbVEhMi4XtuAdH',
	'api_secret': 'JjqoSpB7TTHaoPN5sCOWt61sroy28kE0ccNYdvXcjQ3NhrRdY3',
	'access_token': '492157369-HEzNNAbyBNslXh9gjzluUjuX0c2DR3UoxRn0Baws',
	'access_token_secret': 'h9M2JPBoL0EJbMMxHdQ2HjAHXI4uNfURREm6bE2i0lh8u'
}

twitter= Twython(api_key['api_key'],
				api_key['api_secret'],
				api_key['access_token'],
				api_key['access_token_secret']
				)

def search_tweets(search_phrase):


	count = 0
	tweetCount = 0
	list_of_tweets = []

	new_statuses = twitter.search(q=search_phrase, count="100", include_entities= True)


	tweetCount += len(new_statuses['statuses'])

	print tweetCount

	for tweet in new_statuses['statuses']:
		count += 1
		print json.dumps(tweet)
		list_of_tweets.append(tweet['id'])

		# Saving data in files

		with open('/home/amrit/smog/tweet'+str(count)+'.json', 'w') as outfile:
				json.dump(tweet,outfile)

	print "Total tweets: ", tweetCount

# First parameter: The keyword we wish to search for
search_tweets('#namo')
