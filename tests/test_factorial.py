from lib.factorial import *

'''Given a factorial of 5, it should return 120 (5 x 4 x 3 x 2 x 1)'''
def test_factorial_of_5_returns_120():
    result = factorial(5)
    assert result == 120

'''Given a factorial of 3, it should return 6 (3 x 2 x 1)'''
def test_factorial_of_3_returns_6():
    result = factorial(3)
    assert result == 6

'''Given a factorial of 7, it should return 5040 (7 x 6 x 5 x 4 x 3 x 2 x 1)'''
def test_factorial_of_7_returns_5040():
    result = factorial(7)
    assert result == 5040