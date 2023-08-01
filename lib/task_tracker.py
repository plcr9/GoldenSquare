class TaskTracker():
    def __init__(self):
        self._tasks = []

    def add(self, task):
        self._tasks.append(task)

    def list_incomplete(self):
        return self._tasks

    def mark_complete(self, index):
        del self._tasks[index]