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
def followers_tweets(next_cursor):
	while(next_cursor):
		search = twitter.get_followers_list(screen_name='ndtvgadgets',count=200,cursor=next_cursor)
		for result in search['users']:
			time_zone =result['time_zone'] if result['time_zone'] != None else "N/A"
        	print result["name"].encode('utf-8')+ ' '+time_zone.encode('utf-8')
    	next_cursor = search["next_cursor"]

# First parameter: The keyword we wish to search for
# Second parameter: Total tweets you wish to collect
followers_tweets()
