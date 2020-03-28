# -*-coding:utf-8-*-
from multiprocessing import Process
import time

NUM = 99

def task(name):
    print(f'{name} is running')
    time.sleep(1)
    global NUM
    NUM += 1
    print(f'{name} is done, {NUM}')


if __name__ == '__main__':
    p = Process(target=task, args=('zh',)) # create subprocess

    p.start() # send a message to os and prepare subprocess resources
    # p.join()
    print(f'main process {NUM}')
