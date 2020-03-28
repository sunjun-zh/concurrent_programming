# -*-coding:utf-8-*-
import random
import time
from threading import Thread, currentThread, Semaphore

mutex = Semaphore(3) # when thread get semaphore, acquire'count will reduce one

def task():
    # mutex.acquire()
    # print(f'{currentThread().getName()} get lock')
    #
    # print(f'{currentThread().getName()} is working')
    #
    # print(f'{currentThread().getName()} release lock')
    # mutex.release()

    with mutex:
        print(f'{currentThread().getName()} is working')
        time.sleep(random.randint(1,2))


if __name__ == '__main__':
    for i in range(20):
        t = Thread(target=task)
        t.start()