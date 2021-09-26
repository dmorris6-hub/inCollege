import pytest
from add_user import validatePassword, canAdd

#this function checks if the password is valid
@pytest.mark.parametrize('password, result',
                         [
                            #invalid passwords
                            ('1232', 0),
                            ('2_Shor!', 0),
                            ('abcdefg8!', 0),
                            ('TooLong_Pa55word',0),
                            ('missingcap1!',0),
                            ('No-nonAlph5',0),
                            ('',0),                            
                            #valid passwords
                            ('Mark@1234',1),
                            ('aneSsa.9',1),
                            ('h0uS2@jd',1),

                         ]
                         )
def test_validatePassword(password, result):
    assert validatePassword(password) == result



#this function checks if user can sign up based on the number of accounts in the database
def test_canAdd():
    #if the number of accounts is less than 5, return true
    assert(canAdd([(1, )]) == 1)
    assert(canAdd([(2, )]) == 1)
    assert(canAdd([(4, )]) == 1)
    assert(canAdd([(-1, )]) == 1)
    assert(canAdd([(0, )]) == 1)

    #if the number of accounts is more than 5, return false
    assert(canAdd([(5, )]) == 0)
    assert(canAdd([(6, )]) == 0)