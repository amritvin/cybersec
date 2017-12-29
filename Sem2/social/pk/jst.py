
import facebook
import simplejson
import urllib2
import json
from nltk import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import ngrams
stopwords_english = stopwords.words('english')
stemmer=PorterStemmer()
api_key = {
			'api_key': '122443011878876',
			'api_secret': '0595dccd68ebb3aafc637997c550b03f',
			'access_token':	'EAABvXHw6b9wBALjtSOOG2Qed7L9re83MQOX6IrZCRQEXjvJyETrWU2KTDDprgeq0POwJpz8hyZBojNI10nyvL2RmOLhw89hhhZBRYliHSSdZCKOBDQZAV1RZBX6o7ZAyqld8LtUlE6BZBChWNFiKHLc5Xgs8fKMhTu5z6tGvfGR8ZCAZDZD'
		}
# Initializing the Facebook Graph API object
graph = facebook.GraphAPI(access_token= api_key['access_token'])

# Calling the method of the Graph API to get data
post = graph.get_object("me?fields=posts,address,education,birthday,about,likes{name},friendlists{name},religion,political")
graph.put_wall_post(message='hello how are you all???')
print post
