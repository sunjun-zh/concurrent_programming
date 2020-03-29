# -*-coding:utf-8-*-
from collections import deque


def countdown(n):
    while n > 0:
        print(f'T-minus: {n}')
        yield  # Suspend its execution
        n -= 1
    print('blastoff')


def countup(n):
    x = 0
    while x < n:
        print(f'counting up {x}')
        yield
        x += 1

class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        self._task_queue.append(task)

    def run(self):
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                pass



if __name__ == '__main__':
    s = TaskScheduler()
    # s.new_task(countdown(10))
    # s.new_task(countdown(5))
    s.new_task(countup(15))

    s.run()
