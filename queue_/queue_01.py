# -*-coding:utf-8-*-
import time
import queue

q = queue.Queue(3) # first in first out; contain a lock

def task():
    q.put('a')
    q.put('b')
    q.put('c')

    time.sleep(1)

    print(q.get())
    print(q.get())
    print(q.get())


if __name__ == '__main__':
    task()

    # _sentinel1 = object()
    # _sentinel2 = object()
    # print(_sentinel1 == _sentinel2)


