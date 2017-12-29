import requests
r= requests.get('https://accounts.google.com/ServiceLogin')

payload = {'Email':'c.amritanand'}
url = 'https://accounts.google.com/signin/v1/lookup'
p=requests.post(url, data=payload)
print p.text
