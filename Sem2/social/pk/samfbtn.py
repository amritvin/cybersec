#jestys program
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
post = graph.get_object("narendramodi"+'/feed',fields='caption,description,from,message,created_time,full_picture,id,link,status_type,story,story_tags,type,updated_time,with_tags,is_popular,actions')
all_tokens=[]
all_stemmed_tokens=[]
all_bigrams=[]
for status in post['data']:
	if 'message' in status:
		tokens = word_tokenize(status['message'].lower())
		for word in tokens:
			if word in stopwords_english or len(word)<3:
				continue
			else:
				all_tokens.append(word)
		bigrams=list(ngrams(all_tokens,3))
		#all_tokens = all_tokens + tokens
		all_bigrams=all_bigrams+bigrams
for token in all_tokens:
	stemmed_token=stemmer.stem(token)
	all_stemmed_tokens.append(stemmed_token)

frequencies = Counter(all_bigrams)
for token,count in frequencies.most_common(30):
	#if token in stopwords_english or len(token)<3:
		#continue
	print token,count
