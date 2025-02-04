from authentication import check_auth
from connect import create_collection

@check_auth       
def remove_admin():
     try:
          admin_to_be_removed = input("enter admin username to be removed: ")
          collection = create_collection("admin")
          admin_removal = collection.find_one({"username": admin_to_be_removed})

          if admin_removal:
               collection.delete_one({"username": admin_to_be_removed})
               print("Admin removed successfully")
          else:
               print(f"Admin with username {admin_to_be_removed} is not found")

     except Exception as e:
          print(f"Error ocurred while removing an admin {e}")

remove_admin()