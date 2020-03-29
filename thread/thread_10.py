# -*-coding:utf-8-*-
import random
import time
from threading import Thread, currentThread
from concurrent.futures import ProcessPoolExecutor


def some_works():
    total = 1
    for i in range(1, random.randint(10, 20)):
        total *= i
    return total


def task(pool):
    print(f'{currentThread().getName()} is running')
    r = pool.submit(some_works).result()
    print(f'{currentThread().getName()} get result: {r}')


if __name__ == '__main__':
    start = time.time()
    pool = ProcessPoolExecutor()

    for i in range(5):
        t = Thread(target=task, args=(pool,))
        t.start()
        t.join()
    end = time.time()
    print(f'main:  {end - start}')
