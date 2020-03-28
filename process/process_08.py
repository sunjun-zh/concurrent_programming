# -*-coding:utf-8-*-
from multiprocessing import Process, Lock
import time


def task(name, mutex):
    # add mutex to disposable
    mutex.acquire()
    print(f'{name} is running')
    time.sleep(1)
    print(f'{name} is done')
    mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    for i in range(5):
        p = Process(target=task, args=(f'zh-{i}', mutex))  # transport mutex-lock to make work in a certain order
        p.start()

    print(f'main process')
