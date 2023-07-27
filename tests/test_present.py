import pytest

from lib.present import Present

'''Wrap an item, get it back when unwrapping'''
def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

'''if unwrap before wrapping, error message received'''
def test_unwrap_before_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."

'''If wrapping already wrapped present is attempted, error message received'''
def test_wrapping_already_wrapped_present_throws_error():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    message = str(e.value)
    assert message == "A contents has already been wrapped."

'''if attempt to wrap already wrapped present, the first value is unchanged'''
def test_wrapping_already_wrapped_with_first_value_unchanged():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    assert present.unwrap() == 44

