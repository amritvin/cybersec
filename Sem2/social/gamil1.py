import requests
r= requests.get('http://localhost/FeedBack/out.html     ')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
payload1 = {'Passwd':'c.amritanand'}
url1='https://accounts.google.com/signin/challenge/sl/password'
p1=requests.post(url1, data=payload1)
print p1.content
