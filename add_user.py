
# Checks if there is room for a new account
def canAdd(response):
    print(response)
    if (response[0][0] > 4):
        return 0
    else:
        return 1

def totalAccount():
    conn = db_conn()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # counts number of users
    cur.execute(f"SELECT COUNT(*) FROM auth;")
    return cur.fetchall()

def validatePassword(password): 
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
        return 1
    else:
        return 0

# Adds user to the database
def addUser():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    # finds out if password is allowed
    if (validatePassword(password) == 1):
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


from db_connection import db_conn




    