from authorization import isAuthorized
from add_user import canAdd, addUser, totalAccount

# Handles logins
def login():
    from user_page import userPage
    username = input("Username: ")
    password = input("Password: ")
    next = isAuthorized(username, password)
    if (next):
        print('working')
        userPage()
    else:
        print("Login failed...")
        print("Please try again")
        login()

# handles signups
def signup():
    response = totalAccount()
    if(canAdd(response)): 
        addUser()
        return 1
    else:
        print("Sorry, we are at user capacity: (5/5)")
        return 0

def main():
    print(" ")
    print("---welcome to inCollege!---")
    print(" ")
    print("Please type 'login' to log in to your account")
    print("or type 'signup' to create a new account")

    option = input()
    convert = str(option).lower()

    # interprests user input
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



