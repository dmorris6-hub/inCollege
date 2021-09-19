import pytest
from authorization import isAuthorized


#check if isAuthorize correctly detects account already exists in the database
#for accounts that return 1, change the username and password into what you have in your database

def test_isAuthorized():
    #return 0 if account doesnt exist
    assert isAuthorized('nhi34', 'nhiguyen') == 0
    assert isAuthorized('', 'nhiguyen') == 0
    assert isAuthorized('nhi34', 'nhiguyen') == 0
    assert isAuthorized('nhi34', 'nhiguyen') == 0

    #return 1 if account already exists
    assert isAuthorized('kevin23', 'Keva.421') == 1 #Change these values into any account you have in your database
    assert isAuthorized('nhi34', 'nhiguyen') == 1 #Or sign up with these accounts before testing



