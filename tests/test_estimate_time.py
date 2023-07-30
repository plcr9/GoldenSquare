import pytest

from lib.estimate_time import estimate_reading_time

'''Given text of 200 words, it will return a reading time of 1'''
def test_with_two_hundred_words():
    text = " ".join(["word" for i in range(0, 200)])
    result = estimate_reading_time(text)
    assert result == 1.0

'''Given text of 400 words, it will return a reading time of 2'''
def test_with_four_hundred_words():
    text = " ".join(["word" for i in range(0, 400)])
    result = estimate_reading_time(text)
    assert result == 2.0

'''Given text of 300 words, it will return a reading time of 1.5'''
def test_with_three_hundred_words():
    text = " ".join(["word" for i in range(0, 300)])
    result = estimate_reading_time(text)
    assert result == 1.5

'''Given empty string, it will raise an error'''
def test_with_empty_string():
    with pytest.raises(Exception) as e:
        estimate_reading_time("")
    error_message = str(e.value)
    assert error_message == "Cannot estimate reading time for empty text."