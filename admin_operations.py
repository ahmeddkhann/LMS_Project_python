from authentication import check_auth
from connect import create_collection
from requirements import requirements
from requirements import update_requirements

@check_auth
def add_user(user_role):
    try:   
        user_details = requirements()
        if len(user_details) == 4:
              name, username, password, role = user_details
              user_data = {
               "name": name,
               "username": username,
               "password": password,
               "role": role
          }
              collection = create_collection(user_role)
              collection.insert_one(user_data)
              print(f" added user with role: {role}")

        elif len(user_details) == 6:
             name, username, password, role, marks, status = user_details
             student_data = {
              "name": name,
              "username": username,
              "password": password,
              "role": role,
              "marks": marks,
              "status": status
       }
             collection = create_collection("students")
             collection.insert_one(student_data)
             print(f" added user with role: {role}")
        
    except Exception as e:
         print(f"Error while adding user: {e}")


@check_auth
def remove_user(role):
     try:
          user_to_be_removed = input("enter user username to be removed: ")
          collection = create_collection(role)
          user_removal = collection.find_one({"username": user_to_be_removed})

          if user_removal:
               collection.delete_one({"username": user_to_be_removed})
               print("user removed successfully")
          else:
               print(f"Admin with username {user_to_be_removed} is not found")

     except Exception as e:
          print(f"Error ocurred while removing an admin {e}")

@check_auth
def retrieve_user_list(role):
     try:
          collection = create_collection(role)
          if role == "admin" or role == "teacher":
             users = list(collection.find({"role": role}, {"_id":0 , "name": 1, "username": 1}))
             if users:
                 for user in users:
                       print(f"user name: {user["name"]}")
                       print(f"user username: {user["username"]}")
                       print()
             else:
                print("No users are found")

          elif role == "students":
                users = list(collection.find({"role": "student"}, {"_id":0 , "name": 1, "username": 1, "marks": 1, "status": 1}))
                if users:
                   for user in users:
                       print(f"Student name: {user["name"]}")
                       print(f"Student username: {user["username"]}")
                       print(f"Student Marks: {user["marks"]}")
                       print(f"Student Status: {user["status"]}")
                       print()
                else:
                   print("No students found")

     except Exception as e:
          print(f"Error while retrieving admin list: {e}")

@check_auth
def update_user(role):
     try:
          username = input("enter username of the user to be updated: ")
          new_collection = create_collection(role)
          find = new_collection.find_one({"username": username})

          if find:
                    name, new_username, password = update_requirements()
                    collection = create_collection(role)
                    result = collection.update_one({"username": username},{"$set": 
                    {
                         "name": name,
                         "username": new_username,
                         "password": password
                    }})
                    if result.matched_count > 0:
                         print("user updated successfully")
                    else:
                         print("could not update user details")

              
     except Exception as e :
          print(f"Error while updating student: {e}")


def retrieve_students_on_status():
     try:
          print("Retrieve students based on their status")
          status = input("enter pass for pass students and fail for students that are failed: ").lower()
          collection = create_collection("students")
          if status == "pass" or status == "fail":
               students = list(collection.find({"status": status}, {
                   "_id": 0, "name": 1, "username": 1, "status": 1, "marks": 1
               }))

               if students:
                    for student in students:
                         print(f"Student name: {student['name']}")
                         print(f"Student username: {student['username']}")
                         print(f"Student Marks: {student['marks']}")
                         print(f"Student Status: {student['status']}")
                         print()              
               else:
                    print(f"No students found with the status: {status}")
          else:
               print("Invalid Status! enter pass or fail only.")

     except Exception as e:
          print(f"Error while retrieving students on status: {e}")


def update_marks():
     try:
          print("Update Student Marks")
          username = input("enter username of the student: ")
          collection = create_collection("students")
          student = collection.find_one({"username": username})

          if student:
               marks = int(input("Enter new marks: "))
               collection.update_one({"username": username}, {"$set": {"marks": marks}})
               return username
          else:
               print(f"Student with username: {username} is not found!")
     except Exception as e:
          print(f"Error while updating student marks: {e}")


     

              



        