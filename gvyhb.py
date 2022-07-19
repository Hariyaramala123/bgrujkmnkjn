import pymongo
client = pymongo.MongoClient("mongodb+srv://Hariyaramala1:9160943829@cluster0.nonigju.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name":"hari",
    "email" : "hari@ineuron.ai",
    "surname" : "reddy"
}
print(d)
