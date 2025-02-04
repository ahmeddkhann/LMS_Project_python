from authentication import check_auth
from connect import create_collection
from requirements import requirements
from requirements import update_requirements

collection = create_collection("admin")

@check_auth
def add_admin():
    try:   
        user_details = requirements()
        if len(user_details) == 4:
              name, username, password, role = user_details
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

@check_auth       
def remove_admin():
     try:
          admin_to_be_removed = input("enter admin username to be removed: ")
          admin_removal = collection.find_one({"username": admin_to_be_removed})

          if admin_removal:
               collection.delete_one({"username": admin_to_be_removed})
               print("Admin removed successfully")
          else:
               print(f"Admin with username {admin_to_be_removed} is not found")

     except Exception as e:
          print(f"Error ocurred while removing an admin {e}")


@check_auth
def retrieve_admin_list():
     try:
          admins = list(collection.find({"role": "admin"}, {"_id":0 , "name": 1, "username": 1}))
          if admins:
            for admin in admins:
               print(f"Admin name: {admin["name"]}")
               print(f"Admin username: {admin["username"]}")
               print()
          else:
               print("No admins found")
     except Exception as e:
          print(f"Error while retrieving admin list: {e}")

@check_auth
def update_admin():
     try:
          username = input("enter username of the admin to be updated: ")
          find_Admin = collection.find_one({"username": username})
          
          if find_Admin:
               name, new_username, password = update_requirements()
               result = collection.update_one({"username": username},{"$set": 
               {
                    "name": name,
                    "username": new_username,
                    "password": password
               }})
               if result.matched_count > 0:
                    print("Admin updated successfully")
               else:
                    print("couldnot updated admin details")

          else:
               print(f"Admin with username {username} is not found")
     except Exception as e :
          print(f"Error while updating admin: {e}")

              



        