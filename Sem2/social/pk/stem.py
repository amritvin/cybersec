import facebook
import json
from pymongo import MongoClient
from nltk import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import ngrams
stopwords_english= stopwords.words("english")
stemmer=PorterStemmer()
#access_token":"EAAOKyvp5zQABAOSEJXUxxmxDrX4PmGwZAyAZBSsKlcmzD6R6nZBhwZBkvhLPxuwH7m2qZBbV5rElLEkZBh8GF4bbtUbhUeLNxMoD3FJLruioZAjXYxmLjuNQnmZCOWcwgmJvxFCZBcpC3Sl8YpE2O1cwJJ4IqZBKVaThnmjn7gjvtUhwZDZD","token_type":"bearer","expires_in":5184000}
keytext={"app_id":"997029320445184",
    "appsecret":"677e68d3da49b0eede4c67642ed1a9ce",
    "access_token":"EAAOKyvp5zQABAOSEJXUxxmxDrX4PmGwZAyAZBSsKlcmzD6R6nZBhwZBkvhLPxuwH7m2qZBbV5rElLEkZBh8GF4bbtUbhUeLNxMoD3FJLruioZAjXYxmLjuNQnmZCOWcwgmJvxFCZBcpC3Sl8YpE2O1cwJJ4IqZBKVaThnmjn7gjvtUhwZDZD"
    }
graph = facebook.GraphAPI(keytext["access_token"])
feeds = graph.get_object("narendramodi"+'/feed',fields='caption,description,from,message,created_time,full_picture,id,link,status_type,story,story_tags,type,updated_time,with_tags,is_popular,actions')
"""
for status in feeds['data']:
	print json.dumps(status)
    db.posts_collected.insert(status)

print '\nTotal posts: ' + str(len(post['data']))
"""
all_tok=[]
all_stemmed_token=[]
for status in feeds['data']:
    if 'message' in status:
        token=word_tokenize (status['message'].lower())
        bgrams=list(ngrams(tokens,2))
        
        all_tok=all_tok+token

for token in all_tok:
    stemmed_tok=stemmer.stem(token)
    all_stemmed_token.append(stemmed_tok)


ferq=Counter(all_tok)
for token,count in ferq.most_common(25):
    #if token in stopwords_english or len(token)<3:
    #    continue
    print token,count
    #db.posts_collected.insert(status)
