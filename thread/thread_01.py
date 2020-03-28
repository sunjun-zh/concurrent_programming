# -*-coding:utf-8-*-
import time
from threading import Thread


def task(name):
    print(f'{name} is running')
    time.sleep(1)
    print(f'{name} is done')


if __name__ == '__main__':
    t = Thread(target=task, args=('zh',))
    t.start()
    t.join()

    print('main thread')