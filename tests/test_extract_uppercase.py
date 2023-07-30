from lib.extract_uppercase import *

'''Given a lower and an uppercase word, returns a list with the uppercase word'''
def test_extract_uppercase_with_upper_case_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

'''Given two uppercase words, returns a list with both words'''
def test_extract_uppercase_returns_both_uppercase():
    result = extract_uppercase("HELLO WORLD")
    assert result == ["HELLO", "WORLD"]

'''Given two lowercase words, return an empty string'''
def test_two_lowercase_returns_empty_string():
    result = extract_uppercase("hello world")
    assert result == []

'''Given mixed case word, return an empty list'''
def test_mixed_case_word_returns_empty_string():
    result = extract_uppercase("hello WoRlD")
    assert result == []

'''Given lowercase word with uppercase word with exclamation mark, returns list with uppercase word, but no exclamation mark'''
def test_uppercase_word_with_exclamation_mark_returns_uppercase_without_exclamation_mark():
    result = extract_uppercase("hello WORLD!")
    assert result == ["WORLD"]

'''Given empty string it returns an empty list'''
def test_empty_string_returns_empty_list():
    result = extract_uppercase("")