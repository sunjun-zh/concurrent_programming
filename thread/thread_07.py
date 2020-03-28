# -*-coding:utf-8-*-
import time
import os
from threading import Thread, Lock

NUM = 10

def task(name):
    mutex.acquire()
    print(f'{name} is running')
    global NUM
    time.sleep(0.5)
    NUM -= 1
    print(f'{name} is done: {NUM}')
    mutex.release()



if __name__ == '__main__':
    mutex = Lock()
    t_list = []
    for i in range(8):
        t = Thread(target=task, args=(f'zh_{i}',))
        t_list.append(t)
        t.start()

    [t.join() for t in t_list]

    print(f'--main-{NUM}')




