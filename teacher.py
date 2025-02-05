from admin_operations import retrieve_students_on_status, update_student_marks_and_status

def teacher_work():
        print("Welcome Teacher!")
        print("Which operation would you like to operate?")
        print("Enter 1 or 2 for operations")
        print("1. Retrieve students in base of thier status")
        print("2. Update students marks and status")

def teacher_work_on_students():
    try:
        teacher_work()
        operation  = input("enter no of the operration: ")

        if operation == "1":
                retrieve_students_on_status()
        elif operation == "2":
                update_student_marks_and_status()
        else:
                print("Invalid Input!")

    except Exception as e :
        print(f"Error while handling students operations: {e}")

