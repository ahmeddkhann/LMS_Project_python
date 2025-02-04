from admin_operations import add_user, update_user, remove_user, retrieve_user_list

def admin_work():
        print("Welcome Admin!")
        print("Which operation would you like to operate?")
        print("Enter 1 2 3 etc for operations")
        print("1. Add user")
        print("2. Update User")
        print("3. Retrieve list of the required user")
        print("4: Delete a user")
        print("5. Exit program")

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


admin_work_on_admins()