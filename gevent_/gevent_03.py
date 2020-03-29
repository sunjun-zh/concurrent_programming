# -*-coding:utf-8-*-
import gevent.monkey
gevent.monkey.patch_all() # change python some built-in modules

import time
import requests
import gevent


def fetch():
    url = "https://www.baidu.com/"
    res = requests.get(url=url)


def synchronous():
    [fetch() for i in range(10)]


def asynchronous():
    threads = [gevent.spawn(fetch) for i in range(10)]
    gevent.joinall(threads)


if __name__ == '__main__':
    t1 = time.time()
    synchronous()
    t2 = time.time()
    print(f'sync takes: {t2 - t1}')

    print('-' * 10)

    t3 = time.time()
    asynchronous()
    t4 = time.time()
    print(f'async takes: {t4 - t3}')
