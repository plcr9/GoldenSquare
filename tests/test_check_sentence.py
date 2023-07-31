from lib.check_sentence import check_sentence_grammar

'''Given valid sentence with a capital letter and a full stop, it returns True'''
def test_with_valid_sentence():
    result = check_sentence_grammar("Hello, it's a fine day!")
    assert result == True

'''Given setence with a capital letter but no full stop or other mark, it returns False'''
def test_with_capital_letter_but_no_ending_mark():
    result = check_sentence_grammar("Hello, it's a fine day")
    assert result == False