from lib.make_snippet import make_snippet

'''Given empty string, returns empty string'''
def test_given_empty_string_returns_empty_string():
    result = make_snippet("")
    assert result == ""


'''Given string of 4 words, returns same string'''
def test_given_four_words_returns_same_string():
    result = make_snippet("one two three four")
    assert result == "one two three four"

'''Given string of 5 words, returns same string'''
def test_given_five_words_returns_same_string():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"

'''Given string of 6 words, returns first 5 words and a ...'''
def test_given_six_words_returns_string_of_first_five_words_plus_dotdotdot():
    result = make_snippet("one two three four five six")
    assert result == "one two three four five ..."