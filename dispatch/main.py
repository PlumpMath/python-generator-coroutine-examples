#! /usr/bin/python3

from collections import deque


def task(name, times):

    for i in range(times):
        yield
        print(name, i)


class Runner(object):

    def __init__(self, tasks):
        self.tasks = deque(tasks)

    def next(self):
        return self.tasks.pop()

    def run(self):
        while len(self.tasks):
            task = self.next()
            try:
                next(task)
            except StopIteration:
                pass
            else:
                self.tasks.appendleft(task)


if __name__ == '__main__':
    Runner([
        task('hsfzxjy', 5),
        task('Jack', 4),
        task('Bob', 6)
    ]).run()
