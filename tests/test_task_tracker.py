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

'''When multiple tasks added, they are all reflected in the list of tasks'''
def test_add_multiple_tasks():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    tracker.add("Walk the cat")
    tracker.add("Walk the frog")
    assert tracker.list_incomplete() == ["Walk the dog", "Walk the cat", "Walk the frog"]

'''When multiple tasks added and one marked as complete, it disappears from the task list'''
def test_marks_tasks_complete():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    tracker.add("Walk the cat")
    tracker.add("Walk the frog")
    tracker.mark_complete(1)
    assert tracker.list_incomplete() == ["Walk the dog", "Walk the frog"]