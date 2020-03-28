# -*-coding:utf-8-*-
import os
import time
from multiprocessing import Process


def task(name, t):
    print(f'{name}({os.getpid()}) is running')
    time.sleep(t)
    print(f'{name} is done')


if __name__ == '__main__':
    p1 = Process(target=task, args=('zh-1', 1))  # create subprocess
    p2 = Process(target=task, args=('zh-2', 2))  # create subprocess
    p3 = Process(target=task, args=('zh-3', 3))  # create subprocess
    p4 = Process(target=task, args=('zh-4', 4))  # create subprocess

    p1.start()  # send a message to os and prepare subprocess resources
    p1.join()  # main process is working until subprocess is done
    p2.start()  # send a message to os and prepare subprocess resources
    p2.join()  # main process is working until subprocess is done
    p3.start()  # send a message to os and prepare subprocess resources
    p3.join()  # main process is working until subprocess is done
    p4.start()  # send a message to os and prepare subprocess resources
    p4.join()  # main process is working until subprocess is done


    print(f'main process({os.getppid()})')
