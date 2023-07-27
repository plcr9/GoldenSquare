from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Dale")
    reminder.remind_me_to("Paint the spare room")
    result = reminder.remind()
    assert result == "Paint the spare room, Dale!"