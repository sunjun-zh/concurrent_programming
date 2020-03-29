# -*-coding:utf-8-*-
from datetime import datetime
import gevent
from gevent.event import Event

evt = Event()


def producer():
    print(f'producer is running （{gevent.getcurrent()}） at {datetime.now()}')
    gevent.sleep(3)
    print(f'producer is completed （{gevent.getcurrent()}） at {datetime.now()}')
    evt.set()


def customer():
    print(f'customer is running ({gevent.getcurrent()}) at {datetime.now()}')
    evt.wait()  # blocking
    print(f'customer is done ({gevent.getcurrent()}) at {datetime.now()}')



if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(producer),
        gevent.spawn(customer),
        gevent.spawn(customer),
        gevent.spawn(customer),
        gevent.spawn(customer),
    ])
