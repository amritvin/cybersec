simport json
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
	tweet1=tweet.split("RT")
	if len(tweet1)==2:
		tweet=tweet1[1]
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ",tweet).split())

def st(sp):
	dicy={}
i	i=1
	all_tokens=[]
	all_bigrams=[]
	ut=twitter.get_user_timeline(screen_name=sp,tweet_mode='extended',count=200)
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
	newtext=""
	print"BIGRAMS :"
	for token,count in frequencies.most_common(10):
		newtext=newtext+" " +(token[0]+" ")*count+" "+(token[1]+" ")*count
		x=token[0].encode('ascii','ignore')
		y=token[1].encode('ascii','ignore')
		print x," ",y, count

	text = newtext
	for wrd in all_unigrams_without_noise:
		wrd=wrd.encode('ascii','ignore')

	analyzer = SentimentIntensityAnalyzer()
	twt={}
	pos={}
	neg={}
	neu={}
	i=0
	j=0
	k=0
	temp=[]
	for s in dicy:
		vs = analyzer.polarity_scores(dicy[s])
		if float(vs['compound'])> 0.5:
			temp.append(dicy[s])
			temp.append((float(vs['compound'])))
			pos[i]=temp
			temp=[]
			i+=1
		else:
			if float(vs['compound'])<= -0.5:
				temp.append(dicy[s])
				temp.append(float(vs['compound']))
				neg[j]=temp
				temp=[]
				j+=1
			else:	#if float(vs['compound'])>=0.5 and float(vs['compound'])<=-0.5:
				temp.append(dicy[s])
				temp.append(float(vs['compound']))
				neu[k]=temp
				temp=[]
				k+=1
	"""
	print "\n\nNEGATIVE \n"
	for twts in neg:
		print neg[twts][0],"\n\t",neg[twts][1]
	print "\n\nPOSITIVE\n"
	for twts in pos:
                print pos[twts][0],"\n\t",pos[twts][1]
	print"\n\nNEUTRAL\n"
        for twts in neu:
                print neu[twts][0],"\n\t",neu[twts][1]

	"""
	for sen in dicy:
		 text = text+dicy[sen]+" "

	cp=float(len(pos))
	cn=float(len(neg))
	cnu=float(len(neu))
	print"------------------------------------------------------------------------------------------"
	print " \nANALYSIS \n\n","POSITIVE POSTS :",str((cp/len(dicy))*100)+"%","\n NEGATIVE POST :",str((cn/len(dicy))*100)+"%"," \n NEUTRAL POST :",str((cnu/len(dicy))*100)+"%"
	print"-------------------------------------TIMELINE----------------------------------------------"
	print "\n\nPOSITIVE TWEETS\n"
        for twts in pos:
                print pos[twts][0],"\n\t-----\t\t",pos[twts][1]
	print"\n\nNEUTRAL TWEETS\n"
        for twts in neu:
                print neu[twts][0],"\n\t-----\t\t",neu[twts][1]
	print "\n\nNEGATIVE TWEETS \n"
        for twts in neg:
                print neg[twts][0],"\n\t-----\t\t",neg[twts][1]


	wordcloud = WordCloud(relative_scaling = 1.0, background_color='white',
	                      stopwords = sword # set or space-separated string
	                      ).generate(text)
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()


st('ponguru')
