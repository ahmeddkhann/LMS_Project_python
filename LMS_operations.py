from admin import admin_work_on_admins , admin_work_on_students, admin_work_on_teachers
from teacher import teacher_work_on_students


def LMS_operations():
    print("******** Welcome to LMS ********")
    role = input("Enter your role (admin/teacher): ").lower()
    if role == "admin":
        print("you can work on the following ")
        print("1. Admins")
        print("2. Students")
        print("3. Teachers")
        choice = input("Enter your choice to work on (enter 1, 2 or 3): ")
        if choice == "1":
            admin_work_on_admins()
        elif choice == "2":
            admin_work_on_students()
        elif choice == "3":
            admin_work_on_teachers()
        else:
            print("Invalid choice")
    
    elif role == "teacher":
        teacher_work_on_students()

    else:
        print("Invalid role")

LMS_operations()