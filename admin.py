from admin_operations import add_user, update_user, remove_user, retrieve_user_list, retrieve_students_on_status, update_student_marks_and_status
def admin_work():
        print("Welcome Admin!")
        print("Which operation would you like to operate?")
        print("Enter 1 2 3 etc for operations")
        print("1. Add user")
        print("2. Update User")
        print("3. Retrieve list of the required user")
        print("4: Delete a user")
        

def admin_work_on_admins():
    try:
        admin_work()
        operation  = input("enter no of the operration: ")

        if operation == "1":
                add_user("admin")
        elif operation == "2":
                update_user("admin")
        elif operation == "3":
                retrieve_user_list("admin")
        elif operation == "4":
                remove_user("admin")
        else:
                print("Invalid Input!")

    except Exception as e :
        print(f"Error while handling admin operations: {e}")

def admin_work_on_teachers():
    try:
        admin_work()
        operation  = input("enter no of the operration: ")
        if operation == "1":
                add_user("teacher")
        elif operation == "2":
                update_user("teacher")
        elif operation == "3":
                retrieve_user_list("teacher")
        elif operation == "4":
                remove_user("teacher")
        else:
                print("Invalid Input!")

    except Exception as e :
        print(f"Error while handling teacher operations: {e}")

def admin_work_on_students():
    try:
        admin_work()
        print("5. update student marks and status: ")
        print("6. retrieve student status list: ")
        operation  = input("enter no of the operration: ")

        if operation == "1":
                add_user("student")
        elif operation == "2":
                update_user("student")
        elif operation == "3":
                retrieve_user_list("student")
        elif operation == "4":
                remove_user("student")
        elif operation == "5":
                update_student_marks_and_status()
        elif operation == "6":
                retrieve_students_on_status()
        else:
                print("Invalid Input!")

    except Exception as e :
        print(f"Error while handling students operations: {e}")


admin_work_on_students()

