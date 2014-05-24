from pymongo import MongoClient
from bson.son import SON
client = MongoClient()
db = client['mydb']
iterator = db.location.find({"Postion" : SON([("$near",[9,10]),("$maxDistance",10)])})

for locs in iterator:
    print locs
