# -*-coding:utf-8-*-
from multiprocessing import Process
import time


def task(name):
    print(f'{name} is running')
    time.sleep(3)
    print(f'{name} is done')


if __name__ == '__main__':
    p = Process(target=task, args=('zh',)) # create subprocess

    p.start() # send a message to os and prepare subprocess resources
    p.terminate() # force kill subprocess
    time.sleep(2)
    print('main process')
