from twython import Twython
import requests
import subprocess
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from collections import Counter
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

ut=twitter.get_user_timeline(screen_name='ponguru',count=70,tweet_mode="extended")
#print ut[1]['entities']['media'][0]['media_url_https']
imgdict={}
i=1
for tweets in ut:
	if "entities" in tweets:
		if "media" in tweets["entities"]:
			for med in tweets["entities"]["media"]:
				if med["type"]=="photo":
					if "media_url_https" in med:
						imgdict[i]= med["media_url_https"].encode('ascii','ignore')
						i+=1

i=1
for ele in imgdict:
	url = imgdict[ele]
	response = requests.get(url)
	if response.status_code == 200:
    		with open("/home/amrit/mtechmaster/cybersec/Sem2/social/pk/image_reso/"+"pktweet"+str(i)+".jpg", 'wb') as f:
        		f.write(response.content)
	i+=1

scoredict={}
for j in range(1,i):
	s=subprocess.check_output(['python','/home/amrit/Downloads/models-master/tutorials/image/imagenet/classify_image.py','--image_file','/home/amrit/mtechmaster/cybersec/Sem2/social/pk/image_reso/pktweet'+str(j)+'.jpg'])
	scoredict[j]=s
	print "pktweet"+str(j)+"                          -- ok"
 
li=[]
for ele in scoredict:
	bigrams_score=scoredict[ele].split('\n')[0]
	li.append(bigrams_score)

sword=[]
stopwords_english=stopwords.words('english')
for st in stopwords_english:
        st=st.encode('ascii','ignore')
        sword.append(st)


#li=['mortarboard (score = 0.85993)', 'unicycle, monocycle (score = 0.74411)', 'unicycle, monocycle (score = 0.74411)', 'barbershop (score = 0.12227)', 'toyshop (score = 0.26902)', 'water jug (score = 0.06595)', 'envelope (score = 0.27719)', "academic gown, academic robe, judge's robe (score = 0.53995)", 'carton (score = 0.67161)']

text=""
all_bigrams=[]
for ele in li:
	sub=ele.split("(score")[0]
	b=sub.split(",")
	s=""
	for e in b:
		s=s+e+" "
	text=text+s+" "
	all_bigrams+=b

frequencies = Counter(all_bigrams)
for token,count in frequencies.most_common(10):
	#if token in stopwords_english or len(token)<3:
		#continue
	print token,count
wordcloud = WordCloud(relative_scaling = 1.0, background_color='white',
                              stopwords = sword # set or space-separated string
                              ).generate(text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

