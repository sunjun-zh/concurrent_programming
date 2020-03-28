# -*-coding:utf-8-*-
import os
import time
from multiprocessing import Process

def task(name):
    print(f'{name}({os.getpid()}) is running')
    time.sleep(3)
    print(f'{name} is done')


if __name__ == '__main__':
    p = Process(target=task, args=('zh',)) # create subprocess

    p.start() # send a message to os and prepare subprocess resources

    p.join() # main process is working until subprocess is done

    print(f'main process({os.getppid()}) subprocess_id({os.getpid()})')
    print('subprocess_id::', p.pid)
    print('subprocess_is_alive::', p.is_alive())

