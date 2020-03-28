# -*-coding:utf-8-*-
import os
import time
import random
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def content():
    print(f'{os.getpid()} is running')
    res = random.randint(6, 101)
    return dict(name=os.getpid(), res=res)


def say_hi(data):
    print(f'{data["name"]} want to say {data["res"]}')


if __name__ == '__main__':
    pool = ThreadPoolExecutor(10)

    result = pool.submit(content).result()
    say_hi(result)

    pool.shutdown()  # pool.close() + pool.join()

    print('main process')