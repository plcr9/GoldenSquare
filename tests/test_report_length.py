from lib.report_length import report_length

'''Returns the length of a given string'''
def test_string_length():
    result = report_length("34")
    result2 = len(result)
    assert result2 == 34