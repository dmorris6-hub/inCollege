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
        print("\nWe're here to help!\n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            general()
    elif (option == "3"):
        print("\nWelcome to InCollege, the world's largest college student netwoek with many users " +
              "in manycountries and territories worldwide.\n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            general()
    elif (option == "4"):
        print("\nIn College Pressroom: Stay on top of the lastest news, updates, and reports.\n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            general()
    elif (option == "5"):
        print("\nUnder construction\n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            general()
    elif (option == "6"):
        print("\nUnder construction\n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            general()
    elif (option == "7"):
        print("\nUnder construction\n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            general()
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
        print("\nUnder construction\n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            usefulLink()
    elif (option == "3"):
        print("\nUnder construction\n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            usefulLink()
    elif (option == "4"):
        print("\nUnder construction\n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            usefulLink()
    elif (option == "5"):
        main()
    else:
        print("Invalid option")
        usefulLink()


def importantLink(guestControl):
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
        print("\nAll rights are reserved for the inCollege Team Michigan. All images and or text afiliated to this site is as well under the ownership off all members aboard the team. All accounts created withing the site are private from third party sources and all data is to be stored on the affiliated owners server.\n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            importantLink(guestControl)
    elif (option == "2"):
        print("/nThis website was created with the intent of promoting success in graduation college students./n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            importantLink(guestControl)
    elif (option == "3"):
        print("\nAs of now this program does not comply with any additional functionality for disabilities\n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            importantLink(guestControl)
    elif (option == "4"):
        print("\nCreating an account hereby signifies that the user has agreeed to the terms and conditions of the app. All personal data is protected to the extent of the affiliated owners hardware.\n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            importantLink(guestControl)
    elif (option == "5"):
        if(guestControl == 1):
            print("\nType 1 to turn off the InCollege Email, SMS, and Targeted Advertising features.")
            print("Otherwise type 2 to go back.\n")
            choice = input()
        else:    
            print("\nGuest Controls have limited access, please login to access this feature.\n")
        importantLink(guestControl)
    elif (option == "6"):
        print("\nAll personal data is protected to the extent of the affiliated owners hardware. The affiliated owners are not responsible for data breaches and or attacks to the hardware physically or otherwise.\n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            importantLink(guestControl)
    elif (option == "7"):
        print("\nAll text and images associated to the site are the property of the owners. Any use of the content outside the context of this application is prohibited by law.\n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            importantLink(guestControl)
    elif (option == "8"):
        print("\nUser cookies are used to ensure the convience of our user. All personal data is protected within the context of our hardware security.\n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            importantLink(guestControl)
    elif (option == "9"):
        print("\nGuests have limited access to the site. In order to ensure full access a valid account must be created and verified.\n")
        print("Type your option: ")
        print("1. Go back")
        choice = input()
        if(choice == "1"):
            importantLink(guestControl)
    elif (option == "10"):
        print("Select your language: \n1. English \n2. Spanish")
    elif (option == "11"):
        main()
    else:
        print("Invalid option")
        importantLink(guestControl)