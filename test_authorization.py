import pytest
from authorization import isAuthorized


#check if isAuthorize correctly detects account already exists in the database
#for accounts that return 1, change the username and password into what you have in your database

def test_isAuthorized():
    #return 0 if account doesnt exist
    assert isAuthorized('anessa23', 'An23@abc1') == 0
    assert isAuthorized('jim2301', 'Jim@2a53f') == 0
    assert isAuthorized('panther902', 'P4na3.def') == 0
    assert isAuthorized('kelly324', 'kElly34.xyz') == 0

    #return 1 if account already exists
    assert isAuthorized('kevin23', 'Keva.2421') == 1 #Change these values into any account you have in your database
    assert isAuthorized('nhi34', 'nhi@nguyen35') == 1 #Or sign up with these accounts before testing



