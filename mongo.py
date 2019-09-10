
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb+srv://neilmckibben:nsm5574903@cluster0-n4arl.mongodb.net/test?retryWrites=true&w=majority')
db=client.test
def findUser(email):
    collection = db.users
    test = collection.find_one({"email": "admin@example.com"})
    pprint(test["status"]["admitted"])

# Issue the serverStatus command and print the results
collection = db.users
cursor = collection.find({})
# for document in cursor:
#     pprint(document)

findUser('admin@examplee.com')
