from authentication import check_auth
from connect import create_collection

from requirements import requirements

def add_admin():
    try:    
        user_details = requirements()
        if len(user_details) == 4:
              name, username, password, role = user_details

        collection = create_collection("admin")
        admin_data = {
              "name": name,
              "username": username,
              "password": password,
              "role": role
       }
        collection.insert_one(admin_data)
        print("Admin added successfully")

    except Exception as e:
         print(f"Error while adding user: {e}")
       
add_admin()
              



        