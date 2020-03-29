# -*-coding:utf-8-*-
import os
import time
from threading import Thread, Condition, currentThread


class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = Condition()

    def start(self):
        t = Thread(target=self.run)
        t.daemon = True
        t.start()
        print(f'{t.getName()} is starting')

    def run(self):   # set timer
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1  # 0/1
                self._cv.notify_all()

    def wait_for_tick(self):
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()


def countdown(ptimer, nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print(f'({currentThread().getName()})T-minus: {nticks}')
        nticks -= 1


def countup(ptimer, last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print(f'({currentThread().getName()})counting: {n}')
        n += 1


if __name__ == '__main__':
    ptimer = PeriodicTimer(1)
    ptimer.start()

    t1 = Thread(target=countdown, args=(ptimer, 10))
    t2 = Thread(target=countup, args=(ptimer, 5))

    t1.start()
    # t1.join()
    t2.start()
