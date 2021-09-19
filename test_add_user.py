import pytest
from add_user import validatePassword, canAdd

#this function checks if the password is valid
def test_validatePassword():
    #invalid password
    assert(validatePassword('1232') == 0)
    assert(validatePassword('abcdef') == 0)
    assert(validatePassword('abc123') == 0)

    #valid password
    assert(validatePassword('Mark@1234') == 1)
    assert(validatePassword('aneSsa.9') == 1)
    assert(validatePassword('h0uS2@jd') == 1)


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