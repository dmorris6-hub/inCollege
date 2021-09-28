def general():
    from inCollege import signup
    print("Type your option to view: ")
    print("1. Sign up")
    print("2. Help Center")
    print("3. About")
    print("4. Press")
    print("5. Blog")
    print("6. Careers")
    print("7. Developers")
    print("8. Go back")
    option = input()
    if (option == "1"):
        signup()
    elif (option == "2"):
        print("We're here to help!")
    elif (option == "3"):
        print("Welcome to InCollege, the world's largest college student netwoek with many users " +
              "in manycountries and territories worldwide.")
    elif (option == "4"):
        print(
            "In College Pressroom: Stay on top of the lastest news, updates, and reports.")
    elif (option == "5"):
        print("Under construction")
    elif (option == "6"):
        print("Under construction")
    elif (option == "7"):
        print("Under construction")
    elif (option == "8"):
        usefulLink()


def usefulLink():
    from inCollege import main
    print("Type your option to view: ")
    print("1. General")
    print("2. Browse InCollege")
    print("3. Business Solutions")
    print("4. Directories")
    print("5. Go back")
    option = input()
    if (option == "1"):
        general()
    elif (option == "2"):
        print("Under construction")
    elif (option == "3"):
        print("Under construction")
    elif (option == "4"):
        print("Under construction")
    elif (option == "5"):
        main()
    else:
        print("Invalid option")
        usefulLink()


def importantLink():
    from inCollege import main
    print("Type your option to view: ")
    print("1. A Copyright Notice")
    print("2. About")
    print("3. Accessibility")
    print("4. User Agreement")
    print("5. Privacy Policy")
    print("6. Cookie Policy")
    print("7. Copyright Policy")
    print("8. Brand Policy")
    print("9. Guest Control")
    print("10. Language")
    print("11. Go back")
    option = input()
    if (option == "1"):
        print("")
    elif (option == "2"):
        print("")
    elif (option == "3"):
        print("")
    elif (option == "4"):
        print("")
    elif (option == "5"):
        print("Guest Controls")
    elif (option == "6"):
        print("")
    elif (option == "7"):
        print("")
    elif (option == "8"):
        print("")
    elif (option == "9"):
        print("")
    elif (option == "10"):
        print("Select your language: \n1. English \n2. Spanish")
    elif (option == "11"):
        main()
    else:
        print("Invalid option")
        importantLink()
