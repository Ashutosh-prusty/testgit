import pymongo
client = pymongo.MongoClient("mongodb+srv://prustyashutosh456:atpbulu123@ashutosh456.enbgpeu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name":"ashu",
    "email" : "ashu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )


