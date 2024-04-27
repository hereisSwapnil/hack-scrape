import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)

def addHackathonsToMongoDB_old(hackathon_data):
        db_name = "hackathons"
        col_name = "hackathon_data"
        db = client[db_name]
        col = db[col_name]

        for hackathon in hackathon_data:
            query = {"name": hackathon["name"]}
            update = {"$set": hackathon}
            upsert = True
            results = col.find(query)
            updated = False
            for document in results:
                # print(document["name"])
                col.update_one({"_id": document["_id"]}, update)
                updated = True
            if(not updated):
                col.insert_one(hackathon)
    
def addHackathonsToMongoDB(hackathon_data):
        db_name = "hackathons"
        col_name = "hackathon_data"
        db = client[db_name]
        col = db[col_name]
        col.delete_many({})
        for hackathon in hackathon_data:
            col.insert_one(hackathon)

if __name__ == "__main__":
    addHackathonsToMongoDB(hackathon_data)