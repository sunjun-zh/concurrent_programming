# -*-coding:utf-8-*-
import time
from threading import Timer, currentThread


class Work():
    def __init__(self):
        self.job()

    def job(self):
        self.task()
        t = Timer(3, self.job)
        t.start()

    def task(self):
        print(f'{currentThread().getName()} is working')

    def run(self):
        while True:
            pass


if __name__ == '__main__':
    w = Work()
    w.run()
