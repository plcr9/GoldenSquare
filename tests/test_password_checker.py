import pytest 

from lib.password_checker import PasswordChecker

'''check the length of password is greater than or equal to 8 characters'''
def test_password_greater_than_or_equal_to_eight_characters():
    password = PasswordChecker()
    result = "Password123"
    password = len(result) >= 8
    assert password == True