import pymongo
#client = pymongo.MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017/')
client = pymongo.MongoClient("mongodb+srv://admin:Avc1cvDiYx0ZrapR@cluster0-4rkef.mongodb.net/test?retryWrites=true")

db = client['test_Database']
#db = client.test_database

collection = db['espol']
#collection = db.espol

post = {"materia":"Software Engineering", "attr2":"value2", "attr3":"value3"}
#collection.insert_one(post)

for document in collection.find():
	print(document)
