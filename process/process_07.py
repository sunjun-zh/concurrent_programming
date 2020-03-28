# -*-coding:utf-8-*-
from multiprocessing import Process
import time


def task(name):
    print(f'{name} is running')
    time.sleep(1)
    # p = Process(target=task, args=('zh',))  # if subprocess set daemon, subprocess cant create children
    # p.start()
    print(f'{name} is done')


if __name__ == '__main__':
    p1 = Process(target=task, args=('zh-1',))  # create subprocess
    p2 = Process(target=task, args=('zh-2',))  # create subprocess
    p1.daemon = True  # daemon_subprocess will kill when main process finish
    p1.start()  # send a message to os and prepare subprocess resources
    p2.start()
    # p.join()
    print(f'main process')
