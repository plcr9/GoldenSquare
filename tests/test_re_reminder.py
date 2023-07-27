import pytest
from lib.re_reminder import *

def test_reminder():
    reminder = Reminder("Dale")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"
