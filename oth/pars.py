import feedparser
import sys
url=sys.argv[1] #url of the website
"""The db must be updated/deleted after each upload"""
db='feeds.db' #The Database saved locally which contains all the data
feed=feedparser.parse(url)  #All the feeds get downloaded
f=open(db,'a')
for post in feed.entries: #Creating an object called post to carry all the entries
    s = post.start_date
    s = s.join(s[0:3]+"-")
    f.write(post.title+"\n"+post.start_date+"\t"+post.finish_date+"\n"+post.url+"\n"+post.description)
    """Writing to the database the title,link,time and the description of the ctf"""
f.close
