import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        # TODO: Update with appropriate MongoDB connection information
        url = "mongodb://course2cosmosmongodb:8r0sp16yJzd8mCngBQmNUUeibYtg2LvF8lNJXv9A3GoJRzKmieX2rCGVTCnDTR4sxQJNTJoZuLdnB0ULjkhROw==@course2cosmosmongodb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@course2cosmosmongodb@"  
        client = pymongo.MongoClient(url)
        database = client['course2database']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

