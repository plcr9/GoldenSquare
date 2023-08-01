from lib.task_tracker import TaskTracker

'''Initially, there are no tasks'''
def test_initially_has_no_tasks():
    tracker = TaskTracker()
    assert tracker.list_incomplete() == []

'''When task added, it is reflected in list of tasks'''
def test_add_task_reflected_in_tasks():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    assert tracker.list_incomplete() == ["Walk the dog"]