# -*-coding:utf-8-*-
import time
import random
from threading import Thread
import gevent


def task(pid):
    gevent.sleep(random.randint(0, 2) * 0.001)
    print(f'task {pid} done')

def synchronous():
    [task(i) for i in range(10)]
    # for i in range(10):
    #     t = Thread(target=task, args=(i, ), daemon=True)
    #     t.start()
    #     t.join()

def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)

if __name__ == '__main__':
    t1 = time.time()
    synchronous()
    t2 = time.time()
    print(f'sync takes: {t2-t1}')

    print('-'*10)

    t3 = time.time()
    asynchronous()
    t4 = time.time()
    print(f'async takes: {t4-t3}')

