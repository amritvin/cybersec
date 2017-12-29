import json
import time
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


# Insert data in a MongoDB database
def insert_data(post):
	client = MongoClient()
	db = client.amrita_psosm

	post['_id'] = post['id']
	try:
		db.tweets_collected.insert(post)
	except Exception as e:
		print e

def search_tweets(search_phrase, maxTweets):

	# ID of the earliest tweet in the list
	id_of_earliest_tweet = None

	count = 0
	tweetCount = 0

	while tweetCount < maxTweets:
		list_of_tweets = []

		if id_of_earliest_tweet <= 0:
			new_statuses = twitter.search(q=search_phrase, count="100", include_entities= True)

		else:
			new_statuses = twitter.search(q=search_phrase, count="100", include_entities = True, max_id=id_of_earliest_tweet - 1)

		tweetCount += len(new_statuses['statuses'])

		print tweetCount

		for tweet in new_statuses['statuses']:
			count += 1
			print json.dumps(tweet)
			list_of_tweets.append(tweet['id'])

			# Saving data in a MongoDB collection
			insert_data(tweet)

			# Saving data in files

			# with open('/home/kushagra/modi_twitter/tweet'+str(count)+'.json', 'w') as outfile:
			# 		json.dump(post,outfile)

		id_of_earliest_tweet = sorted(list_of_tweets)[0]


		# print tc

	print "Total tweets: ", tweetCount

# First parameter: The keyword we wish to search for
# Second parameter: Total tweets you wish to collect
search_tweets('#PanamaPapers',10000)
