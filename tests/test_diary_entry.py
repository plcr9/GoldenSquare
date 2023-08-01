import pytest
from lib.diary_entry import DiaryEntry

'''Given an empty title, it raises an error'''
def test_errors_on_empty_title():
    with pytest.raises(Exception) as err:
        DiaryEntry("", "my contents")
    assert str(err.value) == "Diary entries must have a title and contents"

'''Given an empty contents, it raises an error'''
def test_errors_on_empty_contents():
    with pytest.raises(Exception) as err:
        DiaryEntry("my title", "")
    assert str(err.value) == "Diary entries must have a title and contents"

'''Given a title and contents, format returns formatted entry, like 'My Title: These are the contents'''
def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.format()
    assert result == "My Title: Some contents"

'''Given a title and some contents, count_words returns the number of words in the title and contents'''
def test_counts_words_in_both_title_and_contents():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.count_words()
    assert result == 4

'''Given a wpm of 2, reading_time returns the number of minutes it will take to read the contents'''
def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntry("My Title", "Some contents")
    result = diary_entry.reading_time(2)
    assert result == 1

'''Given a wpm of 2 and text of 4 words, reading_time returns 2 minutes'''
def test_reading_time_with_two_wpm_and_four_words():
    diary_entry = DiaryEntry("My Title", "one two three four")
    result = diary_entry.reading_time(2)
    assert result == 2

'''Given a wpm of 2 and text of 3 words, reading_time returns 2 minutes'''
def test_reading_time_with_two_wpm_and_three_words():
    diary_entry = DiaryEntry("My Title", "one two three")
    result = diary_entry.reading_time(2)
    assert result == 2

'''Given a wpm of 0, reading_time raises an error'''
def test_reading_time_wpm_of_zero():
    diary_entry = DiaryEntry("My Title", "one two three")
    with pytest.raises(Exception) as err:
        diary_entry.reading_time(0)
    assert str(err.value) == "Cannot calculate reading time with wpm of 0"

'''Given contents of six words, and wpm of 2, and reading_time of 2 minutes, reading_chunk returns first four words'''
def test_reading_chunk_with_two_wpm_and_two_minutes():
    diary_entry = DiaryEntry("My Title", "one two three four five six")
    result = diary_entry.reading_chunk(2, 2)
    assert result == "one two three four"

'''Given contents of seven words, and wpm of 2 and 1 minute. First time reading_chunk returns on two. Next time, returns three four'''
def test_reading_chunk_with_two_wpm_and_one_minute_called_multiple_times():
    diary_entry = DiaryEntry("My title", "one two three four five six seven")
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(2, 1) == "three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"
    assert diary_entry.reading_chunk(1, 1) == "seven"

'''Given contects of six words, if reading_chunk isa called repeatedly, the last chunk is the last words in the text. The next chunk after that is at the start again'''
def test_reading_chunk_wraps_on_multiple_calls():
    diary_entry = DiaryEntry("My title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 2) == "one two three four"
    assert diary_entry.reading_chunk(2, 2) == "five six"
    assert diary_entry.reading_chunk(2, 2) == "one two three four"

'''Given contects of six words, if reading_chunk isa called repeatedly, the last chunk is the last words in the text. The next chunk after that is at the start again'''
def test_reading_chunk_wraps_on_multiple_calls_with_exact_ending():
    diary_entry = DiaryEntry("My title", "one two three four five six")
    assert diary_entry.reading_chunk(2, 2) == "one two three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"
    assert diary_entry.reading_chunk(2, 2) == "one two three four"