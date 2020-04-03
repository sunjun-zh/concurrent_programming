# -*-coding:utf-8-*-
import gevent.monkey;

gevent.monkey.patch_all()

import requests
import gevent
from gevent.lock import Semaphore

mutex = Semaphore(1)
HEADER = None


def prepare_headers():
    with mutex:
        global HEADER
        if HEADER is None:
            HEADER = 123
    return HEADER


def fetch():
    try:
        url = "https://www.baidu.com"
        headers = prepare_headers()
        res = requests.get(url)
        print(f'headers: {headers}, response: {res.status_code}')

    except Exception as e:
        print(f'{gevent.getcurrent().name} has error {e}')


def worker():
    print(f'{gevent.getcurrent().name} is running')
    while True:
        fetch()


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(worker),
        gevent.spawn(worker),
        gevent.spawn(worker),
    ])
