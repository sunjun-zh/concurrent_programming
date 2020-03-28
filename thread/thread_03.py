# -*-coding:utf-8-*-
import time
import os
from threading import Thread


def task(name):
    print(f'{name} is running')
    time.sleep(1)
    print(f'{name} is done:: {os.getppid()}')


if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=task, args=(f'zh-{i}',))
        t.start()
        t.join()

    print(f'main thread({os.getppid()})')