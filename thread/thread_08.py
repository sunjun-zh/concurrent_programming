# -*-coding:utf-8-*-
import time
from threading import Thread
from multiprocessing import Process


class CountdownTask(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        while self.n > 0:
            print(f'T-minus {self.n}')
            self.n -= 1
            time.sleep(2)


if __name__ == '__main__':
    c = CountdownTask(5)

    p = Process(target=c.run)
    p.start()
