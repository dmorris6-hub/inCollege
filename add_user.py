from db_connection import db_conn

# Checks if there is room for a new account
def canAdd():
    conn = db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # counts number of users
    cur.execute(f"SELECT COUNT(*) FROM auth;")

    response = cur.fetchall()
    print(response[0][0])
    if (response[0][0] > 4):
        return 0
    else:
        return 1

# Adds user to the database
def addUser():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # finds out if password is allowed
    cap = False
    dig = False
    alp = False
    for elm in password:
        if (elm.isupper()):
            cap = True
        elif (elm.isnumeric()):
            dig = True
        elif (not elm.isalnum()):
            alp = True
        else:
            continue
    
    if (cap and dig and alp and len(password)>=8 and len(password)<=16):
        conn = db_conn()
        # Open a cursor to perform database operations
        cur = conn.cursor()

        # insert user info
        query = f"INSERT INTO auth (username, password) VALUES ('{username}', '{password}');"
        cur.execute(query, (username, password))
        conn.commit()

        return 1
    else:
        print("Password must include minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, one non-alpha character")
        addUser()




    