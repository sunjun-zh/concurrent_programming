# -*-coding:utf-8-*-
import time
from threading import Thread, currentThread


def task(name):
    print(f'{name} is running')
    time.sleep(0.5)
    print(f'{name} is done')



if __name__ == '__main__':
    t1 = Thread(target=task, args=('zh_1',))
    t2 = Thread(target=task, args=('zh_2',))

    t1.daemon = True # waiting other threads finish
    t1.start()
    t2.start()

    print('--main-')

    print(f'main-thread: {currentThread().is_alive()}')
    print(f't1-thread: {t1.is_alive()}')

