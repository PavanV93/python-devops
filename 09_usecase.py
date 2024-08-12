# login system
username = "ec2-user"
password = "DevOps321"

in_username = input("please enter your username: ")
in_password = input("please enter your_password: ")

if (in_username == username) and (in_password == password):
    print("Login is successful")
else: 
    print("Login failed!!! Please check your credentials")


