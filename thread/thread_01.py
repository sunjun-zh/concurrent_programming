# -*-coding:utf-8-*-
import time
from threading import Thread


def task1(name):
    print(f'{name} is running')

    while 1:
        time.sleep(1)
        print(f'{name} is done')


def task2(name):
    print(f'{name} is running')
    while 1:
        time.sleep(1)
        print(f'{name} is done')

if __name__ == '__main__':
    t = Thread(target=task1, args=('zh',))
    t2 = Thread(target=task2, args=('zh',))
    t.start()
    t2.start()
    # t.join()

    print('main thread')