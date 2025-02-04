from authentication import check_auth
from connect import create_collection
from requirements import requirements

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


def update_admin():
     try:
          username = input("enter username of the admin to be updated: ")
          find_Admin = collection.find_one(find_Admin)
          
          if find_Admin:
               name = input("Enter new name: ")
               username = input("Enter new username: ")
               password = input("Enter new password: ")
               collection.update_one({"$set": 
               {
                    "name": name,
                    "username": username,
                    "password": password
               }})
               print("Admin data updated successfully")

          else:
               print(f"Admin with username {username} is not found")
     except Exception as e :
          print(f"Error while updating admin: {e}")


              



        