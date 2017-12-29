from pymongo import MongoClient
client=MongoClient()
db=client.psosm
post={"name":"jesty","roll":33}
db.data_collected.insert(post)
client.close()
