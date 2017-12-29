import json
import re
from twython import Twython
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter
from nltk import ngrams


import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud, STOPWORDS
stemmer=PorterStemmer()
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sword=[]
stopwords_english=stopwords.words('english')
for st in stopwords_english:
	st=st.encode('ascii','ignore')
	sword.append(st)

api_key={
	'api_key': 'slF4KXLtgUvwpnafMldjCm4qs',
	'api_secret': 'a9feNqEmFAtFyi9kbMdV7WgEIwuQBDnjeqK6darR2JL9ZrQe6Z',
	'access_token': '492157369-gf7lLIa3YPyREQ4UY7HyVz99DJaQJetPp6ptRixM',
	'access_token_secret': 'w1YeBz0AYgDt6R1UPq1KbFl4wkmyz4FjI8Pe7k2cGbWMo'
}
twitter= Twython(api_key['api_key'],
				api_key['api_secret'],
				api_key['access_token'],
				api_key['access_token_secret']
				)
def clean_tweet(tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
def st(sp):
	dicy={}
	i=1
    all_tokens=[]
	all_bigrams=[]
	ut=twitter.get_user_timeline(screen_name=sp,tweet_mode='extended',count=50)
	for tweets in ut:
		dicy[i]=clean_tweet(tweets['full_text'])
		i+=1
    all_unigrams=[]
	all_stemmed_unigrams=[]
	all_unigrams_without_noise=[]

	for elements in dicy:
		unigrams = word_tokenize(dicy[elements].lower())
		all_unigrams = all_unigrams + unigrams
	for word in all_unigrams:
			stemmed_unigram = stemmer.stem(word)
			all_stemmed_unigrams.append(stemmed_unigram)
	for word in all_stemmed_unigrams:
			if word in stopwords_english or len(word) < 3:
				continue
			else:
				all_unigrams_without_noise.append(word)

	all_bigrams = list(ngrams(all_unigrams_without_noise,2))
	frequencies = Counter(all_bigrams)

	for token,count in frequencies.most_common(10):
		print token,count

	text = " "
	for wrd in all_unigrams_without_noise:
		wrd=wrd.encode('ascii','ignore')

	analyzer = SentimentIntensityAnalyzer()
	for s in dicy:
	    vs = analyzer.polarity_scores(dicy[s])
	    print dicy[s],"\n",(str(vs))

	for sen in dicy:
		 text = text+dicy[sen]+" "

	wordcloud = WordCloud(relative_scaling = 1.0, background_color='white',
	                      stopwords = sword # set or space-separated string
	                      ).generate(text)
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()


st('ponguru')
