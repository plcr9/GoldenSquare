from lib.e_extractor import *

'''With an empty string, empty string returned'''
def test_empty_string_returns_empty_string():
    result = e_extractor("")
    assert result == ""


'''With a string with no e's, it returns the same string it was given'''
def test_without_es_returns_same_string():
    result = e_extractor("juxtaposition")
    assert result == "juxtaposition"

'''With a string with one e, it returns string with e relocated to start of string'''
def test_given_one_e_returns_string_with_e_at_start_of_string():
    result = e_extractor("hello")
    assert result == "ehllo"

'''With a strong with multiple es, it returns string with all es at the start of string'''
def test_given_multiple_es_returns_all_es_at_start_of_string():
    result = e_extractor("heelloe")
    assert result == "eeehllo"

'''with a string with es already at start, it returns same string'''
def test_multiple_es_at_start_of_string_returns_same_string():
    result = e_extractor("eeeasy")
    assert result == "eeeasy"