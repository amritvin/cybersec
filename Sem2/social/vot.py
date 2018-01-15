import requests
r = requests.get("http://cultivatingchange.org/vote/?entry_id=170957278")
#http://wshe.es/5EUWI7C1
#print r.status_code
print r.text
