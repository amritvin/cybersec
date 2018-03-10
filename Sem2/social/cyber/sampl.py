from pymongo import MongoClient
client=MongoClient()
db=client.sample
s=raw_input("Name of the tool\n")
usage=raw_input("usage: \n")
s1=raw_input("Discription\n")
mat={"Name": s,"usage":usage,"Disc":s1 }
db.collected_mat.insert(mat)
