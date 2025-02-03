from connect import create_collection

def check_auth():
    try:
        print("Following details are requird for authentication: ")
        print("1.Username")
        print("2.Password")
        print("3.role")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        role = input("Enter your role: ")

        def check_validation():
          collection = create_collection(role)
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
        return is_validated
    
    except Exception as e:
        print("An error occurred while checking user credentials: ", str(e))
