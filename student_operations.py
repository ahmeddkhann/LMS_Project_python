from requirements import requirements
from connect import create_collection

def add_student():
    try:   
        user_details = requirements()
        if len(user_details) == 6:
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
