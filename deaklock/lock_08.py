# -*-coding:utf-8-*-
import os
import time
from threading import Thread, Condition


def producer(n):
    print(f'(p){os.getpid()} is running')
    global l
    if lock_con.acquire():
        time.sleep(1)
        l.append(n)
        print(f'(p){os.getpid()} product {n}')
        lock_con.notify()
        lock_con.release()


def consumer():
    print(f'(c){os.getpid()} is running')
    global l
    lock_con.acquire()
    if len(l) == 0:
        lock_con.wait()
    time.sleep(0.5)
    res = l.pop()
    print(f'(c){os.getpid()} consume {res}')
    lock_con.release()

    print(f'(c){os.getpid()} is running')


if __name__ == '__main__':
    l = []
    lock_con = Condition()

    p1 = Thread(target=producer, args=(5,))
    p2 = Thread(target=producer, args=(6,))
    p3 = Thread(target=producer, args=(7,))
    c1 = Thread(target=consumer)
    c2 = Thread(target=consumer)

    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()
