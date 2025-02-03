
def requirements():

    print("Enter the following details are been asked")
    name = input("1.Name: ")
    username = input("2.Username: ")
    password = input("3.Password: ")
    role = input("4.Role: ")
    
    if role == "student":
        marks = input("enter marks: ")
        status = input("enter status: ")
        return name, username, password, role, marks, status

    return name, username, password, role

    
    