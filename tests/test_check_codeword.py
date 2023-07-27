from lib.check_codeword import check_codeword

'''If codeword is correct, returns 'come in!'''
def test_codeword_is_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

'''If codeword is wrong, returns WRONG'''
def test_codeword_is_incorrect():
    result = check_codeword("cat")
    assert result == "WRONG!"

'''If codeword has correct first and last letter, returns Close, but nope'''
def test_with_near_codeword():
    result = check_codeword("house")
    assert result == "Close, but nope."

'''If first letter is correct and last letter is incorrect, returns WRONG'''
def test_with_first_correct_and_last_incorrect_letter():
    result = check_codeword("hat")
    assert result == "WRONG!"

'''If last letter is correct and first letter is incorrect, returns WRONG'''
def test_with_last_correct_and_first_incorrect_letter():
    result = check_codeword("mouse")
    assert result == "WRONG!"