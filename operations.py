from db import connect,insert,delete,update,report,browse_user,insert_user_register
def login():
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    selector = browse_user(user,password)
    if selector:
        print("successfully logged in")
    else:
        print("user credentials wrong")
    return selector
def insert_user():
    name = input("Enter the username: ")
    flag1 = insert(name)
    if flag1:
        print(flag1)
def delete_user():
    id_u = input("Enter the id: ")
    name = input("Enter the name: ")
    flag1 = delete(id_u, name)
    if flag1:
        print(flag1)
def update_user():
    id_u = input("Enter the id: ")
    name = input("Enter the name: ")
    flag1 = update(id_u, name)
    if flag1:
        print(flag1)
def report_on_customers():
    data = report()
    print(data)
def register():
    name = input("Enter the name: ")
    password = input("Enter the password: ")
    flag2 = insert_user_register(name,password)
    if flag2:
        print(flag2)
    return flag2
    