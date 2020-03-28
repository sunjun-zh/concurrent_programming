# -*-coding:utf-8-*-
import time
from threading import Thread, currentThread, active_count, enumerate


def task(name):
    print(f'{name} is running, thread_name:{currentThread().getName()}')
    time.sleep(1)
    print(f'{name} is done')


if __name__ == '__main__':
    t = Thread(target=task, args=('zh',), name='zh_thread_1')
    t.start()
    t.setName('zh_thread_2')
    print(f'name:{t.getName()} status:{t.is_alive()}')

    currentThread().setName('main_thread') # main thread

    t.join()
    print(f'threads: {active_count()}')
    print(enumerate())


