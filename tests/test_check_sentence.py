from lib.check_sentence import check_sentence_grammar

'''Given valid sentence with a capital letter and a full stop, it returns True'''
def test_with_valid_sentence():
    result = check_sentence_grammar("Hello, it's a fine day.")
    assert result == True

'''Given setence with a capital letter but no full stop or other mark, it returns False'''
def test_with_capital_letter_but_no_ending_mark():
    result = check_sentence_grammar("Hello, it's a fine day")
    assert result == False

'''Given valid sentence with a capital letter and a question mark, it returns True'''
def test_with_capital_letter_and_question_mark():
    result = check_sentence_grammar("Hello, is it a fine day?")
    assert result == True

'''Given valid sentence with a capital letter and an exclamation mark, it returns True'''
def test_with_capital_letter_and_exclamation_mark():
    result = check_sentence_grammar("Hello, it's a fine day!")
    assert result == True

'''Given valid sentence with a capital letter but with a comma at the end, it returns False'''
def test_with_captial_letter_and_comma_at_end():
    result = check_sentence_grammar("Hello, it's a fine day,")
    assert result == False

'''Given valid sentence with a capital letter but with a colon at the end, it returns False'''
def test_with_capital_letter_and_colon():
    result = check_sentence_grammar("Hello, it's a fine day:")
    assert result == False

'''Given sentence with lowercase letter at beginning and a full stop at the end, it returns False'''
def test_with_lowercase_start_letter_and_full_stop():
    result = check_sentence_grammar("hello, it's a fine day.")
    assert result == False