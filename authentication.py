from connect import create_collection

def check_auth(func): 
    def wrapper (*args, **kwargs): 

        try:
            print("Following details are requird for authentication: ")
            print("1.Username")
            print("2.Password")
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            def check_validation():
                collection = create_collection("admin")
                user_document = collection.find_one({"username": username})
                if user_document:

                    if user_document["password"] == password:
                        print("Authentication Verified.")
                        return True
                    else:
                        print("Authentication failed. Please check your password.")
                        return False

                else:
                    print("Authentication failed. Please check your username.")
                    return False
            
            is_validated = check_validation()
            if is_validated:
                return func(*args, **kwargs)

        except Exception as e:
            print("An error occurred while checking user credentials: ", str(e))
    
    return wrapper
