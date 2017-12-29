dic={}
i=1
user_timeline = twitter.get_user_timeline(screen_name=search_key, tweet_mode='extended',count=50)
for tweets in user_timeline:
    dic=tweets['full_text']
