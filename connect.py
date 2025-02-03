import pymongo

def connect_to_db():
    try:
        uri = "mongodb+srv://iamahmedkhan02:LMS_databaset@cluster0.ng8t3.mongodb.net/"
        client = pymongo.MongoClient(uri)
        db = client["LMS_database"]
        return db
    except Exception as e:
        print(f"error ocurred while connecting to database: {e}")


def student_collection():
    try: 
        db = connect_to_db()
        collection = db["students"]
        return collection
    except Exception as e:
        print(f"error occurred while accessing students collection")

def teacher_collection():
    try: 
        db = connect_to_db()
        collection = db["teachers"]
        return collection
    except Exception as e:
        print(f"error occurred while accessing students collection")

def student_collection():
    try: 
        db = connect_to_db()
        collection = db["admins"]
        return collection
    except Exception as e:
        print(f"error occurred while accessing students collection")
