from lib.todo import *

'''Check whether #TODO is contained within string and is capitalised, if so returns true'''
def test_check_if_todo_is_contained_within_text_with_hashtag():
    result = string_includes_todo("Today I must clear out my shed #TODO")
    assert result == True

'''Check whether TODO is present without # in string, if so returns false'''
def test_check_if_todo_is_contained_within_text_without_hashtag():
    result = string_includes_todo("Today I must clear out my shed TODO")
    assert result == False

'''Check whether # plus some other text is present in string, if so returns false'''
def test_check_if_string_contains_hashtag_plus_text_other_than_todo():
    result = string_includes_todo("Today I must clear out my shed #SHEDCLEAROUT")
    assert result == False

'''Check whether #todo is lowercase, if so returns false'''
def test_check_if_string_contains_hashtag_plus_lowercase_todo():
    result = string_includes_todo("Today I must clear out my shed #todo")