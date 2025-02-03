import pymongo

def connect_to_db():
    try:
        uri = "mongodb+srv://iamahmedkhan02:LMS_database@cluster0.ng8t3.mongodb.net/"
        client = pymongo.MongoClient(uri)
        db = client["LMS_database"]
        return db
    except Exception as e:
        print(f"error ocurred while connecting to database: {e}")


def create_collection(collection):
    try: 
        db = connect_to_db()
        collection = db[f"{collection}"]
        return collection
    except Exception as e:
        print(f"error occurred while accessing {collection} collection")

