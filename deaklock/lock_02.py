# -*-coding:utf-8-*-
import time
from threading import Thread, RLock

# 递归锁:可以连续acquire多次，每acquire一次计数器+1，只有计数为0时，才能被抢到acquire
mutex_1 = mutex_2 = RLock()


class Customize_Thread(Thread):
    def run(self):
        self.fn1()
        self.fn2()

    def fn1(self):
        mutex_1.acquire()
        print(f'(fn1){self.name} get mutex_1')

        mutex_2.acquire()
        print(f'(fn1){self.name} get mutex_2')

        mutex_1.release()
        print(f'(fn1){self.name} release mutex_1')

        mutex_2.release()
        print(f'(fn1){self.name} release mutex_2')

    def fn2(self):
        mutex_2.acquire()
        print(f'(fn2){self.name} get mutex_2')

        mutex_1.acquire()
        print(f'(fn2){self.name} get mutex_1')

        mutex_2.release()
        print(f'(fn2){self.name} release mutex_2')

        mutex_1.release()
        print(f'(fn2){self.name} release mutex_1')


if __name__ == '__main__':

    for i in range(20):
        t = Customize_Thread()
        t.start()
