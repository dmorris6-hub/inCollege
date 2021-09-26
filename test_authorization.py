import pytest
from authorization import isAuthorized


#check if isAuthorize correctly detects account already exists in the database
#for accounts that return 1, change the username and password into what you have in your database
@pytest.mark.parametrize('username, password, result',
    #return 0 if account doesnt exist
                            ('anessa23', 'An23@abc1', 0),
                            ('jim2301', 'Jim@2a53f', 0),
                            ('panther902', 'P4na3.def', 0),
                            ('kelly324', 'kElly34.xyz',0),
    #return 1 if account already exists
                            ('kevin23', 'Keva.2421',1),
    #Change these values into any account you have in your database
    #Or sign up with these accounts before testing
                            ('nhi34', 'nhi@nguyen35',1)

)
def test_isAuthorized(username, password, result):
    assert isAuthorized(username, password) == result



