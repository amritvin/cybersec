from twython import Twython
import requests
import subprocess
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import json
from highcharts import Highchart

from pymongo import MongoClient
client=MongoClient()
db=client.mytweets

post={}

#db.data_collected.insert(post)

api_key={
        'api_key': 'hRWSfRZcu5970AlvrC5JMxpce',
        'api_secret': 'axUYpV8Ah6mef4KHTU0W9iUwwPO1diR2hU4nScVIyobFYjYM8t',
        'access_token': '492157369-uSiBPXVKWwW5GVPR09Nj81qJsIBGXZlRDSsBZCo9',
        'access_token_secret': 'tYWyyVwiwzAPnEq7y1H95mAV2hnovcwTc4Mtoz9vuolyp'
}
twitter= Twython(api_key['api_key'],
                                api_key['api_secret'],
                                api_key['access_token'],
                                api_key['access_token_secret']
                                )
def search_tweets(search_phrase, maxTweets):
	

	# ID of the earliest tweet in the list
	id_of_earliest_tweet = None
	monthcal ={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,
'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
	count = 0
	tweetCount = 0
	list_of_tweets = []
	c=1
	
	try:
		while tweetCount < maxTweets:
                	list_of_tweets = []

                	if id_of_earliest_tweet <= 0:
                        	new_statuses = twitter.get_user_timeline(screen_name=search_phrase,tweet_mode="extended")

                	else:
                        	new_statuses = twitter.get_user_timeline(screen_name=search_phrase,tweet_mode="extended",max_id=id_of_earliest_tweet - 1)

                	tweetCount += len(new_statuses)

                #print tweetCount
                	temp=[]
                	for tweet in new_statuses:
                        	temp.append(json.dumps(tweet['full_text']))
                        	temp.append(json.dumps(tweet['created_at']))
                            	temp.append(json.dumps(tweet['id']))
                        	post[c]=temp
                        	temp=[]
                        	c+=1
				list_of_tweets.append(tweet['id'])
			id_of_earliest_tweet = sorted(list_of_tweets)[0]

	except:
		print tweetCount ,"[Error]"
	print post
	my={}
	tweetsco={}
	for ele in post:
		tw=post[ele][0]
		dat=post[ele][1].split(" ")
		m=monthcal[str(dat[1])]
		d=dat[2]
		y=dat[5].split("\"")[0]
        	my['_id']=post[ele][2]
		my['tweet']=tw
		my['month']=m
		my['year']=y
		print my
		#weetsco['_id']=post[ele][2]
        	#tweetsco[str(ele)]=my
		try:
                	db.tweets_collected.insert(my)
        	except Exception as e:
                	print e

		my={}
    
	
	tot9=db.tweets_collected.find({"year":"2009"}).count()
	tot10=db.tweets_collected.find({"year":"2010"}).count()
	tot11=db.tweets_collected.find({"year":"2011"}).count()
	tot12=db.tweets_collected.find({"year":"2012"}).count()
	tot13=db.tweets_collected.find({"year":"2013"}).count()
	tot14=db.tweets_collected.find({"year":"2014"}).count()
	tot15=db.tweets_collected.find({"year":"2015"}).count()
	tot16=db.tweets_collected.find({"year":"2016"}).count()
	tot17=db.tweets_collected.find({"year":"2017"}).count()
	

	haf9=db.tweets_collected.find({"year":"2009","month":{"$gt":6}}).count()
        haf10=db.tweets_collected.find({"year":"2010","month":{"$gt":6}}).count()
        haf11=db.tweets_collected.find({"year":"2011","month":{"$gt":6}}).count()
        haf12=db.tweets_collected.find({"year":"2012","month":{"$gt":6}}).count()
        haf13=db.tweets_collected.find({"year":"2013","month":{"$gt":6}}).count()
        haf14=db.tweets_collected.find({"year":"2014","month":{"$gt":6}}).count()
        haf15=db.tweets_collected.find({"year":"2015","month":{"$gt":6}}).count()
        haf16=db.tweets_collected.find({"year":"2016","month":{"$gt":6}}).count()
        haf17=db.tweets_collected.find({"year":"2017","month":{"$gt":6}}).count()
	
	faf9=tot9-haf9
	faf10=tot10-haf10
	faf11=tot11-haf11
	faf12=tot12-haf12
	faf13=tot13-haf13
	faf14=tot14-haf14
	faf15=tot15-haf15
	faf16=tot16-haf16
	faf17=tot17-haf17
		
	
	chart = Highchart()
	options = {
        'chart': {'type': 'line'},
        'title': {'text': 'PK\'s TIME-LINE'},
        'legend': {'enabled':True}, 
        'xAxis': {
                'categories': ['Jan-Jun_09','Jul-Dec_09','Jan-Jun_10','Jul-Dec_10','Jan-Jun_11','Jul-Dec_11','Jan-Jun_12','Jul-Dec_12','Jan-Jun_13','Jul-Dec_13','Jan-Jun_14','Jul-Dec_14','Jan-Jun_15','Jul-Dec_15','Jan-Jun_16','Jul-Dec_16','Jan-Jun_17','Jul-Dec_17','Jan-Jun_18','Jul-Dec_18'] 
  },
        'yAxis':{
                        'title': {'text': 'Number of Tweets'}
        },
	}

	data1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	data2 = [0,0,0,0,0,0,0]
	data3 = [0,0,0,0,0,0,0,0,0,0]
	data1[0]=faf9
	data1[1]=haf9
	data1[2]=faf10
	data1[3]=haf10
	data1[4]=faf11
	data1[5]=haf11
	data1[6]=faf12
	data1[7]=haf12
	data1[8]=faf13
	data1[9]=haf13
	data1[10]=faf14
	data1[11]=haf14
	data1[12]=faf15
        data1[13]=haf15
        data1[14]=faf16
        data1[15]=haf16
        data1[16]=faf17
        data1[17]=haf17



	chart.set_dict_options(options)

	chart.add_data_set(data1,'line','PK')

	chart.save_file('./pktweetplot')

search_tweets("ponguru",1950)
