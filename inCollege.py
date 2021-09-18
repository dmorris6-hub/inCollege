from authorization import isAuthorized
from add_user import canAdd, addUser



def login():
    username = input("Username: ")
    password = input("Password: ")
    next = isAuthorized(username, password)
    if (next):
        ##### INSERT OPTIONS HERE #####
        print('working')
    else:
        print("Login failed...")
        print("Please try again")
        login()


def signup():
    if(canAdd()):
        addUser()
        return 1
    else:
        print("Sorry, we are at user capacity: (5/5)")
        return 0


def main():
    print("---welcome to inCollege!---")
    print(" ")
    print("Please type 'login' to log in to your account")
    print("or type 'signup' to create a new account")

    option = input()
    convert = str(option).lower()

    if (convert == "login"):
        login()
    elif (convert == "signup"):
        if (signup()):
            print("Thank you for signing up!")
            print("Now log in with your new username and password")
            login()
        else:
            main()
    else:
        print("Invalid option")
        main()



if __name__ == "__main__":
    main()