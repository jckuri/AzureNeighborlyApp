import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            # TODO: Update with appropriate MongoDB connection information
            url = "mongodb://course2cosmosmongodb:8r0sp16yJzd8mCngBQmNUUeibYtg2LvF8lNJXv9A3GoJRzKmieX2rCGVTCnDTR4sxQJNTJoZuLdnB0ULjkhROw==@course2cosmosmongodb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@course2cosmosmongodb@"  
            client = pymongo.MongoClient(url)
            database = client['course2database']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )
