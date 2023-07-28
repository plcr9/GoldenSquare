from lib.fizzbuzz import *

'''if input is not divisible by 3 or 5, it returns the original number'''
def test_not_divisible_by_3_or_5_returns_number():
    result = fizzbuzz(1)
    assert result == 1

'''if input is divisble by 3, it returns fizz'''
def test_divisible_by_3():
    result = fizzbuzz(9)
    assert result == "Fizz"

'''if input is divisble by 5, it returns fizz'''
def test_divisible_by_5():
    result = fizzbuzz(10)
    assert result == "Buzz"

'''if input is divisble by 3 or 5, it returns fizzbuzz'''
def test_divisible_by_5():
    result = fizzbuzz(15)
    assert result == "FizzBuzz"