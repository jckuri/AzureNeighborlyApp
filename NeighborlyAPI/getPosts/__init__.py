import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Python getPosts trigger function processed a request.')
    
    try:
        # TODO: Update with appropriate MongoDB connection information
        url = "mongodb://course2cosmosmongodb:8r0sp16yJzd8mCngBQmNUUeibYtg2LvF8lNJXv9A3GoJRzKmieX2rCGVTCnDTR4sxQJNTJoZuLdnB0ULjkhROw==@course2cosmosmongodb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@course2cosmosmongodb@"  
        client = pymongo.MongoClient(url)
        database = client['course2database']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)
