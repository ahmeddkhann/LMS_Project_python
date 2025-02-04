
def requirements():

    print("Enter the following details that are been asked")
    name = input("1.Name: ")
    username = input("2.Username: ")
    password = input("3.Password: ")
    role = input("4.Role: ")
    
    if role == "student":
        marks = input("enter marks: ")
        status = input("enter status: ")
        return name, username, password, role, marks, status

    return name, username, password, role

def update_requirements():
        name = input("Enter new name: ")
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        return name, username, password
     
    