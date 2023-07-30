from lib.extract_uppercase import *

'''Given a lower and an uppercase word, returns a list with the uppercase word'''
def test_extract_uppercase_with_upper_case_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]