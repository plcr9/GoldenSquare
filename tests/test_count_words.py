from lib.count_words import *

'''Empty string returns 0 words'''
def test_empty_string_returns_zero_words():
    result = count_words(" ")
    assert result == 0

'''Returns the total number of words in a given string'''
def test_total_number_of_words_in_string():
    result = count_words("One two three")
    assert result == 3